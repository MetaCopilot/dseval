# DSEval

DSEval is a series of benchmarks aiming at evaluating LLM-powered data science agents.

## Benchmark Summary

This table summarizes the currently-provided benchmarks in this repository.

| Benchmark | Latest | # Sets | # Problems | Difficulty |
|-------------|----------|----------|--------------|--------------|
| Exercise | v1 | 21 | 187 | 17.3 |
| SO | v1 | 202 | 202 | 16.2 |
| LeetCode | v1 | 40 | 40 | 56.0 |
| Kaggle | v1 | 31 | 396 | 35.9 |

## Environment setup

- Create `.env` folder and put `aiyyds.env` and `aoai.env` inside. Add extra services if necessary (requires editing `scripts/test.py`).
- Install necessary dependencies (e.g., `numpy`, `pandas`, `xgboost`, `catboost`, `lightgbm`, `scikit-learn`).
- Install dseval (via: `pip install -e .`).

## Benchmarks

- autoproblems/benchmark_v3
- leetcode/benchmark
- pandasexec
- pycodegpt/benchmark

Please use these paths in the following commands.

## Evaluation

Solving a benchmark (generating code only, with gpt-35-turbo on aiyyds as example). This will generate a folder containing the code snippets:

```bash
python scripts/test.py <benchmark_path> --model gpt-35-turbo --endpoint aiyyds --solve-only
```

Evaluating the generated code snippets:

```bash
python scripts/test.py <benchmark_path> --evaluate-from <solution_folder_just_generated>
```

Both solving and evaluating (not recommended for ease of debugging):

```bash
python scripts/test.py <benchmark_path>
```

**Attention:** Please commit all the running results in `results` folder. Note to check if there are any results overwritten before committing.

## Diagnosis

```bash
flask --app browse run
```

## DSEval Development

Unit test:

```bash
pytest dseval
```
