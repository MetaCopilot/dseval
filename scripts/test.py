import argparse
import logging
from datetime import datetime
from pathlib import Path

from langchain.chat_models.base import BaseChatModel
from langchain_openai import ChatOpenAI

import dotenv
from dseval import Evaluator, Benchmark
from dseval.agent import (
    CoMLAgent,
    ChapyterAgent,
    JupyterAIAgent,
    CodeInterpreterAgent,
)
from dseval.loop import resumable_benchmark_evaluation_loop


_logger = logging.getLogger("dseval")


def configure_llm(model: str, endpoint: str):
    if endpoint == "aoai":
        from msllm_extensions import AzureChatOpenAIWithTooling

        return AzureChatOpenAIWithTooling(
            temperature=0.0,
            azure_deployment=model,
            api_version="2023-12-01-preview",
            max_retries=30,
        )
    elif endpoint in ("openai", "aiyyds"):
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
        return ChatGoogleGenerativeAI(model=model, temperature=0.0)
    elif endpoint == "llamacpp":
        from msllm_extension import LlamaCppClient

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


def configure_agent(model: str, agent: str, llm: BaseChatModel, debug: bool):
    if agent == "coml":
        return CoMLAgent(llm)
    elif agent == "chapyter":
        return ChapyterAgent(llm)
    elif agent == "jupyterai":
        return JupyterAIAgent(llm)
    elif agent == "codeinterpreterapi":
        return CodeInterpreterAgent(llm)
    else:
        raise ValueError(f"Unknown agent: {agent}")


def _evaluate_benchmark(args: argparse.Namespace, benchmark_path: Path):
    # Configure the agent
    llm = configure_llm(args.model, args.endpoint)
    agent = configure_agent(args.model, args.agent, llm, args.debug)

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
    evaluator = Evaluator(**evaluator_kwargs)

    benchmark = Benchmark.frompath(benchmark_path)
    # Guessing the output file
    output_path = (
        (
            Path("results")
            / (benchmark.name if benchmark.name else "unknown")
            / (datetime.now().strftime("%y%m%d") + "-" + args.agent + "-" + args.model + "-" + args.endpoint + ".jsonl")
        )
        .resolve()
        .relative_to(Path(".").resolve())
    )
    _logger.info("Output path: %s", output_path)

    resumable_benchmark_evaluation_loop(benchmark, agent, evaluator, Path("runs") / output_path.stem, output_path)


def _main():
    parser = argparse.ArgumentParser()
    parser.add_argument("benchmark", type=Path, nargs="+")
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
        choices=["aoai", "openai", "aiyyds", "substrate", "azureml", "google", "llamacpp"],
    )
    parser.add_argument("--agent", default="coml", choices=["coml", "chapyter", "jupyterai", "codeinterpreterapi"])
    parser.add_argument("--overwrite", action="store_true", default=False)
    parser.add_argument("--solve-only", default=False, action="store_true")
    parser.add_argument("--evaluate-from", type=Path, default=None)
    parser.add_argument("--retry", default=None, type=int)
    parser.add_argument("--retry-reset", default=False, action="store_true")
    parser.add_argument("--error-propagation", default=False, action="store_true")
    parser.add_argument("--retry-hint", action="store_true", default=False)
    parser.add_argument("--debug", action="store_true", default=False)

    args = parser.parse_args()

    dotenv.load_dotenv()

    for benchmark in args.benchmark:
        _logger.info("Testing: %s", benchmark)
        _evaluate_benchmark(args, benchmark)


if __name__ == "__main__":
    _main()
