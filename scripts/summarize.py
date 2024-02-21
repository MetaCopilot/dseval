from dseval import ProblemSet
from radon.metrics import h_visit


def get_code_complexity(code: str) -> float:
    import ast

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


def get_problems_metrics(problem_path):
    from pathlib import Path
    import pandas as pd

    difficulties = []
    for path in Path(problem_path).glob("*.py"):
        problem_count = 0
        for problem in ProblemSet.fromfile(path):
            if problem.question and problem.reference_code:
                difficulties.append(
                    {
                        "problemset": path.stem,
                        "index": problem_count,
                        "dseval_complexity": get_code_complexity(
                            problem.reference_code
                        ),
                        **h_visit(problem.reference_code).total._asdict(),
                    }
                )
            problem_count += 1
    difficulties = pd.DataFrame(difficulties)
    return difficulties