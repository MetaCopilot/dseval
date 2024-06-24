from metagpt.roles.di.data_interpreter import DataInterpreter
from .simulation import Environment, CellOutput
from metagpt.actions.di.execute_nb_code import ExecuteNbCode
from nbformat import NotebookNode
import asyncio
import re
from typing import Tuple
from nbclient.util import ensure_async, run_hook, run_sync
from nbclient.exceptions import (
    CellControlSignal,
    CellExecutionComplete,
    CellExecutionError,
    CellTimeoutError,
    DeadKernelError,
)

_RGX_CARRIAGERETURN = re.compile(r".*\r(?=[^\n])")
_RGX_BACKSPACE = re.compile(r"[^\n]\b")

class ExecuteNbCodeForDSEval(ExecuteNbCode):
    def __init__(self, environment: Environment):
        super().__init__()
        self.environment = environment
    
        
    async def run_cell(self, cell: NotebookNode, cell_index: int) -> Tuple[bool, str]:
        """set timeout for run code.
        returns the success or failure of the cell execution, and an optional error message.
        """
        def limit_output(output, limit=100):
            """Limit the output to a certain number of words."""
            words = output.split()
            if len(words) > limit:
                return " ".join(words[:limit]) + "..."
            return output
        if not cell.source.strip():
            return False, "No Code"
        code = cell.source
        output = self.environment.execute(code)
        # return self.parse_outputs(self.environment.cells[-1].output)
        if self.environment.last_exception is not None:
            return False, self.environment.last_exception
        if output is not None:
            return True, limit_output(str(output))
        return True, limit_output(str(self.environment.last_cell.output["stream_output"]))
        # try:
        #     await self.async_execute_cell(cell, cell_index)
        #     return self.parse_outputs(self.nb.cells[-1].outputs)
        # except CellTimeoutError:
        #     assert self.nb_client.km is not None
        #     await self.nb_client.km.interrupt_kernel()
        #     await asyncio.sleep(1)
        #     error_msg = "Cell execution timed out: Execution exceeded the time limit and was stopped; consider optimizing your code for better performance."
        #     return False, error_msg
        # except DeadKernelError:
        #     await self.reset()
        #     return False, "DeadKernelError"
        # except Exception:
        #     return self.parse_outputs(self.nb.cells[-1].outputs)
        
    def parse_outputs(self, outputs: CellOutput, keep_len: int = 2000) -> Tuple[bool, str]:
        """Parses the outputs received from notebook execution."""
        assert isinstance(outputs, CellOutput)
        parsed_output, is_success = [], True
        for i, output in enumerate(outputs):
            output_text = ""
            if output["output_type"] == "stream" and not any(
                tag in output["text"]
                for tag in ["| INFO     | metagpt", "| ERROR    | metagpt", "| WARNING  | metagpt", "DEBUG"]
            ):
                output_text = output["text"]
            elif output["output_type"] == "display_data":
                if "image/png" in output["data"]:
                    self.show_bytes_figure(output["data"]["image/png"], self.interaction)
                else:
                    logger.info(
                        f"{i}th output['data'] from nbclient outputs dont have image/png, continue next output ..."
                    )
            elif output["output_type"] == "execute_result":
                output_text = output["data"]["text/plain"]
            elif output["output_type"] == "error":
                output_text, is_success = "\n".join(output["traceback"]), False

            # handle coroutines that are not executed asynchronously
            if output_text.strip().startswith("<coroutine object"):
                output_text = "Executed code failed, you need use key word 'await' to run a async code."
                is_success = False

            output_text = remove_escape_and_color_codes(output_text)
            # The useful information of the exception is at the end,
            # the useful information of normal output is at the begining.
            output_text = output_text[:keep_len] if is_success else output_text[-keep_len:]

            parsed_output.append(output_text)
        return is_success, ",".join(parsed_output)

class DataInterpreterForDSEval(DataInterpreter):
    def __init__(self, environment: Environment):
        super().__init__()
        self.environment = environment
        self.execute_code = ExecuteNbCodeForDSEval(environment)
    
