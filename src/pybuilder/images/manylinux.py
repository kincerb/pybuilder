"""Interface to build AppImages from manylinux docker images."""

import logging

import docker

from docker.models.images import Image

logger = logging.getLogger(name=__name__)


class PythonImage:
    """Object to facilitate building python AppImages."""

    python_version: str
    image: Image | None

    def __init__(self, python_version: str):  # noqa: D107
        self.python_version = python_version
        self._docker = docker.from_env()
        self.image = None
