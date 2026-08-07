"""Report template placeholders that should be replaced before publication."""

from __future__ import annotations

from pathlib import Path


class PlaceholderChecker:
    """Find known placeholder text in small, version-controlled source files."""

    PLACEHOLDERS = (
        "Project Name",
        "project_name",
        "OWNER",
        "REPOSITORY",
        "YOUR_NAME",
        "FAMILY_NAME",
        "GIVEN_NAME",
        "SECURITY_CONTACT",
    )
    SEARCHABLE_SUFFIXES = {".cff", ".md", ".py", ".toml", ".yaml", ".yml"}
    SKIPPED_DIRECTORIES = {".git", ".venv", "checkpoints", "data", "outputs"}

    def __init__(self, repository_root: Path) -> None:
        self.repository_root = repository_root

    def run(self) -> int:
        """Print matching paths and return the number of files with placeholders."""

        matching_file_count = 0
        for file_path in sorted(self.repository_root.rglob("*")):
            if not self._should_search(file_path):
                continue
            contents = file_path.read_text(encoding="utf-8")
            matches = [placeholder for placeholder in self.PLACEHOLDERS if placeholder in contents]
            if matches:
                relative_path = file_path.relative_to(self.repository_root)
                print(f"{relative_path}: {', '.join(matches)}")
                matching_file_count += 1
        return matching_file_count

    def _should_search(self, file_path: Path) -> bool:
        if not file_path.is_file() or file_path.suffix not in self.SEARCHABLE_SUFFIXES:
            return False
        if file_path.resolve() == Path(__file__).resolve():
            return False
        relative_parts = file_path.relative_to(self.repository_root).parts
        return not any(part in self.SKIPPED_DIRECTORIES for part in relative_parts)


if __name__ == "__main__":
    root_directory = Path(__file__).resolve().parents[1]
    raise SystemExit(1 if PlaceholderChecker(root_directory).run() else 0)
