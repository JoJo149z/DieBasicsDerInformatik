import ctypes
import pathlib
import shutil
import subprocess
from pathlib import Path
from typing import Callable

import pytest
import sys

def get_c_compiler() -> str:
    for candidate in ["gcc", "clang"]:
        if shutil.which(candidate):
            return candidate
    raise RuntimeError("No C compiler found")

@pytest.fixture(scope="function")
def shared_lib(tmp_path_factory, request) -> ctypes.CDLL:
    tmpdir = tmp_path_factory.mktemp("shared_lib")

    test_dir = pathlib.Path(request.node.fspath).parent
    c_files = list(test_dir.glob("*.c"))

    if sys.platform.startswith("linux"):
        libname = "solution.so"
    elif sys.platform == "darwin":
        libname = "solution.dylib"
    else:
        raise RuntimeError(f"Unsupported platform: {sys.platform}")

    libpath = tmpdir / libname

    compile_cmd = [
        get_c_compiler(),
        "-fPIC",
        "-shared",
        "-o",
        str(libpath),
    ] + [str(f) for f in c_files]
    subprocess.run(compile_cmd, check=True)

    return ctypes.CDLL(str(libpath))


@pytest.fixture
def tmp_c_compile(tmp_path_factory, request):
    def compile_now() -> pathlib.Path:
        test_dir = pathlib.Path(request.node.fspath).parent
        c_files = list(test_dir.glob("*.c"))

        libpath = tmp_path_factory.mktemp("build") / "solution"

        compile_cmd = [
            get_c_compiler(),
            "-Wall",
            "-o",
            str(libpath),
            *map(str, c_files),
        ]
        subprocess.run(compile_cmd, check=True)

        if not sys.platform.startswith("win"):
            libpath.chmod(libpath.stat().st_mode | 0o111)

        return libpath

    return compile_now
