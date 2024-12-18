"""Constants for the config module."""

import platform


class ConfigConstants:
    """Configuration constants."""

    __slots__ = ()
    ARCH = platform.machine()
    LIBC = platform.libc_ver()[0]
