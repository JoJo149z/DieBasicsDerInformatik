import ctypes
import pathlib
import random
import re
import subprocess


def manipulate_c(array:list[int]) -> list[int]:
    # Ordner des aktuellen Tests
    test_dir = pathlib.Path(__file__).parent
    src_path = test_dir / "solution.c"

    # C-Code lesen
    code_text = src_path.read_text()

    # alte Werte auslesen
    match = re.search(r"int\s+array\s*\[\s*]\s*=\s*\{([^}]*)}\s*;", code_text)

    if match:
        old_array = [int(x.strip()) for x in match.group(1).split(",")]
    else:
        old_array = []

    # Variablen ersetzen
    code_text = re.sub(
        r"int\s+array\s*\[\s*]\s*=\s*\{[^}]*}\s*;",
        f"int array[] = {{{', '.join(map(str, array))}}};",
        code_text
    )
    code_text = re.sub(
        r"int\s+len\s*=\s*-?\d+\s*;",
        f"int len = {len(array)};",
        code_text,
    )

    # Datei überschreiben
    src_path.write_text(code_text)

    return old_array

def py_print_array(array: list[int]) -> str:
    return (
        f"Array: {', '.join(map(str, array))}\n"
        f"Minimum: {min(array)}\n"
        f"Maximum: {max(array)}\n"
        f"Sum: {sum(array)}\n"
    )


def test_100_arrays(tmp_c_compile):
    for _ in range(100):
        array = [random.randint(-1000, -1) for _ in range(random.randint(1, 20))]
        old_array = manipulate_c(array)
        exe_path = tmp_c_compile
        result = (subprocess.run(str(exe_path), capture_output=True, text=True))
        manipulate_c(old_array)
        assert result.returncode == 0
        assert result.stdout == py_print_array(array)