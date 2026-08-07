"""Allow the package to run with ``python -m project_name``."""

from project_name.cli import main

raise SystemExit(main())
