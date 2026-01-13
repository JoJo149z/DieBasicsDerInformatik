# Guide to Recursion and Libraries in C

> *“Recursion is like looking into two mirrors facing each other—except one of them better stop eventually.”*

Welcome, brave C programmer. Today we’re talking about **recursion** and **libraries**, two concepts that are powerful, elegant, and capable of ruining your day if used incorrectly.

Let’s dive straight in.

---

## 1. Functions: The Beating Heart of C

Functions are everywhere. If C were a body, functions would be the organs. Or maybe the bones. Or both. The metaphor breaks down quickly.

What functions give you:

* **Modularity** – break big problems into smaller ones
* **Readability** – future-you will thank you
* **Reusability** – write once, use everywhere
* **Sanity** – fewer giant `main()` functions

Any function can call any other function.

Including **itself**.

Which brings us to…

---

## 2. Recursion: When a Function Calls Itself (On Purpose)

### What Is Recursion?

Recursion happens when a function calls **itself** to solve a smaller version of the same problem.

This is totally legal in C.

It’s also totally dangerous if you mess it up.

---

### The Two Laws of Recursion

Every recursive function **must** have:

1. **A base case**
   → When to stop recursing
2. **Progress toward the base case**
   → Each call must get “smaller” or “simpler”

Forget either one and your program will:

* Run forever
* Blow the stack
* Make you sad

---

### Bad Recursion (Don’t Do This)

```c
int recursion(int a) {
    return recursion(a + 1);
}
```

What happens?

* No base case
* Infinite recursion
* 💥 Stack overflow

---

### Good Recursion (At Least It Stops)

```c
int recursion(int a) {
    if (a > 41) {        // base case
        return a;
    }
    return recursion(a + 1);  // recursive step
}
```

This one **terminates**, which already makes it better than the previous version.

---

## 3. The Classic Example: Factorial

Mathematically:

```
n! = 1              if n ≤ 1
n! = n · (n−1)!     if n > 1
```

Looks recursive, right? That’s because it is.

---

### Recursive Factorial in C

```c
int fak(int n) {
    if (n <= 1)
        return 1;              // base case
    return n * fak(n - 1);     // recursion
}
```

Key observations:

* `n` gets smaller each time
* Eventually `n == 1`
* Recursion stops
* Program lives another day

---

### Bigger Numbers = Bigger Types

Factorials get **huge** very fast.

```c
long fak(int n) {
    if (n <= 1) return 1;
    return n * fak(n - 1);
}
```

On a 64-bit system:

* `long` range: `−2^63` to `


Guter Fang — du hast recht, **der Bibliotheken-Teil fehlt noch**.
Hier ist der **fehlende Abschnitt**, passend **im Beej-Guide-Stil**, direkt anschlussfähig an den bisherigen Text.

---

## 4. Bibliotheken: Hör auf, alles selbst zu schreiben

> *„Wenn du `printf()` selbst implementierst, bist du entweder sehr mutig oder hast etwas missverstanden.“*

### Was ist eine Bibliothek?

Eine **Bibliothek** ist einfach:

* eine Sammlung von **fertigen Funktionen**
* die jemand anderes schon geschrieben, getestet und debuggt hat
* und die du einfach **benutzen** kannst

C bringt viele davon gleich mit.

Beispiele:

* `stdio.h` → Ein- und Ausgabe (`printf`, `scanf`)
* `string.h` → Strings (`strlen`, `strcmp`)
* `math.h` → Mathe (`sin`, `sqrt`)
* `stdlib.h` → Speicher, Konvertierung, Zufall

---

## 5. Header-Dateien (`.h`): Das Versprechen

Header-Dateien enthalten **keinen Code**, sondern nur **Ankündigungen**.

*„Diese Funktion existiert irgendwo. Vertrau mir.“*

Beispiel:

```c
// fak.h
int fak(int n);
```

Das nennt man einen **Funktionsprototyp**.

Warum das wichtig ist:

* Der Compiler weiß, **wie** die Funktion benutzt wird
* Der Linker findet später, **wo** sie implementiert ist

---

## 6. Modularisierung: C-Dateien trennen (Wie Erwachsene)

### Alles in einer Datei (funktioniert, aber meh)

```c
int fak(int n) {
    if (n <= 1) return 1;
    return n * fak(n - 1);
}

int main(void) {
    return fak(3);
}
```

---

### Sauber getrennt (so macht man’s richtig)

**`fak.h`**

```c
int fak(int n);
```

**`fak.c`**

```c
int fak(int n) {
    if (n <= 1) return 1;
    return n * fak(n - 1);
}
```

**`main.c`**

```c
#include "fak.h"

int main(void) {
    return fak(3);
}
```

Vorteile:

* Übersichtlicher
* Wiederverwendbar
* Besser wartbar
* Größere Programme bleiben beherrschbar

---

## 7. `#include`: Copy & Paste auf Präprozessor-Art

```c
#include <stdio.h>
#include "fak.h"
```

Unterschied:

| Syntax      | Bedeutung                      |
| ----------- | ------------------------------ |
| `<stdio.h>` | Suche im Systempfad            |
| `"fak.h"`   | Suche im aktuellen Verzeichnis |

Der Präprozessor ersetzt das **literally** durch den Inhalt der Datei.
Kein Magie. Nur Text.

---

## 8. Kompilieren & Linken: Zwei (oder mehr) Schritte

### Einzelne Module kompilieren

```bash
clang -c fak.c
clang -c main.c
```

Ergebnis:

* `fak.o`
* `main.o`

---

### Linken zum Programm

```bash
clang -o fak main.o fak.o
```

**Der Linker** verbindet:

* Funktionsaufrufe
* Objektdateien
* Bibliotheken

---

## 9. Externe Bibliotheken benutzen

### Im Code

```c
#include <glib.h>
```

### Beim Kompilieren

```bash
clang -Wall -std=c11 fak.c -lglib
```

* `-lglib` → linke gegen `libglib`
* `-I` → zusätzliche Header-Verzeichnisse
* `-L` → zusätzliche Bibliotheks-Verzeichnisse

---

## 10. Wichtig: Header ≠ Implementierung

**Falsch gedacht:**

> „Header werden kompiliert“

**Richtig:**

* Header enthalten **nur Deklarationen**
* `.c`-Dateien enthalten **Code**
* Nur `.c` → `.o` → ausführbar

---

## 11. Typische Anfängerfehler

* Kein Header für externe Funktionen
* Funktion benutzt, bevor sie deklariert ist
* Header enthält Funktionsdefinitionen
* `main()` rekursiv aufrufen (bitte nicht)
* `#include` vergessen → kryptische Fehler

---

## 12. TL;DR (für die Ungeduldigen)

* **Rekursion** = Funktion ruft sich selbst
* **Abbruchbedingung ist Pflicht**
* **Header (`.h`) sagen, was es gibt**
* **Source (`.c`) implementiert es**
* **Compiler übersetzt**
* **Linker verbindet**
* **Bibliotheken sparen Zeit und Nerven**

---
Alles klar
Hier ist **Aufgabe 1 (Fibonacci)** **im Beej’s-Guide-Stil**, sauber strukturiert, locker erklärt und **als Markdown**, genau wie gewünscht.

---

# Anleitung zu Aufgabe 4: Rekursive Fibonacci-Folge

> *„Fibonacci ist das `Hello World` der Rekursion. Einfach genug, um zu starten – fies genug, um dich später zu ärgern.“*

---

## Überblick


In dieser Aufgabe geht es darum, die **n-te Fibonacci-Zahl rekursiv** zu berechnen –
ohne Schleifen, ohne Tricks, ohne Magie.

Nur du, Rekursion und der Stack.

---

## Die Fibonacci-Folge (Kurzfassung)

Die Fibonacci-Zahlen sind so definiert:

```
Fib(1) = 1
Fib(2) = 1
Fib(n) = Fib(n-1) + Fib(n-2)   für n > 2
```

Die ersten Werte:

```
1, 1, 2, 3, 5, 8, 13, 21, ...
```

Ja, das wächst schnell.
Nein, `int` mag das nicht besonders lange.

---

## Ziel der Aufgabe

Du sollst ein C-Programm schreiben, das:

* eine Zahl **n** vom Benutzer einliest
* **rekursiv** die n-te Fibonacci-Zahl berechnet

---

## Beispielausgabe

```text
> ./solution
Bitte gib eine Nummer ein: 4
Fib(4) = 3
```

```text
> ./solution
Bitte gib eine Nummer ein: 6
Fib(6) = 8
```

---

## Wichtiger Punkt: `input.c` ist eine Bibliothek

Du benutzt **nicht** `scanf()`.

Stattdessen:

```c
int n = lese_int();
```

Warum funktioniert das?

* `input.c` enthält die **Implementierung**
* `input.h` enthält die **Deklaration**
* Beide Dateien werden beim Kompilieren eingebunden
* C weiß dadurch: *„Diese Funktion existiert.“*

Klassisches **Header + Implementierung**-Modell.

---

## Vorgegebene Programmstruktur

Du **musst** diese Struktur verwenden:

```c
#include <stdio.h>
#include <stdlib.h>
#include "input.h" // Hier binden wir die Bibliothek ein

// Schreibe hier die Funktion "int fibonacci"

int main() {
    int n = lese_int();          // Zahl einlesen
    int f = fibonacci(n);        // Fibonacci berechnen
    printf("Fib(%d) = %d\n", n, f);
    return 0;
}
```

Was du hinzufügen darfst:

* **eine** Funktion: `int fibonacci(int n)`

Was du **nicht** darfst:

* Schleifen (`for`, `while`, `do`)
* zusätzliche Ausgaben
* Änderungen am Ausgabeformat

---

## Die rekursive Fibonacci-Funktion

Hier ist die **gedankliche Struktur**, nicht zum Copy-Paste, sondern zum Verstehen:

```c++
int fibonacci(int n) {
    if ( Anker bedingung )
    return fibonacci( irgendwas mit n );
}
```

Warum das funktioniert:

* **Abbruchbedingung**:
* **Fortschritt**: `n` sollte kleiner werden
* **Rekursion**: Funktion ruft sich selbst auf
* **Terminierung garantiert**

Ohne Abbruchbedingung → Stack Overflow

---

## Einschränkungen (Sehr wichtig!)

Da wir den Datentyp `int` verwenden, können nur die Fibonacci-Zahlen bis einschließlich
`Fib(23)` (also 28657) berechnet werden.

---

## Kompilieren (exakt so!)

```bash
gcc -std=c11 -Wall -g solution.c input.c -o solution
```

---
## TL;DR

* Fibonacci **rekursiv**
* **keine Schleifen**
* Eingabe mit `lese_int()`
* `int` reicht nur bis `Fib(23)`
* Header sagen *was*, `.c` sagt *wie*

---
P.S. es gibt auch sehr effiziente implementierungen von der Fibonacci Reihe, schaue nach dem Lösen gerne mal in den Python test rein.