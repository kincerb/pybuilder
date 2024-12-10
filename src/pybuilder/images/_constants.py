from pathlib import Path
from urllib.parse import urljoin


class ImageConstants:
    __slots__ = ()
    NWIE_REGISTRY = "https://ntr.nwie.net"
    MANYLINUX_REGISTRY = urljoin(base=NWIE_REGISTRY, url="/quay.io")
    MANYLINUX_GLIBC_X86_IMAGE = urljoin(base=MANYLINUX_REGISTRY, url="/pypa/manylinux_2_28_x86_64")
    MANYLINUX_GLIBC_ARM_IMAGE = urljoin(base=MANYLINUX_REGISTRY, url="/pypa/manylinux_2_28_aarch64")
    MANYLINUX_GLIBC_X86_IMAGE_LEGACY = urljoin(base=MANYLINUX_REGISTRY, url="/pypa/manylinux2014_x86_64")
    MANYLINUX_MUSL_X86_IMAGE = urljoin(base=MANYLINUX_REGISTRY, url="/pypa/musllinux_1_2_x86_64")
    MANYLINUX_MUSL_ARM_IMAGE = urljoin(base=MANYLINUX_REGISTRY, url="/pypa/musllinux_1_2_aarch64")
    INSTALL_DIRECTORY = Path("/opt/python")

constants = ImageConstants()