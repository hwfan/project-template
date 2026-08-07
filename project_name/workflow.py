"""Example stateful workflow used to validate the project scaffold."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class WorkflowResult:
    """Serializable result produced by :class:`ExampleWorkflow`."""

    message: str
    character_count: int

    def as_dict(self) -> dict[str, str | int]:
        """Return a JSON-compatible representation of the result."""

        return {
            "message": self.message,
            "character_count": self.character_count,
        }


class ExampleWorkflow:
    """Run a minimal workflow and persist its result as JSON."""

    def __init__(self, output_directory: Path) -> None:
        self.output_directory = output_directory

    def run(self, message: str) -> Path:
        """Validate ``message`` and atomically write the workflow result."""

        normalized_message = message.strip()
        if not normalized_message:
            raise ValueError("message must contain at least one non-whitespace character")

        workflow_result = WorkflowResult(
            message=normalized_message,
            character_count=len(normalized_message),
        )
        return self._write_result(workflow_result)

    def _write_result(self, workflow_result: WorkflowResult) -> Path:
        self.output_directory.mkdir(parents=True, exist_ok=True)
        output_path = self.output_directory / "result.json"
        temporary_path = output_path.with_suffix(".json.tmp")
        temporary_path.write_text(
            json.dumps(workflow_result.as_dict(), indent=2) + "\n",
            encoding="utf-8",
        )
        temporary_path.replace(output_path)
        return output_path
