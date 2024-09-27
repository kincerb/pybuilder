#!/usr/bin/env python3
"""Simple script to dump the current running python environment."""

import logging
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

file_formatter = logging.Formatter(
    fmt="%(asctime)-14s %(levelname)-8s %(message)s", datefmt="%y%m%d %H:%M"
)
stdout_formatter = logging.Formatter(fmt="%(message)s")
console_handler.setFormatter(stdout_formatter)
logger.addHandler(console_handler)


def main():
    """Entrypoint."""
    environment = {}
    environment.update({"prefix": sys.prefix})
    environment.update({"exec_prefix": sys.exec_prefix})
    environment.update({"base_prefix": sys.base_prefix})
    environment.update({"base_exec_prefix": sys.base_exec_prefix})
    environment.update({"path": sys.path})

    for key, value in environment.items():
        logger.info("%-16s: %s", key, value)


if __name__ == "__main__":
    main()
