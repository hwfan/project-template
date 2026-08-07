# Contributing

Thank you for improving Project Name.

## Before opening a change

1. Discuss substantial API, architecture, dependency, or data-format changes in
   an issue first.
2. Create a focused branch from the default branch.
3. Install the development dependencies with `python -m pip install -e '.[dev]'`.
4. Follow the repository guidance in `AGENTS.md`.

## Verification

Run the checks relevant to your change:

```bash
python -m ruff check .
python -m unittest discover -s tests -v
python -m compileall -q project_name tools
```

For expensive workflows, include a bounded smoke-test command and describe the
full environment that was not exercised locally.

## Pull requests

Keep pull requests small and explain the motivation, implementation, verification,
and compatibility impact. Do not commit generated outputs, datasets, model
weights, credentials, or unrelated formatting changes.
