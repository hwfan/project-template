# Project Name

> One sentence describing what this project does and why it matters.

[![CI](https://github.com/OWNER/REPOSITORY/actions/workflows/ci.yml/badge.svg)](https://github.com/OWNER/REPOSITORY/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)

This repository is a reusable template for Python research and machine-learning
projects. Its layout follows the workflow separation used by Real2Edit2Real:
thin shell entry points live in `scripts/`, Python command-line tools live in
`tools/`, reusable code lives in a package, and large artifacts stay outside
version control.

## Use this template

1. Create a repository from this template on GitHub, or copy the directory.
2. Replace `Project Name`, `OWNER/REPOSITORY`, and the package name
   `project_name` throughout the repository.
3. Update the project metadata in `pyproject.toml` and `CITATION.cff`.
4. Replace the sample workflow, configuration, and tests with project logic.
5. Review `LICENSE`, `CODE_OF_CONDUCT.md`, and `SECURITY.md` before publishing.

To find all placeholders:

```bash
rg 'Project Name|project_name|OWNER|REPOSITORY|YOUR_NAME|FAMILY_NAME|GIVEN_NAME|SECURITY_CONTACT'
```

## Installation

Create an isolated environment and install the package:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e '.[dev]'
```

For automated setup, run:

```bash
bash scripts/installation/install.sh
```

## Quick start

Run the sample workflow:

```bash
bash scripts/run_example.sh --message "hello"
```

The command writes a small JSON artifact under `outputs/example/`. Replace this
sample with the project's real workflow while keeping generated outputs out of
Git.

## Project layout

```text
.
├── .github/          # CI, issue templates, and pull request guidance
├── assets/           # Small, versioned images used in documentation
├── checkpoints/      # Local model weights; ignored except for its README
├── configs/          # Versioned experiment and application configuration
├── data/             # Local datasets; ignored except for its README
├── outputs/          # Generated artifacts; ignored except for its README
├── project_name/     # Reusable Python package
├── scripts/          # Thin user-facing shell entry points
├── tests/            # Automated tests
├── third-party/      # External projects, preferably Git submodules
└── tools/            # Python workflow and maintenance entry points
```

## Development

Run the same checks as CI:

```bash
python -m ruff check .
python -m unittest discover -s tests -v
python -m compileall -q project_name tools
```

Repository-specific development guidance is documented in [AGENTS.md](AGENTS.md).

## Data, checkpoints, and outputs

Do not commit datasets, credentials, model checkpoints, or generated results.
Each artifact directory contains a README describing how to document acquisition
or reproduction. If a small fixture is required for a test, place it under
`tests/fixtures/` and keep its origin and license explicit.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request. Bug reports
and feature requests can be created from the GitHub issue templates.

If this is a research project, update `CITATION.cff` so GitHub can display the
preferred citation automatically.

## License

Licensed under the Apache License 2.0. See [LICENSE](LICENSE).
