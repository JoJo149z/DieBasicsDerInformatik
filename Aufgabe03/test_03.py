import pathlib
import re
import subprocess

def manipulate_c(breite: int, hoehe: int) -> tuple[int, int]:
    # Ordner des aktuellen Tests
    test_dir = pathlib.Path(__file__).parent
    src_path = test_dir / "solution.c"

    # C-Code lesen
    code_text = src_path.read_text()

    # alte Werte auslesen
    breite_match = re.search(r"int\s+breite\s*=\s*(-?\d+)\s*;", code_text)
    hoehe_match  = re.search(r"int\s+hoehe\s*=\s*(-?\d+)\s*;", code_text)

    old_breite = int(breite_match.group(1)) if breite_match else 0
    old_hoehe  = int(hoehe_match.group(1)) if hoehe_match else 0

    # Variablen ersetzen
    code_text = re.sub(
        r"int\s+breite\s*=\s*-?\d+\s*;",
        f"int breite = {breite};",
        code_text,
    )
    code_text = re.sub(
        r"int\s+hoehe\s*=\s*-?\d+\s*;",
        f"int hoehe = {hoehe};",
        code_text,
    )

    # Datei überschreiben
    src_path.write_text(code_text)

    return old_breite, old_hoehe

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

def test_negativ_size(tmp_c_compile):
    breite = -1
    hoehe = -1
    breite_old, hoehe_old = manipulate_c(breite,hoehe)
    exe_path = tmp_c_compile()
    result = subprocess.run(str(exe_path), capture_output=True, text=True)
    manipulate_c(breite_old,hoehe_old)
    assert result.returncode == 0
    assert result.stdout == py_draw_rect(breite, hoehe)

def test_null_size_hoehe(tmp_c_compile):
    breite = 7
    hoehe = 0
    breite_old, hoehe_old = manipulate_c(breite,hoehe)
    exe_path = tmp_c_compile()
    result = subprocess.run(str(exe_path), capture_output=True, text=True)
    manipulate_c(breite_old,hoehe_old)
    assert result.returncode == 0
    assert result.stdout == py_draw_rect(breite, hoehe)

def test_null_size_breite(tmp_c_compile):
    breite = 0
    hoehe = 7
    breite_old, hoehe_old = manipulate_c(breite,hoehe)
    exe_path = tmp_c_compile()
    result = subprocess.run(str(exe_path), capture_output=True, text=True)
    manipulate_c(breite_old,hoehe_old)
    assert result.returncode == 0
    assert result.stdout == py_draw_rect(breite, hoehe)

def test_normal_size(tmp_c_compile):
    breite = 3
    hoehe = 8
    breite_old, hoehe_old = manipulate_c(breite,hoehe)
    exe_path = tmp_c_compile()
    result = subprocess.run(str(exe_path), capture_output=True, text=True)
    manipulate_c(breite_old,hoehe_old)
    assert result.returncode == 0
    assert result.stdout == py_draw_rect(breite, hoehe)