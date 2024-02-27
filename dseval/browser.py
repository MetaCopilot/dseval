from __future__ import annotations

import argparse
from contextvars import ContextVar

from pathlib import Path
from flask import Flask, render_template_string, request

from .loop import EvaluationResult, Verdict

app = Flask(__name__)

result_dir = ContextVar("result_dir")


def available_results(root_dir: Path) -> list[Path]:
    return sorted(root_dir.glob("**/*.jsonl"), reverse=True)


@app.route("/")
def home():
    selected_run = request.args.get("run", None)
    available_runs = available_results(result_dir.get())
    if selected_run is None:
        selected_run = available_runs[0]
    assert selected_run in available_runs

    result = EvaluationResult.read(selected_run).as_dataframe()

    filters = {
        "ALL": len(result),
        "CORRECT": (result["verdict"] == "CORRECT").sum(),
        "INCORRECT": (result["verdict"] != "CORRECT").sum(),
    }

    for verdict, count in result["verdict"].value_counts().to_dict().items():
        if verdict == "CORRECT":
            continue
        filters[verdict] = count

    selected_filter = request.args.get("filter", "ALL")
    if selected_filter == "INCORRECT":
        result = result[result["verdict"] != "CORRECT"]
    elif selected_filter != "ALL":
        result = result[result["verdict"] == selected_filter]

    return render_template_string(
        (Path(__file__).parent / "static" / "index.html").read_text(),
        records=result,
        run=Path(selected_run).as_posix(),
        available_runs=available_runs,
        selected_filter=selected_filter,
        available_filters=filters,
        total=len(result),
        correct=(result["verdict"] == "CORRECT").sum(),
        correct_wo_intact=(result["verdict"].isin(["CORRECT", "INTACT_VIOLATION"])).sum(),
        correct_wo_pe=(result["verdict"].isin(["CORRECT", "PRESENTATION_ERROR"])).sum(),
    )


def _main():
    parser = argparse.ArgumentParser()

    parser.add_argument("result_dir", type=Path)
    parser.add_argument("--debug", action="store_true", default=False)
    parser.add_argument("--port", type=int, default=5000)
    args = parser.parse_args()

    result_dir.set(args.result_dir)

    app.run(debug=args.debug, port=args.port)


if __name__ == "__main__":
    _main()
