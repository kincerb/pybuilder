"""Constants for the images module."""

from pathlib import Path


class ImageConstants:
    """Manylinux image constants."""

    __slots__ = ()
    MANYLINUX_REPO = "https://quay.io/pypa"
    MANYLINUX_GLIBC_X86_IMAGE = f"{MANYLINUX_REPO}/manylinux_2_28_x86_64"
    MANYLINUX_GLIBC_ARM_IMAGE = f"{MANYLINUX_REPO}/manylinux_2_28_aarch64"
    MANYLINUX_GLIBC_ARM_IMAGE_LEGACY = f"{MANYLINUX_REPO}/manylinux2014_x86_64"
    MANYLINUX_MUSL_X86_IMAGE = f"{MANYLINUX_REPO}/musllinux_1_2_x86_64"
    MANYLINUX_MUSL_ARM_IMAGE = f"{MANYLINUX_REPO}/musllinux_1_2_x86_64"
    INSTALL_DIRECTORY = Path("/opt/python")
