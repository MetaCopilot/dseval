import ast

import pandas as pd

from dseval import Benchmark
from dseval.utils import get_code_complexity


def compute_benchmark_difficulty(benchmark: Benchmark) -> float:
    difficulties = []
    for problemset in benchmark:
        for index, problem in problemset.enumerate():
            difficulties.append(
                {
                    "problemset": problemset.name,
                    "index": index,
                    "dseval_complexity": get_code_complexity(problem.reference_code),
                }
            )
    difficulties = pd.DataFrame(difficulties)
    print(difficulties)
    return difficulties["dseval_complexity"].mean()


def summarize():
    summary = []
    for benchmark in Benchmark.list("benchmarks"):
        difficulty = compute_benchmark_difficulty(benchmark)
        summary.append(
            {
                "Benchmark": benchmark.name,
                "Latest": f"v{benchmark.version}",
                "# Sets": len(benchmark.problemsets),
                "# Problems": sum(problemset.num_complete for problemset in benchmark),
                "Difficulty": difficulty,
            }
        )

    print(pd.DataFrame(summary).to_markdown(index=False, numalign=None, stralign=None, floatfmt=".1f"))


if __name__ == "__main__":
    summarize()
