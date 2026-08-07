#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIRECTORY="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
REPOSITORY_ROOT="$(cd -- "${SCRIPT_DIRECTORY}/../.." && pwd)"
VIRTUAL_ENVIRONMENT_PATH="${REPOSITORY_ROOT}/.venv"

python -m venv "${VIRTUAL_ENVIRONMENT_PATH}"
"${VIRTUAL_ENVIRONMENT_PATH}/bin/python" -m pip install --upgrade pip
"${VIRTUAL_ENVIRONMENT_PATH}/bin/python" -m pip install -e "${REPOSITORY_ROOT}[dev]"

printf 'Installed Project Name in %s\n' "${VIRTUAL_ENVIRONMENT_PATH}"
