# Hello, World!

Also. Du willst Programmieren lernen.\
Und was macht man als erstes? Richtig: man schreibt ein **Hello World** Programm.
Weil’s einfach ist. Weil’s jeder macht. Weil’s so eine Art Initiationsritual ist.

---
## Das Programm

Hier der Klassiker:
```c++
#include <stdio.h>

int main(void)
{
    printf("Hello, World!\n");
    return 0;
}
```
Speicher das in einer Datei, sagen wir mal hello.c.

---
## Der Programmierablauf

Du schreibst Quellcode → speicherst ihn in hello.c.\
Quellcode ist für Menschen lesbar (naja, für manche und hoffentlich bald dich).

Computer hingegen? Die haben null Bock auf dein printf(). Die sprechen nur Maschinencode (so Nullen und Einsen, sehr langweilig binär).

---
## Kompilierung

Also brauchen wir einen Übersetzer: den Compiler.\
Der Compiler nimmt also dein hello.c und übersetzt es in Maschinencode.\
<details>
<summary>Wenn man es Genau nimmt...</summary>
Um genauer zu sein, übersetzt der Compiler C in Assemblercode danach übernimmt der Assembler und übersetzt Assemblercode in Maschinensprache letztendlich kommt noch der linker zur Nachbearbeitung/Verlinken verschiedener Module.
Bei der Linking stage, werden also vor allem die includes aufgelöst.
Am wichtigsten ist es zu verstehen, dass C als Sprache lesbarer und portabler ist als Maschinencode oder auch als Assembly Code, welcher beides CPU-abhängig ist.

---
</details>

Beispiel mit gcc (GNU Compiler Collection):
```
gcc hello.c -o hello
```
- `hello.c`: dein Quellcode

- `-o hello`: sagt „mach mir eine ausführbare Datei mit dem Namen hello“

Danach hast du eine Datei `hello`. (Ja, auf Windows heißt das dann hello.exe.)

---
## Ausführung

Und dann kommt der magische Moment:
```bash
./hello
```
Bämm. Ausgabe:
```bash
Hello, World!
```
Und du denkst: „Wow, ich habe soeben mit einem Computer kommuniziert.“\
(Okay, eigentlich hast du ihm nur gesagt, er soll was auf den Bildschirm schreiben. Aber hey, Baby-Steps!)

---
## Der Programmablauf

Als du die Binärdatei nun also ausgeführt hast, ist im Groben sowas passiert:
1. Dein Programm startet irgendwo im Betriebssystem.
2. Das Betriebssystem sagt: „Ok, ab in die `main()`-Funktion, viel Spaß.“
3. Dein `printf()`-Aufruf geht los: „Hey, Standard Output, bitte Hello, world! ausspucken!“
4. Der Text taucht auf deinem Bildschirm auf.
5. `main()` gibt 0 zurück → das ist so der Code für „Alles easy“.
6. Das Betriebssystem nickt zufrieden und macht wieder sein Ding.


---
## Aufgabe 01.1
Nun also zu deiner Aufgabe, wenn du alles gut verstanden hast, sollte die ein klax für dich sein.
Schreibe ein C-Programm in `solution.c`, welches auf dem Terminal mittels printf den Text ```Hallo, <Name>!``` ausgibt.\
Wichtig ist zu wissen, dass die Binärdatei, also deine Lösung `solution` heißen muss.\
Auch soll die Ausgabe auf einer separaten Zeile erfolgen bzw. das Terminal erst eine Zeile darunter wieder übernehmen.
Eine beispielhafte Benutzung des Programms liefe wiefolgt ab:
```
> gcc -std=c11 -Wall -g solution.c -o solution
> ./solution
Hallo, Jonas!
```

Gehe sicher, dass Deine Aufgabe dabei die folgenden Bedingungen erfüllt:
- Die Ein- und Ausgabebibliothek `stdio.h` wird korrekt geladen.
- Die Funktion `main` ist definiert.
- `printf` wird zur Ausgabe von Text benutzt.
- **kein** White Space am Anfang oder Ende oder zwischen der **neuen Zeile und !**.

Die Datei sollte ohne Fehler und Warnungen kompilieren beim Aufruf von:
```
gcc -std=c11 -Wall -g solution.c -o solution
```