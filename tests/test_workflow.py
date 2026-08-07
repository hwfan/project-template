"""Tests for the sample workflow."""

import json
import tempfile
import unittest
from pathlib import Path

from project_name.workflow import ExampleWorkflow


class ExampleWorkflowTest(unittest.TestCase):
    def test_run_writes_normalized_result(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            workflow = ExampleWorkflow(Path(temporary_directory))

            output_path = workflow.run("  hello  ")

            result = json.loads(output_path.read_text(encoding="utf-8"))
            self.assertEqual(result, {"message": "hello", "character_count": 5})

    def test_run_rejects_blank_message(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            workflow = ExampleWorkflow(Path(temporary_directory))

            with self.assertRaisesRegex(ValueError, "message must contain"):
                workflow.run("   ")


if __name__ == "__main__":
    unittest.main()
