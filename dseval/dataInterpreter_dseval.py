from metagpt.roles.di.data_interpreter import DataInterpreter
from .simulation import Environment
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
    
    # async def async_execute_cell(self, cell, cell_index, execution_count: int | None = None,):
    #     assert self.nb_client.kc is not None

    #     await run_hook(self.nb_client.on_cell_start, cell=cell, cell_index=cell_index)

    #     if cell.cell_type != "code" or not cell.source.strip():
    #         self.nb_client.log.debug("Skipping non-executing cell %s", cell_index)
    #         return cell

    #     if self.nb_client.skip_cells_with_tag in cell.metadata.get("tags", []):
    #         self.nb_client.log.debug("Skipping tagged cell %s", cell_index)
    #         return cell

    #     if self.nb_client.record_timing:  # clear execution metadata prior to execution
    #         cell["metadata"]["execution"] = {}

    #     self.nb_client.log.debug("Executing cell:\n%s", cell.source)

    #     cell_allows_errors = (not self.nb_client.force_raise_errors) and (
    #         self.nb_client.allow_errors or "raises-exception" in cell.metadata.get("tags", [])
    #     )

    #     await run_hook(self.nb_client.on_cell_execute, cell=cell, cell_index=cell_index)
        
    #     await run_hook(self.nb_client.on_cell_complete, cell=cell, cell_index=cell_index)
    #     # We launched a code cell to execute
    #     self.nb_client.code_cells_executed += 1
    #     exec_timeout = self.nb_client._get_timeout(cell)

    #     cell.outputs = []
    #     self.nb_client.clear_before_next_output = False
        

    #     if execution_count:
    #         cell["execution_count"] = execution_count
        
    #     if self.nb_client.coalesce_streams and cell.outputs:
    #         new_outputs = []
    #         streams: dict[str, NotebookNode] = {}
    #         for output in cell.outputs:
    #             if output["output_type"] == "stream":
    #                 if output["name"] in streams:
    #                     streams[output["name"]]["text"] += output["text"]
    #                 else:
    #                     new_outputs.append(output)
    #                     streams[output["name"]] = output
    #             else:
    #                 new_outputs.append(output)

    #         # process \r and \b characters
    #         for output in streams.values():
    #             old = output["text"]
    #             while len(output["text"]) < len(old):
    #                 old = output["text"]
    #                 # Cancel out anything-but-newline followed by backspace
    #                 output["text"] = _RGX_BACKSPACE.sub("", output["text"])
    #             # Replace all carriage returns not followed by newline
    #             output["text"] = _RGX_CARRIAGERETURN.sub("", output["text"])

    #         # We also want to ensure stdout and stderr are always in the same consecutive order,
    #         # because they are asynchronous, so order isn't guaranteed.
    #         for i, output in enumerate(new_outputs):
    #             if output["output_type"] == "stream" and output["name"] == "stderr":
    #                 if (
    #                     len(new_outputs) >= i + 2
    #                     and new_outputs[i + 1]["output_type"] == "stream"
    #                     and new_outputs[i + 1]["name"] == "stdout"
    #                 ):
    #                     stdout = new_outputs.pop(i + 1)
    #                     new_outputs.insert(i, stdout)

    #         cell.outputs = new_outputs

    #     await self.nb_client._check_raise_for_error(cell, cell_index, exec_reply)

    #     self.nb_client.nb["cells"][cell_index] = cell
        
    async def run_cell(self, cell: NotebookNode, cell_index: int) -> Tuple[bool, str]:
        """set timeout for run code.
        returns the success or failure of the cell execution, and an optional error message.
        """
        if not cell.source.strip():
            return False, "No Code"
        code = cell.source
        self.environment.execute(code)
        if self.environment.last_exception is not None:
            return False, self.environment.last_exception
        return True, ""
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

class DataInterpreterForDSEval(DataInterpreter):
    def __init__(self, environment: Environment):
        super().__init__()
        self.environment = environment
        self.execute_code = ExecuteNbCodeForDSEval(environment)
    
