"""This module is automatically imported by `site <https://docs.python.org/3/library/site.html#module-site>`_.

This module looks for ``pyvenv.cfg`` a directory above the command given
on the command line.

Due to the nature of AppImages along with virtual environments, without this, attempting
to execute a script inside an environment will not work unless it is activated first.
"""

import os
import sys

from pathlib import Path


def _search_paths(command: Path) -> Path:
    try:
        app_dir = os.environ["APPDIR"]
    except KeyError:
        raise RuntimeWarning(
            "Env variable 'APPDIR' is not set (for AppImages)"
        ) from None

    for env_path in os.environ["PATH"].split(":"):
        if env_path.startswith(app_dir):
            continue
        candidate = Path(env_path).joinpath(command)
        if candidate.exists():
            return candidate

    raise RuntimeWarning("Command '%s' not in any PATH directories", str(command))


def resolve_command_location(cmd_string: str) -> Path:
    """Attempt to find real location of command given.

    Returns:
        Path object containing full path of command

    Raises:
        `RuntimeWarning` when failed to resolve location
    """
    try:
        command = Path(cmd_string).expanduser()
    except RuntimeError as e:
        raise RuntimeWarning(e) from None

    if command.absolute().exists():
        return command.absolute()

    return _search_paths(command=command)


def get_venv() -> Path:
    """Attempt to find virtual environment.

    Returns:
        Path object to root of venv

    Raises:
        `RuntimeWarning` when no venv could be determined
    """
    try:
        return Path(os.environ["VIRTUAL_ENV"]).expanduser().absolute()
    except KeyError:
        pass

    try:
        command_directory = Path(os.environ["CMD_GIVEN"]).expanduser().absolute().parent
    except KeyError:
        raise RuntimeWarning(
            "Env variable 'CMD_GIVEN' was not found (for AppImages)"
        ) from None

    venv = command_directory.parent
    if not venv.joinpath("pyvenv.cfg").exists():
        raise RuntimeWarning("Possible venv %s had no pyvenv.cfg", str(venv))

    return venv


def addsites():
    """Insert AppImage venv into `sys.path` if found."""
    try:
        venv = get_venv()
    except RuntimeWarning:
        return

    sys.prefix = sys.exec_prefix = str(venv)

    version = f"{sys.version_info.major}.{sys.version_info.minor}"
    venv_site = venv.joinpath("lib", f"python{version}", "site-packages")

    if not venv_site.exists() or str(venv_site) in sys.path:
        return

    sys.path.insert(0, str(venv_site))


addsites()
