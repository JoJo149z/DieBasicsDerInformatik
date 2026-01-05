# Die ersten Schritte

Ok, Leute, lehnt euch zurück, schnappt euch einen Kaffee (oder Kuchen), und lasst uns einsteigen.  
Wir quatschen über: Programm vs. Algorithmus, C-Grundlagen, Datentypen, Operatoren und Schleifen.

---

## Algorithmus vs Programm

- **Algorithmus**: Die Schritt-für-Schritt-Anleitung.  
  Beispiel: Kuchen backen.
    1. Mehl holen.
    2. Eier reinschlagen.
    3. Zucker dazu.
    4. Backen, bis lecker.

  Wichtige Aspekte:
    - **Korrektheit**: Erfüllt der Algorithmus seine Anforderungen?\
      D.h.: Gibt der obige Algorithmus wirklich einen Kuchen aus?
    - **Effizienz**: Wie viel Zeit und wie viel Speicherplatz braucht er?
    - **Terminierung**: Hält der Algorithmus immer an?


- **Programm**: Die *Umsetzung* des Algorithmus in einer Sprache, die dein Computer versteht.  
  Wenn der Algorithmus das Rezept ist, ist das Programm die Übersetzung des Algorithms für den Roboter, der den Kuchen wirklich backt.  
  Und wenn du Mist codest, kommt ein verbrannter Brownie raus.

---

## Elementare C-Strukturen

Variablen: Erlauben es, Daten strukturiert zu speichern\
In C haben wir so ’nen Baukasten.  
Hier die Teile, die du dauernd sehen wirst:

```c++
#include <stdio.h>

int main() {
    // Variablen sind kleine Boxen im RAM
    int alter = 42;
    char initial = 'B';
    float pi = 3.14;

    printf("Alter: %d\n", alter);
    printf("Initial: %c\n", initial);
    printf("Pi: %f\n", pi);

    return 0;
}
```

Jede Variable = so ’ne kleine Schublade mit nem Label drauf.\
Und wehe, du versuchst, Zucker in die Eier-Schublade zu kippen. Compiler meckert.

## Datentypen
Definieren die Art der Daten die in der Variable gespeichert wird.

- `int` → ganze Zahlen (z.B. 42, -7, 0)
- `float` → Kommazahlen mit begrenzter Genauigkeit
- `double` → Kommazahlen, aber mehr Bits = mehr Nachkommastellen
- `char` → EIN Zeichen (`'a'`, `'Z'`)
- `void` → nix, nada, null oft rückgabe von Funktionen

Profi-Move: `unsigned` z.b. int → keine negativen Zahlen, aber doppelt so viel Platz nach oben.

## Operatoren
Operatoren sind einfach Mathe-Symbole mit mehr Attitüde:
```c++
int a = 10, b = 3;
// Sonderzeichen:
// \n Newline, Zeilensprung
// \t Tabulator
// \0 EOS - Endezeichen in String
printf("%d\n", a + b);   // Addition → 13
printf("%d\n", a - b);   // Subtraktion → 7
printf("%d\n", a * b);   // Multiplikation → 30
printf("%d\n", a / b);   // Ganzzahl-Division → 3 (kein Komma!)
printf("%d\n", a % b);   // Modulo → Rest = 1
```
Zuweisung:
- `int z;` Initialisierung: setzt den Typ einer Variable
- `z = 8;`Zuweisungsoperator: bedeutet: „z wird der Wert 8 zugewiesen“

Vergleichsoperatoren:
- `==` gleich
- `!=` ungleich
- `<`, `>`, `<=`, `>=` logisch, oder?

Logik-Operatoren:
- `&&` UND
- `||` ODER
- `!` NICHT

## Schleifen
Loops sind wie Kuchen-Essen: immer wiederholen, bis Schluss ist.
### while-Schleife
```c++
int kuchen = 5;

while (kuchen > 0) {
    printf("Nom nom... Kuchen übrig: %d\n", kuchen);
    kuchen--;
}
```
### for-Schleife
```c++
for (int i = 0; i < 3; i++) {
    printf("Backe Kuchen Nummer %d\n", i + 1);
}
```
### do-while-Schleife
```c++
int hunger = 0;

do {
    printf("Iss mindestens EIN Stück Kuchen!\n");
    hunger++;
} while (hunger < 1);
```
## Wrap-up

- **Algorithmus**: Plan (Rezept).
- **Programm**: Umsetzung in C (der Koch-Roboter).
- **Datentypen**: Schubladen für verschiedene Zutaten.
- **Operatoren**: Werkzeuge zum Mixen, Vergleichen, Rechnen.
- **Schleifen**: Dinge wiederholen, bis sie fertig oder kaputt sind.

Programmiere wie beim Kuchen backen: Rezept folgen, Zutaten sortieren, nicht anbrennen lassen.

---
## Aufgabe 02 - Prime Time

Du sollst ein kleines C-Programm schreiben, das testet, ob eine eingegebene Zahl eine **Primzahl** ist.\
Nutze dafür das vorgegebene Gerüst von `solution.c`.\
Zur Erinnerung: Eine Primzahl ist nur durch **1** und **sich selbst** teilbar (z. B. 2, 3, 5, 7, 11, …).

## Anforderungen

1. **Gerüst für die Funktion `isPrime()` ist gegeben**
    -  der Funktion wird eine Zahl `nummer` übergeben
    - Die Funktion soll **`true` zurückgeben, wenn `nummer` eine Primzahl ist**, und **`false` sonst**.

2. **Schleife verwenden**
    - Um zu testen, ob eine Zahl durch eine andere teilbar ist, nutze eine Schleife.
    - Zum Überprüfen der Teilbarkeit verwende den **Modulo-Operator `%`**.  
      Beispiel:
      ```c++
      int rest = 5 % 2; // Ergebnis ist 1, weil 5 durch 2 geteilt Rest 1 ergibt
      ```

3. **Ausgabe ins Terminal**
    - Es müssen **genau zwei Zeilen** ausgegeben werden.
    - Erste Zeile: die Frage, ob die Zahl eine Primzahl ist.  
      Beispiel:
      ```
      Ist 105 eine Primzahl?
      ```
    - Zweite Zeile: entweder nur **"Ja"** oder nur **"Nein"**.  
      Keine zusätzlichen Texte oder Leerzeilen!

4. **Beispiel-Aufruf** (wie im Terminal):
      ```bash
        gcc -std=c11 -Wall -g solution.c -o solution
        ./solution
        Ist 105 eine Primzahl?
        Nein
      ```
---
## Zusammenfassung

- Zahl kommt in `isPrime()`.
- Funktion gibt `true` oder `false` zurück.
- Mit `printf` zwei Zeilen ausgeben:
1. "Ist <zahl> eine Primzahl?"
2. "Ja" **oder** "Nein".
- Keine Extras, kein Bonus-Output, nur das Gewünschte.
