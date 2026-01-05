import math
import random
import subprocess
import shutil
import pathlib
import tempfile
import re
import pytest
import ctypes
import sys

import os, select


def get_compiler() -> str:
    for candidate in ["gcc", "clang", "cc"]:
        if shutil.which(candidate):
            return candidate
    raise RuntimeError("No C compiler found")


@pytest.fixture(scope="module")
def clib(tmp_path_factory):
    tmpdir = tmp_path_factory.mktemp("build")
    src = pathlib.Path(__file__).parent / "solution.c"

    # platform-specific shared library extension
    if sys.platform.startswith("linux"):
        libname = "solution.so"
    elif sys.platform == "darwin":
        libname = "solution.dylib"
    else:
        raise RuntimeError(f"Unsupported platform: {sys.platform}")

    compiler = get_compiler()
    libpath = tmpdir / libname

    compile_cmd = [compiler, "", "-fPIC", "-o", str(libpath), str(src), "-lm"]
    subprocess.run(compile_cmd, check=True)

    lib = ctypes.CDLL(str(libpath))

    return lib

@pytest.fixture(scope="module")
def compile_c_program_factory(tmp_path_factory):
    """
    Returns a function that compiles solution.c with given width and height.
    Usage:
        exe_path = compile_c_program_factory(breite=10, hoehe=5)
    """
    tmpdir = tmp_path_factory.mktemp("build")
    src = pathlib.Path(__file__).parent / "solution.c"

    def _compile(breite: int, hoehe: int) -> str:
        # Read original C file
        with open(src, "r") as f:
            code = f.read()

        # Replace width and height dynamically using regex
        code = re.sub(r"int\s+breite\s*=\s*\d+;", f"int breite = {breite};", code)
        code = re.sub(r"int\s+hoehe\s*=\s*\d+;", f"int hoehe = {hoehe};", code)

        # Write temp C file
        temp_c_file = tmpdir / f"solution_{breite}_{hoehe}.c"
        temp_c_file.write_text(code)

        # Path for the executable
        exe_path = tmpdir / f"solution_exec_{breite}_{hoehe}"

        # Compile
        compiler = get_compiler()
        compile_cmd = [compiler, "-Wall", str(temp_c_file), "-o", str(exe_path)]
        result = subprocess.run(compile_cmd, capture_output=True, text=True)
        if result.returncode != 0:
            pytest.fail(f"Compilation failed:\n{result.stderr}")

        return str(exe_path)

    return _compile


def py_draw_rect(breite: int, hoehe: int) -> str:
    rn = ""
    if breite < 0 or hoehe < 0:
        return rn
    breite = breite+2
    hoehe = hoehe+2
    for y in range(hoehe):
        for x in range(breite):
            if x == 0 or x == breite-1 or y == 0 or y == hoehe-1:
                rn += "A"
            else:
                rn += "B"
        rn += "\n"
    return rn


def test_negativ_size(compile_c_program_factory):
    breite = -1
    hoehe = -1
    exe_path = compile_c_program_factory(breite, hoehe)
    result = subprocess.run([exe_path], capture_output=True, text=True)
    assert result.returncode == 0
    assert result.stdout in py_draw_rect(breite, hoehe)

def test_null_size(compile_c_program_factory):
    breite = 7
    hoehe = 0
    exe_path = compile_c_program_factory(breite, hoehe)
    result = subprocess.run([exe_path], capture_output=True, text=True)
    assert result.returncode == 0
    assert result.stdout in py_draw_rect(breite, hoehe)
    breite = 0
    hoehe = 7
    exe_path = compile_c_program_factory(breite, hoehe)
    result = subprocess.run([exe_path], capture_output=True, text=True)
    assert result.returncode == 0
    assert result.stdout in py_draw_rect(breite, hoehe)

def test_normal_size(compile_c_program_factory):
    breite = 3
    hoehe = 8
    exe_path = compile_c_program_factory(breite, hoehe)
    result = subprocess.run([exe_path], capture_output=True, text=True)
    assert result.returncode == 0
    assert result.stdout in py_draw_rect(breite, hoehe)