from __future__ import annotations

import json
import logging
import re
import textwrap
import traceback
import types
from contextlib import contextmanager
from pathlib import Path
from typing import Any, List, Literal, Optional, TypedDict, cast

import colorama
from langchain.chat_models.base import BaseChatModel
from langchain.schema import AgentAction, AgentFinish, AIMessage, BaseMessage, HumanMessage, SystemMessage

from .problem import ProblemSet
from .simulation import Environment

_logger = logging.getLogger(__name__)

MARKDOWN_CODE_PATTERN = re.compile(r"`{3}([\w]*)\n([\S\s]+?)\n`{3}")


class SolverException(Exception):
    pass


class Solver:
    stats: dict[str, Any] = {}

    def reset(self) -> None:
        pass

    def solve(self, question: str, environment: Environment) -> str:
        raise NotImplementedError()

    def retry(self, error: str, output: Any, hint: Any = None) -> str:
        # Give another chance to solve the previous problem.
        raise NotImplementedError()

    @contextmanager
    def track_stats(self):
        if hasattr(self, "llm"):
            llm: BaseChatModel | None = self.llm  # type: ignore
        else:
            llm = None

        from langchain_community.callbacks import get_openai_callback
        from langchain_community.chat_models import ChatOpenAI

        try:
            from langchain_google_genai import ChatGoogleGenerativeAI

            google_genai_available = True
        except ImportError:
            google_genai_available = False

        if isinstance(llm, ChatOpenAI):
            callback_fn = get_openai_callback
        elif google_genai_available and isinstance(llm, ChatGoogleGenerativeAI):
            from msllm_extensions.callback import get_gemini_callback

            def callback_fn():
                return get_gemini_callback(llm)

        elif hasattr(llm, "tracking_callback"):
            callback_fn = llm.tracking_callback  # type: ignore
        else:
            callback_fn = None

        if callback_fn is not None:
            with callback_fn() as callback:
                yield  # run solve
                self.stats = {
                    "prompt_tokens": callback.prompt_tokens,
                    "completion_tokens": callback.completion_tokens,
                }
        else:
            yield  # do nothing


class DummySolver(Solver):
    def solve(self, question: str, environment: Environment) -> str:
        return (
            "import pandas as pd\n" "import numpy as np\n" "\n" "pd.DataFrame(np.random.uniform(0, 1, size=(300, 300)))"
        )


class PerfectSolver(Solver):
    def __init__(self, problems: ProblemSet | None = None):
        if problems is not None:
            self.memory = {
                problem.question: problem.reference_code
                for problem in problems
                if problem.reference_code and problem.question
            }
        else:
            self.memory = {}

    def load_problems(self, problems: ProblemSet) -> None:
        for problem in problems:
            if problem.reference_code and problem.question:
                self.memory[problem.question] = problem.reference_code

    def solve(self, question: str, environment: Environment) -> str:
        if question in self.memory:
            return self.memory[question]
        return ""


class TentativeSolution(TypedDict):
    question: str
    code: str
    solver_stats: dict[str, Any]


class TentativeSolutions:
    def __init__(self, solutions: list[TentativeSolution]):
        self.solutions = solutions

    def pop_solution(self, question: str) -> TentativeSolution:
        if len(self.solutions) == 0:
            raise ValueError("No more solutions")
        if self.solutions[0]["question"] != question:
            raise ValueError(f"Expected question {question}, got {self.solutions[0]}")
        return self.solutions.pop(0)

    def write(self, path: Path | str) -> None:
        if not isinstance(path, Path):
            path = Path(path)
        with path.open("w") as f:
            for solution in self.solutions:
                f.write(json.dumps(solution) + "\n")

    @classmethod
    def load(cls, path: Path | str) -> "TentativeSolutions":
        if not isinstance(path, Path):
            path = Path(path)
        solutions = []
        with path.open("r") as f:
            for line in f.readlines():
                solutions.append(json.loads(line))
        return cls(solutions)


class PreloadSolver(Solver):
    solutions: TentativeSolutions

    def load_tentative_solutions(self, solutions: TentativeSolutions) -> None:
        self.solutions = solutions

    def solve(self, question: str, environment: Environment) -> str:
        solution = self.solutions.pop_solution(question)
        self.stats = solution["solver_stats"]
        return solution["code"]

    @contextmanager
    def track_stats(self):
        yield  # stats are already tracked in solve()


class GPTSolver(Solver):
    system_message = """You're a data scientist. You're good at writing Python code to do data analysis, visualization, and machine learning. You can leverage the Python libraries such as `pandas`, `sklearn`, `matplotlib`, `seaborn`, and etc. to achieve user's request.

Specifically, the user will present a question and optionally some variables (e.g., pandas DataFrame) they already have. Your task is to write a cell in an iPython notebook that serves the user's request. The cell's output should be exactly what the user has asked for.

Some extra instructions:

- The generated code should be wrapped by ``` before and after it.
- Import necessary libraries at the beginning.
- The output of a cell is the last statement of the code. Do not use `print` to output the result or `return` to return the result.
- Do not overwrite or modify the variables provided by the user, unless the user has explicitly asked for it. For example, if the user has provided a DataFrame `df`, you should not reassign `df`, unless the user asks to modify `df` in-place.
- Please write runnable code directly and do not provide examples.
"""

    def __init__(self, llm: BaseChatModel) -> None:
        self.llm = llm

    @staticmethod
    def _smart_repr(value: Any) -> str:
        import numpy
        import pandas

        if isinstance(value, numpy.ndarray):
            return "numpy.ndarray(shape={})".format(value.shape)
        elif isinstance(value, pandas.DataFrame):
            return "pandas.DataFrame(shape={}, columns={})".format(value.shape, value.columns)
        elif isinstance(value, pandas.Series):
            return "pandas.Series(shape={})".format(value.shape)
        elif isinstance(value, list):
            if len(value) > 30:
                return "[{}, ...]".format(", ".join(GPTSolver._smart_repr(v) for v in value[:30]))
            return "[{}]".format(", ".join(GPTSolver._smart_repr(v) for v in value))
        elif isinstance(value, dict):
            if len(value) > 30:
                return "{{{}, ...}}".format(
                    ", ".join(f"{k}: {GPTSolver._smart_repr(v)}" for k, v in list(value.items())[:30])
                )
            return "{{{}}}".format(", ".join(f"{k}: {GPTSolver._smart_repr(v)}" for k, v in value.items()))
        elif isinstance(value, str):
            return f'"{value}"'
        elif isinstance(value, (bool, int, float)):
            return str(value)
        elif value is None:
            return "None"
        else:
            val = str(value)
            if len(val) > 300:
                val = val[:300] + "..."
            return val

    def solve(self, question: str, environment: Environment) -> str:
        human_message = f"Question: {question}"
        variables = "\n".join(
            [
                f"- {name}: {GPTSolver._smart_repr(value)}"
                for name, value in environment.namespace.items()
                if not isinstance(
                    value,
                    (types.ModuleType, types.FunctionType, types.BuiltinFunctionType),
                )
                and not name.startswith("__")
            ]
        )
        if variables:
            human_message += f"\n\nVariables:\n{variables}"
        messages = [
            SystemMessage(content=self.system_message),
            HumanMessage(content=human_message),
        ]
        for message in messages:
            print(colorama.Fore.BLUE + message.type + ":\n" + message.content + colorama.Fore.RESET)
        response = self.llm(messages)
        match = re.search(r"```.*\n([\s\S]+?)\n```", response.content)
        if match is not None:
            return match.group(1)
        # Give up. Return whole response.
        return response.content


class CoMLSolver(Solver):
    def __init__(
        self,
        llm: BaseChatModel,
        shots_shrinking: bool = False,
        dataframe_format: str = "coml",
        code_history_with_question: bool = False,
        **kwargs,
    ) -> None:
        self.llm = llm

        from coml import CoMLAgent

        self.agent = CoMLAgent(llm, **kwargs)
        self.context = None
        self.prev_code = None
        self.hint = None

        self.shots_shrinking = shots_shrinking
        self.dataframe_format = dataframe_format
        self.code_history_with_question = code_history_with_question

    def reset(self) -> None:
        self.history = []

    def solve(self, question: str, environment: Environment) -> str:
        from coml.prompt_utils import describe_variable, filter_variables

        if not self.history and environment.cells:
            for cell in environment.cells:
                self.history.append(cell.source)

        if self.code_history_with_question:
            codes = self.history
        else:
            codes = [cell.source for cell in environment.cells]

        if not self.shots_shrinking:
            if self.dataframe_format == "comlconcise":
                describe_config = {
                    "pandas_description_config": dict(max_cols=2, max_colwidth=5, max_rows=2),
                    "maximum_list_items": 2,
                }
                dataframe_format = "coml"
            elif self.dataframe_format == "comlverbose":
                describe_config = {
                    "pandas_description_config": dict(max_cols=30, max_colwidth=25, max_rows=10),
                    "maximum_list_items": 30,
                }
                dataframe_format = "coml"
            else:
                describe_config = {}
                assert self.dataframe_format in ["coml", "lida"]
                dataframe_format = cast(Literal["coml", "lida"], self.dataframe_format)

            variables = {
                key: describe_variable(value, **describe_config, dataframe_format=dataframe_format)
                for key, value in filter_variables(environment.namespace).items()
            }
            try:
                self.context = self.agent.generate_code(question, variables, codes)
            except Exception as e:
                self.context = None
                raise SolverException(e)
        else:
            configs = self._shrinking_configs()

            for idx, config in enumerate(configs):
                self.agent.num_examples = config["num_examples"]
                if codes:
                    codes = codes[-max(int(len(codes) * config["num_codes"]), 1) :]
                else:
                    codes = []
                if config["describe_config"] is None:
                    variables = {
                        key: "Description unavailable" for key in filter_variables(environment.namespace).keys()
                    }
                else:
                    variables = {
                        key: describe_variable(value, **config["describe_config"])
                        for key, value in filter_variables(environment.namespace).items()
                    }

                try:
                    self.context = self.agent.generate_code(
                        question,
                        variables,
                        codes,
                    )
                    break
                except ValueError as e:
                    if "Input is too long" not in str(e):
                        raise
                    if idx < len(configs) - 1:
                        _logger.warning("%s. Retrying with: %s", str(e), configs[idx + 1])
                    else:
                        _logger.warning("%s. Trying the last resort.", str(e))
            else:
                raise ValueError("Input is too long")

        self.prev_code = self.context["answer"]
        self.hint = None

        self.history.append(textwrap.indent(question.rstrip(), "# ") + "\n" + self.prev_code)

        return self.prev_code

    def retry(self, error: str, output: Any, hint: Any = None) -> str:
        from coml.prompt_utils import describe_variable

        if output is None:
            output = ""
        else:
            output = describe_variable(output)
        try:
            if hint:
                self.hint = hint
            new_context = self.agent.fix_code(error, output, self.hint, self.context)
        except:
            traceback.print_exc()
            new_context = None
        # It could refuse to fix the code.
        if new_context is None:
            # Try a different hint.
            self.hint = "The output is not expected. Please try a different approach."
        else:
            self.prev_code = new_context["interactions"][-1]["code"]
            self.context = new_context
        return self.prev_code

    def _shrinking_configs(self) -> list[dict]:
        return [
            {
                "num_examples": 1.0,
                "num_codes": 1.0,
                "describe_config": {},
            },
            {
                "num_examples": 1.0,
                "num_codes": 1.0,
                "describe_config": {
                    "pandas_description_config": dict(max_cols=10, max_colwidth=15, max_rows=5),
                    "maximum_list_items": 10,
                },
            },
            {
                "num_examples": 0.8,
                "num_codes": 1.0,
                "describe_config": {
                    "pandas_description_config": dict(max_cols=10, max_colwidth=15, max_rows=4),
                    "maximum_list_items": 5,
                },
            },
            {
                "num_examples": 0.6,
                "num_codes": 0.8,
                "describe_config": {
                    "pandas_description_config": dict(max_cols=8, max_colwidth=12, max_rows=4),
                    "maximum_list_items": 5,
                },
            },
            {
                "num_examples": 0.4,
                "num_codes": 0.6,
                "describe_config": {
                    "pandas_description_config": dict(max_cols=6, max_colwidth=10, max_rows=3),
                    "maximum_list_items": 3,
                },
            },
            {
                "num_examples": 0.2,
                "num_codes": 0.3,
                "describe_config": {
                    "pandas_description_config": dict(max_cols=2, max_colwidth=5, max_rows=2),
                    "maximum_list_items": 2,
                },
            },
            {
                "num_examples": 0.2,
                "num_codes": 0.2,
                "describe_config": None,
            },
        ]


class JupyterAISolver(Solver):
    """Solver inspired by Jupyter AI.

    Reference: https://github.com/jupyterlab/jupyter-ai/blob/976f8b9303d198fb339f7b594d29e4cd879618a4/packages/jupyter-ai-magics/jupyter_ai_magics/magics.py#L528
    """

    def __init__(self, llm: BaseChatModel) -> None:
        self.llm = llm
        self.memory: List[BaseMessage] = []

    def reset(self) -> None:
        self.memory.clear()

    def solve(self, question: str, environment: Environment) -> str:
        if self.memory and environment.last_cell:
            self.memory.append(AIMessage(content=environment.last_cell.source))

        prompt = (
            "{prompt}\n\nProduce output as source code only, " "with no text or explanation before or after it."
        ).format(prompt=question.strip())
        self.memory.append(HumanMessage(content=prompt))
        content = self.llm(self.memory).content
        match = re.search(MARKDOWN_CODE_PATTERN, content)
        if match is not None:
            return match.group(2)
        else:
            # Return the whole response.
            return content


class ChapyterSolver(Solver):
    """Solver with the method in Chapyter.

    https://github.com/chapyter/chapyter/blob/a7c8a4c296cec4dfa03da81c4906bd0c53168bb2/chapyter/programs.py#L49
    """

    def __init__(self, llm: BaseChatModel) -> None:
        self.llm = llm

    def solve(self, question: str, environment: Environment) -> str:
        if environment.cells:
            history_code = self.get_execution_history(environment)
            question = question.strip() + "\n\nHere is my python code so far:\n" + history_code

        messages = [
            SystemMessage(content="You are a helpful and assistant and you are chatting with an python programmer."),
            HumanMessage(
                content="From now on, you are ought to generate only the python code based on the description from the programmer."
            ),
            AIMessage(content="Ok, I will do that. Let's do a practice round."),
            HumanMessage(content="Load the json file called orca.json"),
            AIMessage(content="import json \nwith open('orca.json') as file:\n    data = json.load(file)"),
            HumanMessage(content="That was great, now let's do another one."),
            AIMessage(content="Sounds good."),
            HumanMessage(content=question),
        ]

        return self.clean_response_str(self.llm(messages).content)

    @staticmethod
    def get_execution_history(environment: Environment) -> str:
        def limit_output(output, limit=100):
            """Limit the output to a certain number of words."""
            words = output.split()
            if len(words) > limit:
                return " ".join(words[:limit]) + "..."
            return output

        history_strs = []
        for cell in environment.cells:
            history_str = ""

            if cell.output["execute_result"] is not None:
                output = str(cell.output["execute_result"])
            elif cell.output["error"]:
                output = f'{cell.output["error"]["ename"]}: {cell.output["error"]["evalue"]}'
            elif cell.output["stream_output"]:
                output = cell.output["stream_output"]
            else:
                output = ""

            history_str = history_str + "```\n" + cell.source + "\n```"
            if output:
                history_str += "\nOutput:\n" + limit_output(output.strip())

            history_strs.append(history_str + "\n")
        return "\n".join(history_strs)

    @staticmethod
    def clean_response_str(raw_response_str: str):
        all_code_spans = []
        for match in MARKDOWN_CODE_PATTERN.finditer(raw_response_str):
            all_code_spans.append(match.span(2))

        # TODO: This is a very bold move -- if there is no code inside
        # markdown code block, we will assume that the whole block is code.
        # We need better ways to handle this in the future, e.g., checking
        # whether the first line of the output is valid python code.
        if len(all_code_spans) == 0:
            all_code_spans.append((0, len(raw_response_str)))

        cur_pos = 0
        all_converted_str = []
        for cur_start, cur_end in all_code_spans:
            non_code_str = raw_response_str[cur_pos:cur_start]
            non_code_str = "\n".join(
                [f"# {ele}" for ele in non_code_str.split("\n") if not ele.startswith("```") and ele.strip()]
            )
            code_str = raw_response_str[cur_start:cur_end].strip()
            cur_pos = cur_end
            all_converted_str.extend([non_code_str, code_str])

        last_non_code_str = [
            f"# {ele}" for ele in raw_response_str[cur_pos:].split("\n") if not ele.startswith("```") and ele.strip()
        ]
        if len(last_non_code_str) > 0:
            all_converted_str.append("\n".join(last_non_code_str))

        return "\n".join(all_converted_str)


class CodeInterpreterSolver(Solver):
    """Solver with the method in codeinterpreter-api.

    The original implementation uses langchain tools and agents,
    but we need to interrupt the generated tool configuration.
    So this is actually a re-implementation with lower-level langchain APIs.

    Reference: https://github.com/shroominic/codeinterpreter-api/blob/c8898d0cb63a33f086a97f0059c0cff0561aeb32/src/codeinterpreterapi/session.py#L165
    """

    def __init__(self, llm: BaseChatModel) -> None:
        self.llm = llm

        from codeinterpreterapi import CodeInterpreterSession
        from langchain.agents import OpenAIFunctionsAgent

        session = CodeInterpreterSession(llm)

        self.agent = session._choose_agent()
        assert isinstance(self.agent, OpenAIFunctionsAgent)

        self.memory: List[BaseMessage] = []
        self.last_question: Optional[str] = None
        self.last_call_id: Optional[str] = None

    def reset(self) -> None:
        self.memory.clear()

    @staticmethod
    def get_execution_output(output: Any) -> str:
        if output["stream_output"]:
            result = output["stream_output"]
        elif output["execute_result"] is not None:
            result = str(output["execute_result"])
        elif output["error"] is not None:
            result = f"{output['error']['ename']}: {output['error']['evalue']}"
        else:
            result = "The Assistant did not produce any output."

        if len(result) > 500:
            result = "[...]\n" + result[-500:]
        return result

    def solve(self, question: str, environment: Environment) -> str:
        from langchain.tools import StructuredTool
        from langchain_core.agents import AgentActionMessageLog
        from langchain_core.exceptions import OutputParserException

        variable_names = [
            name
            for name, value in environment.namespace.items()
            if not isinstance(
                value,
                (types.ModuleType, types.FunctionType, types.BuiltinFunctionType),
            )
            and not name.startswith("__")
        ]

        if variable_names:
            question += "\n**The kernel has the following variables: **\n"
            for name in variable_names:
                question += f"[Variable: {name}]\n"

        tool = cast(StructuredTool, self.agent.tools[-1])

        if self.last_question is not None and environment.last_cell is not None:
            last_source = environment.last_cell.source
            last_output = self.get_execution_output(environment.last_cell.output)

            # Fake a last action with ground truth
            last_action = AgentActionMessageLog(
                tool=tool.name,
                tool_input={
                    "code": last_source,
                },
                log="Invoking: `{}` with `{}`\n".format(tool.name, {"code": last_source}),
                message_log=[
                    AIMessage(
                        content="",
                        additional_kwargs={
                            "function_call": {
                                "arguments": json.dumps({"code": last_source}, indent=2),
                                "name": tool.name,
                                **({"id": self.last_call_id} if self.last_call_id else {}),
                            }
                        },
                    )
                ],
            )

            agent_action = self.agent.plan(
                [(last_action, last_output)],
                input=self.last_question,
                chat_history=self.memory,
            )
            if isinstance(agent_action, AgentFinish):
                self.memory.append(AIMessage(content=agent_action.return_values["output"]))
            else:
                _logger.warning("Agent failed to finish with ground truth code: %s", agent_action)
                self.memory.append(
                    AIMessage(
                        content=f"The task can be solved with the following code:\n\n```python\n{last_source}\n```"
                    )
                )

        intermediate_steps = []  # No multi-steps are supported yet.

        self.last_call_id = None

        try:
            agent_action = self.agent.plan(intermediate_steps, input=question, chat_history=self.memory)

            if isinstance(agent_action, AgentActionMessageLog):
                self.last_call_id = agent_action.message_log[-1].additional_kwargs["function_call"].get("id")
        except OutputParserException as e:
            error_message = e.args[0]
            _logger.warning(
                "Failed to parse the output. Retrying with regex parsing: %s",
                error_message,
            )
            match = re.search(r"\{'arguments': (.*), 'name': 'python'(.*?)\}", error_message)
            if match is not None:
                tool_input = {"code": eval(match.group(0))["arguments"]}
                agent_action = AgentAction(
                    tool=tool.name,
                    tool_input=tool_input,
                    log="Failed to parse the output. Attempting to fix the code.",
                )
            else:
                _logger.warning("Failed to parse the output after retry.")
                raise

        self.memory.append(HumanMessage(content=question))
        self.last_question = question
        if isinstance(agent_action, AgentFinish):
            output = agent_action.return_values["output"]
            match = re.search(MARKDOWN_CODE_PATTERN, output)
            if match is not None:
                return match.group(2)
            return output
        elif isinstance(agent_action.tool_input, str):
            return agent_action.tool_input
        elif isinstance(agent_action.tool_input, dict) and "code" in agent_action.tool_input:
            return agent_action.tool_input["code"]
        else:
            return "Invalid code"
