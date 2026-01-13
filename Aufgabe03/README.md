# Kontrollstrukturen & Funktionen in C

---

## 1. Syntax vs. Semantik

**Syntax** sagt dir, *was erlaubt ist*.\
**Semantik** sagt dir, *was es bedeutet*.

```c++
// Syntax: korrekt
x = y + 1;

// Semantik: vielleicht völliger Unsinn
```

Ein Programm kann **perfekt kompilieren** und trotzdem **komplett falsch** sein.

---

## 2. Hello World – immer noch unser bester Freund

```c++
#include <stdio.h>

int main(void) {
    printf("Hello World\n");
    return 0;
}
```

Wenn das läuft, hast du:

* einen Compiler
* ein funktionierendes Setup
* einen Fuß in der Tür

Alles Weitere ist Luxus.

---

## 3. Blöcke und Scope (aka: Wer sieht was?)

Ein **Block** ist alles zwischen `{` und `}`.

```c++
{
    int x = 5;
    printf("%d\n", x);
}
```

**Regel:**

* Innen sieht außen
* Außen sieht **nicht** innen

```c++
{
    int n = 20;
}
printf("%d\n", n); // 💥 Compiler ist sauer
```

**Merksatz:** Variablen leben nur dort, wo sie definiert sind.

---

## 4. if – immer mit geschweiften Klammern

Tu dir selbst einen Gefallen:

```c++
if (x < 0) {
    x = -x;
}
```

Auch wenn es *theoretisch* ohne geht:

```c++
if (x < 0)
    x = -x; // tu das nicht
```

C ignoriert Einrückungen. Der Compiler hat keine Augen.

**Best Practice:**

> **Immer** `{}` benutzen. Punkt.

---

## 5. if / else / else if – Entscheidungen treffen

### Einfache Alternative

```c++
if (n == 0) {
    printf("Zero!\n");
} else {
    printf("Not zero!\n");
}
```

### Mehrere Alternativen

```c++
if (n == 1) {
    // thing 1
} else if (n == 2) {
    // thing 2
} else {
    // thing 3
}
```
### Sehr viele Alternativen
```c++
switch(n) {
	case 1: // n == 1
	    printf("n ist eins\n"); 
	    break;
	case 2: // n == 2
	    printf("n ist zwei\n");
	    break;
	case 3:  // n == 3
	    printf("n ist drei\n");
	    break;
	default:  // n != 1,2,3
	    printf("n ist irgendwas\n"); 
	    break;
}
```
Das ist **genau eine** Entscheidungskette. Keine Überraschungen.

---

## 6. Logische Ausdrücke (Boolean-Style, C-Edition)

C hat keinen echten `bool`, sondern:

* `0` → false
* alles andere → true

```c++
if (x != 0 && y > 3) {
    printf("Boom!\n");
}
```

Boolesche Operatoren:

* `==` gleich
* `!=` ungleich
* `< > <= >=` kleiner/größer (gleich)
* `&&` und
* `||` oder

---

## 7. Schleifen – Maschinen lieben Wiederholungen

### while-Schleife

```c++
int i = 0;
while (i < 10) {
    printf("i = %d\n", i);
    i++;
}
```

Läuft **nur**, wenn die Bedingung wahr ist. Vielleicht auch nie.

---

### for-Schleife

```c++
for (int i = 0; i < 10; i++) {
    printf("i = %d\n", i);
}
```

Perfekt, wenn du weißt, **wie oft** du etwas tun willst.

**Faustregel:**

* `for` → Anzahl bekannt
* `while` → Anzahl unklar

---

## 8. i++ vs. ++i (der Klassiker)

```c++
printf("%d\n", i++); // erst ausgeben, dann erhöhen
printf("%d\n", ++i); // erst erhöhen, dann ausgeben
```

Alleinstehend egal.
In Ausdrücken: **sehr wichtig**.

---

## 9. Funktionen – weil Copy & Paste böse ist

### Motivation

Wenn du denselben Code 10× schreibst:

**schlecht …**

Wenn du ihn einmal schreibst und 10× aufrufst:
 
**gut …**

---

### Beispiel: Maximum zweier Zahlen

```c++
int max(int a, int b) {
    if (a > b) {
        return a;
    } else {
        return b;
    }
}
```

Aufruf:

```c++
int m = max(10, 20);
printf("max = %d\n", m);
```

---

## 10. Funktionen = Struktur + Wartbarkeit

Vorteile:

* weniger Code
* weniger Fehler
* Änderungen an **einer** Stelle
* besser testbar

Oder anders gesagt:

> Funktionen retten Leben.

---

## 11. Scope in Funktionen

```c++
int foo(void) {
    int x = 10;
    return x;
}
```

`x` existiert **nur** in `foo`.

Das ist kein Bug. Das ist ein Feature.

---

## 12. Semantik zuerst, Syntax danach

Schlechter Code:

* irgendwie zusammengeschustert
* funktioniert „zufällig“

Guter Code:

1. Überlege dir **was** passieren soll
2. Schreibe es als Pseudocode
3. Übersetze in C

Compiler lieben Syntax.
Menschen lieben Semantik.

---

## 13. Pseudocode – unterschätzte Superkraft

Vorab in mit einfacher syntax Problem lösen, dann implementieren.
```c++
m = 0
p = 1
while p < n:
    print 2^m = p
    m = m + 1
    p = p * 2
```

Kurz. Klar. Verständlich.

Danach ist C nur noch Tipparbeit.

---

## 14. Fazit

* C ist simpel, aber gnadenlos
* Der Compiler ist kein Freund
* Gute Struktur schlägt cleveren Code
* Semantik > Syntax

Und denk dran:

> **Wenn dein Code komisch aussieht, ist er es wahrscheinlich auch.**

---
# Aufgabe 03: ASCII-Rechteck

---

## Ziel der Aufgabe

Schreibe ein **C-Programm**, das ein **Rechteck aus ASCII-Zeichen** im Terminal ausgibt:

* **Innen:** nur der Buchstabe `B`
* **Rand:** ausschließlich der Buchstabe `A`

Das Ergebnis soll **genau** so aussehen:

```
AAAAAAAA
ABBBBBBA
ABBBBBBA
ABBBBBBA
AAAAAAAA
```

Kein Extra-Whitespace. Keine Leerzeilen. Keine kreativen Freiheiten.

---

## Maße des Rechtecks

Das Rechteck besteht aus **zwei Teilen**:

1. einem **inneren Rechteck** aus `B`
2. einem **Rahmen** aus `A`

**Wichtig:**

Die Variablen `breite` und `hoehe` beschreiben **nur das innere Rechteck** aus `B` – **nicht** den Rahmen!

---

## Programmstruktur

Du **musst** diese Grundstruktur verwenden:

```c++
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int breite = 6;
    int hoehe = 3;
    // Hier Code einfügen
}
```

### Regeln dazu:

* `breite` und `hoehe` sind vom Typ `int`
* Die **Werte dürfen nur bei der Deklaration** gesetzt werden
* Keine spätere Zuweisung
* Kein Einlesen von der Tastatur

---

## Anforderungen

Dein Programm ist korrekt, wenn:

* das innere Rechteck **nur aus `B`** besteht
* der Rand **an allen vier Seiten aus `A`** besteht
* sich Breite und Höhe **allein durch Ändern der Variablen** steuern lassen
* **keine zusätzlichen Leerzeilen** ausgegeben werden
* das Programm mit

```bash
   gcc -std=c11 -Wall -g solution.c -o solution
```

  **ohne Warnungen** kompiliert

---

## Denkansatz

Bevor du Code schreibst, überlege dir die **Semantik**:

* Wie viele Zeilen werden insgesamt ausgegeben?
* Wann wird eine komplette Zeile aus `A` gedruckt?
* Wann beginnt und endet der Rand?
* Wo stehen die `B`?

Tipp:

> Meistens läuft es auf **zwei verschachtelte Schleifen** hinaus: eine für die Zeilen, eine für die Spalten.

---

## Beispiel: Ändere nur die Variablen

```c
int breite = 2;
int hoehe = 1;
```

Sollte zu folgendem Output führen:

```
AAAA
ABBA
AAAA
```

Wenn das klappt → Aufgabe verstanden.

---
Du kannst die Tests immer mit
```bash
./test.bash
#oder
./../test.bash
```
ausführen.



