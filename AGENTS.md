# Repository Development Guide

These instructions apply to the entire repository unless a more specific
`AGENTS.md` exists in a subdirectory.

## Design priorities

- Prefer readable, maintainable implementations over compact or clever code.
- Make the smallest change that fully solves the requested task.
- Preserve public interfaces, configuration defaults, and existing behavior
  unless a change is explicitly requested.
- Keep third-party code isolated under `third-party/`. Implement
  repository-specific integrations in the first-party package or `tools/`.

## Project structure

- Keep reusable Python code in `project_name/` and rename that package when the
  template is initialized.
- Keep user-facing shell entry points in `scripts/`.
- Put Python workflow implementations and command-line utilities in `tools/`.
- Keep versioned experiment settings in `configs/`.
- Keep small documentation media in `assets/`.
- Never commit datasets, checkpoints, generated outputs, credentials, or secrets.
- Prefer a workflow class for non-trivial stateful processing. Add helper classes
  only when they own a distinct responsibility.

## Python style

- Use Python 3.10 or newer.
- Use descriptive class, method, variable, and argument names.
- Add type hints to public functions and non-trivial internal helpers.
- Add concise docstrings to public classes and methods and to logic with
  important assumptions.
- Use `pathlib.Path` for filesystem-oriented code unless an interface requires
  strings.
- Use private methods for class-internal operations.
- Group imports as standard library, third-party packages, then local modules.
- Raise errors with enough input, path, sample, or record context to diagnose
  failed batch jobs.
- Do not suppress warnings globally; handle expected warnings narrowly.

## Batch and accelerator workflows

- Load heavyweight models once per process and reuse them across samples.
- Process large datasets incrementally instead of retaining them in memory.
- Make long-running commands resumable and safe to rerun.
- Provide bounded sample ranges or limits for smoke tests.
- Release files, temporary resources, and accelerator memory promptly.
- Never log keys, tokens, passwords, or full credential contents.

## Data and artifact handling

- Validate records and paths before expensive computation.
- Document ordering, shapes, dtypes, coordinate systems, and units for serialized
  data.
- Write final artifacts atomically when practical.
- Avoid redundant intermediate copies of large arrays or media.
- Delete temporary artifacts only after their final destination is verified.

## Shell scripts

- Start Bash entry points with `set -euo pipefail`.
- Resolve the repository root relative to the script.
- Quote paths and forward user arguments with `"$@"`.
- Keep shell scripts thin; workflow logic belongs in Python.

## Tests and verification

- Add or update tests for behavior changes.
- Run the smallest relevant unit test, lint, type, syntax, or smoke check.
- Keep expensive GPU tests opt-in and provide a bounded CPU validation path when
  possible.
- Before finishing, review changes for unrelated formatting, debug output,
  generated artifacts, and secrets.

## Pull requests

- Explain the user-visible change and the reason for it.
- List the checks that were run and any checks that were skipped.
- Call out compatibility changes, new dependencies, data-format changes, and
  performance tradeoffs explicitly.
- Keep commits focused and avoid mixing refactors with behavioral changes.
