import json
from pathlib import Path

from dseval import Benchmark
from dseval.utils import read_jsonl, get_code_complexity


def _main(root_dir: str | Path):
    root_dir = Path(root_dir)
    root_dir.mkdir(exist_ok=True, parents=True)

    benchmark_data = {}
    for benchmark_path in Path("benchmarks").iterdir():
        benchmark = Benchmark.frompath(benchmark_path)
        benchmark_data[benchmark.name] = []
        for problemset in benchmark.problemsets:
            for index, problem in problemset.enumerate(False):
                setup, code = problem.to_dseal()
                benchmark_data[benchmark.name].append({
                    "benchmark": benchmark.name,
                    "problemset": problemset.name,
                    "index": index,
                    "question": problem.question,
                    "setup": setup,
                    "code": code,
                    "difficulty": get_code_complexity(code),
                })

    (root_dir / "benchmarks.json").write_text(json.dumps(benchmark_data))

    result_data = {}
    for result_dir in Path("results").iterdir():
        result_data[result_dir.name] = []
        for result_path in result_dir.iterdir():
            added_result = read_jsonl(result_path)
            for result in added_result:
                result["agent"] = result_path.stem
            result_data[result_dir.name] += added_result

    (root_dir / "results.json").write_text(json.dumps(result_data))


if __name__ == "__main__":
    _main("website/public/data")
