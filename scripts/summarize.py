import ast

import pandas as pd

from dseval import Benchmark


def get_code_complexity(code: str) -> float:
    module = ast.parse(code)

    complexity = 0.0
    for node in ast.walk(module):
        # Conditions
        if isinstance(node, (ast.For, ast.While, ast.If, ast.With)):
            complexity += 3
        # Other statements
        elif isinstance(node, ast.stmt):
            complexity += 1
        # Constant, variable
        elif isinstance(node, (ast.Constant, ast.Name)):
            complexity += 0
        # Call other methods
        elif isinstance(node, ast.Call):
            complexity += 3
        # Calling an attribute or a subscript
        elif isinstance(node, (ast.Attribute, ast.Subscript)):
            complexity += 4
        # Other expressions
        elif isinstance(node, ast.expr):
            complexity += 1
        # Function arguments
        elif isinstance(node, ast.arg):
            complexity += 1

    return complexity


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
