#!/usr/bin/env python3
"""Simple script to dump the current running python environment."""

import logging
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

log_formatter = logging.Formatter(
    fmt="%(asctime)-14s %(levelname)-8s %(message)s", datefmt="%y%m%d %H:%M"
)
console_handler.setFormatter(log_formatter)
logger.addHandler(console_handler)


def main():
    """Entrypoint."""
    environment = {}
    environment.update({"base_prefix": sys.base_prefix})
    environment.update({"base_exec_prefix": sys.base_exec_prefix})
    environment.update({"exec_prefix": sys.exec_prefix})
    environment.update({"prefix": sys.prefix})
    environment.update({"path": sys.path})
    environment.update({"platlibdir": sys.platlibdir})
    logger.info("%s", environment)


if __name__ == "__main__":
    main()
