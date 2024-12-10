"""Interface to build AppImages from manylinux docker images."""

import docker


class PythonImage:
    """Object to facilitate building python AppImages."""

    def __init__(self, python_version: str):  # noqa: D107
        self.python_version = python_version
        self._docker = docker.from_env()
