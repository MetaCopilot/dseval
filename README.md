# DSEval

DSEval is a series of benchmarks aiming at evaluating LLM-powered data science agents.

In this repository, we provide both the toolkit to support the benchmarking, as well as the data used for benchmarks.

## Benchmark Toolkit

DSEval (as a Python package) provides the necessary infrastructure needed for reliable evaluation of data science agents. It has some integrations of popular data science agents inside.

It **DOES NOT** contain any benchmark data or benchmarking results.

### Installation Option 1

Recommended. Note that in this case, the version installed might not be latest.

```
pip install dseval
```

Use `pip install dseval[agent]` to automatically install all the dependant agents.

### Installation Option 2

Install from source code.

```
git clone https://github.com/MetaCopilot/dseval
cd dseval
pip install -e .
```

## Benchmark Data

This table summarizes the currently-provided benchmarks in this repository.

| Benchmark | Latest | # Sets | # Problems | Difficulty |
|-------------|----------|----------|--------------|--------------|
| Exercise | v1 | 21 | 187 | 17.3 |
| SO | v1 | 202 | 202 | 16.2 |
| LeetCode | v1 | 40 | 40 | 56.0 |
| Kaggle | v1 | 31 | 396 | 35.9 |

### Evaluating Existing Agent on Existing Benchmarks

1. Install the **toolkit** following the guide above.
2. Clone `dseval` repository if you haven't done so.
3. Use `python scripts/test.py <path_to_benchmark>` to test a benchmark. You can select agent frameworks, LLMs, endpoints and evaluation configurations.

For example:

```
python scripts/test.py benchmarks/leetcode --model gpt-35-turbo --endpoint aoai
```

**TODO:** Guide for properly setup reproducible environment for evaluation.

### Diagnosis

TODO

### Contributing New Problems

TODO

### Developing New Benchmarks

TODO

### Integrating New Agents

TODO

## Citation

The repository is founded upon the idea proposed in [this paper](https://arxiv.org/abs/2402.17168). If you find it useful in your research, please consider citing it:

```bibtex
@misc{zhang2024benchmarking,
    title={Benchmarking Data Science Agents}, 
    author={Yuge Zhang and Qiyang Jiang and Xingyu Han and Nan Chen and Yuqing Yang and Kan Ren},
    year={2024},
    eprint={2402.17168},
    archivePrefix={arXiv},
    primaryClass={cs.AI}
}
```
