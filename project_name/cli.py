"""Command-line interface for the sample workflow."""

from __future__ import annotations

import argparse
from collections.abc import Sequence
from pathlib import Path

from project_name.workflow import ExampleWorkflow


def build_argument_parser() -> argparse.ArgumentParser:
    """Build the command-line parser without reading process-global state."""

    parser = argparse.ArgumentParser(description="Run the example project workflow.")
    parser.add_argument("--message", default="hello from Project Name")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("outputs/example"),
        help="Directory that receives result.json.",
    )
    return parser


def main(arguments: Sequence[str] | None = None) -> int:
    """Run the command-line workflow and return a process exit code."""

    parsed_arguments = build_argument_parser().parse_args(arguments)
    workflow = ExampleWorkflow(parsed_arguments.output_dir)
    output_path = workflow.run(parsed_arguments.message)
    print(f"Wrote workflow result to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
