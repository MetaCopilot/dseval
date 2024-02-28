from __future__ import annotations

import argparse
from contextvars import ContextVar

from pathlib import Path
from flask import Flask, render_template, request

from .loop import EvaluationResult

app = Flask(
    __name__, static_folder=Path(__file__).parent / "static", template_folder=Path(__file__).parent / "templates"
)

result_dir = ContextVar("result_dir")


def available_results(root_dir: Path) -> list[Path]:
    return sorted(root_dir.glob("**/*.jsonl"), reverse=True)


@app.route("/")
def home():
    selected_run = request.args.get("run", None)
    available_runs = available_results(app.config["result_dir"])
    if selected_run is None:
        selected_run = available_runs[0]
    else:
        for run in available_runs:
            if str(run).lower() == selected_run.lower():
                selected_run = run
                break
        else:
            raise FileNotFoundError(f"Run {selected_run} not found")

    result = EvaluationResult.read(selected_run).as_dataframe()

    filters = {
        "All": len(result),
        "Correct": (result["verdict"] == "Correct").sum(),
        "Incorrect": (result["verdict"] != "Correct").sum(),
    }

    for verdict, count in result["verdict"].value_counts().to_dict().items():
        if verdict == "Correct":
            continue
        filters[verdict] = count

    selected_filter = request.args.get("filter", "All")
    if selected_filter == "Incorrect":
        result = result[result["verdict"] != "Correct"]
    elif selected_filter != "All":
        result = result[result["verdict"] == selected_filter]

    return render_template(
        "index.html",
        records=result.to_dict(orient="records"),
        run=Path(selected_run).as_posix(),
        available_runs=available_runs,
        selected_filter=selected_filter,
        available_filters=filters,
        total=len(result),
        correct=(result["verdict"] == "Correct").sum(),
        correct_wo_intact=(result["verdict"].isin(["Correct", "IntactViolation"])).sum(),
        correct_wo_pe=(result["verdict"].isin(["Correct", "PresentationError"])).sum(),
    )


def _main():
    parser = argparse.ArgumentParser()

    parser.add_argument("result_dir", type=Path)
    parser.add_argument("--debug", action="store_true", default=False)
    parser.add_argument("--port", type=int, default=5000)
    args = parser.parse_args()

    app.config.update(result_dir=args.result_dir)

    app.run(debug=args.debug, port=args.port)


if __name__ == "__main__":
    _main()
