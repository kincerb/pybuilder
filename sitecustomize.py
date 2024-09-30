"""This module is automatically imported by `site <https://docs.python.org/3/library/site.html#module-site>`_.

This module looks for ``pyvenv.cfg`` a directory above the command given
on the command line.

Due to the nature of AppImages along with virtual environments, without this, attempting
to execute a script inside an environment will not work unless it is activated first.
"""

import os
import sys

from pathlib import Path


def addsites():
    """Insert AppImage venv into `sys.path` if found."""
    try:
        command_directory = Path(os.environ["CMD_GIVEN"]).absolute().parent
    except KeyError:
        return

    venv = command_directory.parent
    if not venv.joinpath("pyvenv.cfg").exists():
        return

    version = f"{sys.version_info.major}.{sys.version_info.minor}"
    venv_site = venv.joinpath("lib", f"python{version}", "site-packages")

    if not venv_site.exists() or str(venv_site) in sys.path:
        return

    sys.path.insert(0, str(venv_site))


addsites()
