import argparse
import json
import logging
import os
import shutil
import sys
import re
from datetime import datetime
from pathlib import Path
from typing import Any

from langchain.chat_models.base import BaseChatModel
from langchain_community.chat_models import ChatOpenAI, AzureChatOpenAI
from langchain.embeddings import CacheBackedEmbeddings
from langchain.storage import LocalFileStore
from langchain_community.embeddings import AzureOpenAIEmbeddings, OpenAIEmbeddings

import dotenv
from dseval import ProblemSet, Evaluator
from dseval.agent import (
    CoMLAgent,
    PreloadAgent,
    ChapyterAgent,
    JupyterAIAgent,
    CodeInterpreterAgent,
    TentativeSolutions,
)


_logger = logging.getLogger("dseval")


def resolve_running_environment(problemset_path: Path, run_dir: Path = Path("runs")):
    run_dir.mkdir(exist_ok=True, parents=True)

    # Delete old files
    for file in run_dir.iterdir():
        if file.is_file() or file.is_symlink():
            file.unlink()
        else:
            shutil.rmtree(file)

    # Link input directory
    if (problemset_path.parent / "_inputs").exists():
        shutil.copytree(
            (problemset_path.parent / "_inputs").resolve(), run_dir / "_inputs"
        )
    else:
        # No data required.
        pass


def glob_problemsets(problemset_path: Path) -> list[Path]:
    problemsets = sorted(problemset_path.glob("*.py"))
    if problemset_path.name == "pandasexec":
        problemsets = [p for p in problemsets if p.name[0].isdigit()]
    return problemsets


def configure_llm(model: str, endpoint: str):
    if endpoint == "aoai":
        from msllm_extensions import AzureChatOpenAIWithTooling
        return AzureChatOpenAIWithTooling(
            temperature=0.0,
            azure_deployment=model,
            api_version="2023-12-01-preview",
            max_retries=30,
        )
    elif endpoint == "aiyyds":
        dotenv.load_dotenv(".env/aiyyds.env")
        if model == "gpt-35-turbo":
            model = "gpt-3.5-turbo"
        if model == "gpt-4":
            model = "gpt-4-1106-preview"
        return ChatOpenAI(
            temperature=0.0,
            model=model,
            max_retries=10,
            request_timeout=60,
            max_tokens=1000,
        )
    elif endpoint == "substrate":
        if model != "gpt-35-turbo":
            raise ValueError("Only gpt-35-turbo is supported for SubstrateChatLLM")
        from msllm_extensions import SubstrateChatLLM
        return SubstrateChatLLM(temperature=0.0, max_retries=10, max_tokens=1000)
    elif endpoint == "azureml":
        from msllm_extensions import AzureMLModel
        dotenv.load_dotenv(".env/azureml.env")
        if model == "llama2-70b":
            model = "llama-2-70b-chat-13"
        elif model == "llama2-13b":
            model = "llama-2-13b-chat-7"
        elif model == "llama2-7b":
            model = "llama-2-7b-chat-15"
        return AzureMLModel(model=model, temperature=0.0, max_retries=10)
    elif endpoint == "google":
        from langchain_google_genai import ChatGoogleGenerativeAI

        if model != "gemini-pro":
            raise ValueError("Only gemini-pro is supported for GoogleChatLLM")
        dotenv.load_dotenv(".env/google.env")
        return ChatGoogleGenerativeAI(model=model, temperature=0.0)
    elif endpoint == "llamacpp":
        from msllm_extension import LlamaCppClient
        dotenv.load_dotenv(".env/llamacpp.env")
        if model == "codellama-7b":
            model = "CodeLlama-7B-Instruct"
        elif model == "codellama-13b":
            model = "CodeLlama-13B-Instruct"
        elif model == "codellama-34b":
            model = "CodeLlama-34B-Instruct"
        return LlamaCppClient(
            model=model,
            temperature=0.0,
            max_length=16384,
            max_tokens=600,
            prompt_strategy="reddit",
        )
    else:
        raise ValueError(f"Unknown endpoint {endpoint}")


def configure_agent(model: str, prompt: str, llm: BaseChatModel, debug: bool):
    if prompt.startswith("coml"):
        return CoMLAgent(llm)
    elif prompt == "chapyter":
        return ChapyterAgent(llm)
    elif prompt == "jupyterai":
        return JupyterAIAgent(llm)
    elif prompt == "codeinterpreterapi":
        return CodeInterpreterAgent(llm)
    else:
        raise ValueError(f"Unknown prompt {prompt}")


def _test_problemset(args: argparse.Namespace, problemset_path: Path):
    if problemset_path.is_dir():
        problemsets = glob_problemsets(problemset_path)
    else:
        problemsets = [problemset_path]

    # Resolve output directory

    if args.evaluate_from:
        # Using the specified directory as output directory
        if args.solve_only:
            raise ValueError(
                "Cannot use --solve-only and --evaluate-from at the same time"
            )
        _logger.info(
            "Model, endpoint and prompt will be ignored when evaluating with --evaluate-from. "
            "Evaluating from: %s",
            args.evaluate_from,
        )
        output_dir = Path(args.evaluate_from)
        agent = PreloadAgent()
    else:
        # Configure th agent
        llm = configure_llm(args.model, args.endpoint)
        agent = configure_agent(args.model, args.prompt, llm, args.debug)

        # Guessing the output directory
        output_dir = (
            Path("results")
            / ("version-" + datetime.now().strftime("%m%d"))
            / (
                args.model
                + "-"
                + args.endpoint
                + ("-" + args.prompt if args.prompt != "coml" else "")
                + (
                    "-r"
                    + str(args.retry)
                    + ("hint" if args.retry_hint else "")
                    + ("reset" if args.retry_reset else "")
                    if args.retry
                    else ""
                )
                + ("-errorprop" if args.error_propagation else "")
            )
        )

        if problemset_path.is_dir():
            output_dir = output_dir / problemset_path.resolve().relative_to(
                Path(".").resolve()
            )
        else:
            output_dir = output_dir / problemset_path.parent.resolve().relative_to(
                Path(".").resolve()
            )

        if "benchmark" in output_dir.name:
            output_dir = output_dir.parent

        if args.solve_only:
            output_dir = output_dir / "solutions"

    _logger.info("Output diretory: %s", output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    if output_dir.name == "solutions":
        run_dir_name = output_dir.parent.parent.name + "-" + output_dir.parent.name
    else:
        run_dir_name = output_dir.parent.name + "-" + output_dir.name

    evaluator_kwargs = {}
    if args.retry:
        evaluator_kwargs["max_retries"] = args.retry
        if args.retry_hint:
            evaluator_kwargs["retry_hint"] = True
        if args.retry_reset:
            evaluator_kwargs["retry_reset"] = True
    if args.error_propagation:
        evaluator_kwargs["error_propagation"] = True
    if args.endpoint == "google":
        evaluator_kwargs["ignore_solver_failure"] = True
    if "-dflida" in args.prompt:
        evaluator_kwargs["ignore_solver_failure"] = True
    evaluator = Evaluator(**evaluator_kwargs)

    for idx, problemset in enumerate(problemsets, start=1):
        solver.reset()

        if isinstance(solver, PreloadSolver):
            solver.load_tentative_solutions(
                TentativeSolutions.load(
                    output_dir / "solutions" / f"{problemset.stem}.jsonl"
                )
            )
        result_path = (output_dir / f"{problemset.stem}.jsonl").resolve()

        if result_path.exists():
            if args.overwrite:
                _logger.warning("[Problem set %d] %s (overwritten)", idx, problemset)
            else:
                _logger.info("[Problem set %d] %s (skipped)", idx, problemset)
                continue

        _logger.info("[Problem set %d] %s", idx, problemset)
        resolve_running_environment(problemset, Path("runs") / run_dir_name)
        problems = ProblemSet.fromfile(problemset)

        current_working_directory = Path.cwd().resolve()

        os.chdir(Path("runs") / run_dir_name)

        if args.solve_only:
            result = evaluator.solve_only(problems, solver)
            result.write(result_path)
            _logger.info("[Problem set %d] Solutions written to %s", idx, result_path)
        else:
            result = evaluator.solve_evaluate(problems, solver)
            result.write(result_path)
            _logger.info("[Problem set %d] Score: %.2f", idx, result.score)

        os.chdir(current_working_directory)


def _main():
    parser = argparse.ArgumentParser()
    parser.add_argument("problemset", type=Path, nargs="+")
    parser.add_argument(
        "--model",
        default="gpt-4",
        choices=[
            "gpt-4",
            "gpt-4-32k",
            "gpt-35-turbo",
            "gpt-35-turbo-16k",
            "llama2-70b",
            "llama2-13b",
            "llama2-7b",
            "gemini-pro",
            "codellama-7b",
            "codellama-13b",
            "codellama-34b",
        ],
    )
    parser.add_argument(
        "--endpoint",
        default="aoai",
        choices=["aoai", "aiyyds", "substrate", "azureml", "google", "llamacpp"],
    )
    parser.add_argument(
        "--prompt",
        default="coml",
    )
    parser.add_argument("--overwrite", action="store_true", default=False)
    parser.add_argument("--solve-only", default=False, action="store_true")
    parser.add_argument("--evaluate-from", type=Path, default=None)
    parser.add_argument("--retry", default=None, type=int)
    parser.add_argument("--retry-reset", default=False, action="store_true")
    parser.add_argument("--error-propagation", default=False, action="store_true")
    parser.add_argument("--retry-hint", action="store_true", default=False)
    parser.add_argument("--debug", action="store_true", default=False)

    args = parser.parse_args()

    for problemset in args.problemset:
        _logger.info("Testing: %s", problemset)
        _test_problemset(args, problemset)


if __name__ == "__main__":
    _main()
