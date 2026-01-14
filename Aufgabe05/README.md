# Arrays und Adressen

Hör zu, Kumpel, setzen wir uns mal kurz hin und reden über Speicher, Arrays und diesen ganzen Pointer-Wahnsinn. In C ist das alles eigentlich ziemlich logisch, wenn man erst mal kapiert hat, dass der Speicher nichts weiter als eine endlose Reihe von Bytes ist.

### Der Speicher: Ein endloses Band aus Bytes

Stell dir den Arbeitsspeicher wie eine riesige Kette von kleinen Kisten vor. Jede Kiste ist ein Byte groß. Wenn du ein `int` deklarierst, belegt C einfach vier dieser Kisten hintereinander. Eine Variablendeklaration ist im Grunde nur eine Reservierung: „Hey C, ich brauch hier mal Platz!“. Die Zuweisung füllt diesen Platz dann mit einem Wert.

### Arrays: Die Vorratskammer

Wenn du eine ganze Wagenladung gleicher Datentypen hast (wie Primzahlen oder Messwerte), nimmst du ein Array. Ein Array hat eine feste Länge und alle Elemente darin sind vom selben Typ.

Wichtig für dich:

* **Index startet bei Null:** Das erste Element ist immer `a[0]`. Immer.


* **Keine Leitplanken:** C ist es völlig egal, ob du über das Ende des Arrays hinausschreibst. Wenn du `a[10]` abfragst, obwohl dein Array nur 5 Elemente hat, liest du einfach irgendwas aus dem Speicher, was da nicht hingehört. Das ist der Stoff, aus dem Bugs gemacht sind.


* **Speicher-Layout:** Arrays liegen am Stück im Speicher. Bei einem 2D-Array (`matrix[3][2]`) wird das Ganze einfach Zeile für Zeile hintereinander in den Speicher geklatscht.



### Adressen und der magische `&`-Operator

Jede Variable hat einen Ort, an dem sie wohnt – die Adresse. Mit dem `&`-Operator (dem „Adress-of“-Operator) kriegst du raus, wo genau das ist. Während sich der *Wert* einer Variable ändern kann, bleibt ihre *Adresse* immer gleich.

### Pointer: Variablen für Adressen

Ein Pointer ist eine Variable, die nichts anderes tut, als die Adresse einer anderen Variable zu speichern.

* `int *p;` sagt: „`p` ist ein Pointer auf einen Integer“.


* `*p = 10;` bedeutet: „Geh zu der Adresse, die in `p` steht, und pack dort eine 10 rein“.



### Call by Value vs. Call by Reference

Wenn du eine Variable einfach so an eine Funktion übergibst, kriegt die Funktion nur eine **Kopie** (`Call by Value`). Wenn die Funktion den Wert ändert, merkt die `main` davon gar nichts.

Willst du, dass die Funktion das Original ändert, musst du die **Adresse** übergeben (`Call by Reference`). Du gibst der Funktion einen Pointer auf deine Variable, und sie kann dann direkt im Original-Speicher rumwerkeln.

### Der Plot-Twist: Arrays SIND Pointer

Hier kommt der Clou: Der Name eines Arrays ist eigentlich nur ein Pointer auf das allererste Element (`&data[0]`).

* `data[2]` ist exakt dasselbe wie `*(data + 2)`.


* Wenn du ein Array an eine Funktion übergibst, wird **immer** die Adresse übergeben. Ein „Call by Value“ gibt es für Arrays in C nicht.



Also, pass auf deine Indizes auf und behalte deine Pointer im Auge. Wir sehen uns im Debugger!

----
# Aufgabe 05

Hör zu, Kumpel. Du hast hier ein paar Zahlen in einem Array und willst wissen, was da eigentlich abgeht? Wir schreiben uns jetzt die Werkzeuge, um diese Arrays zu durchwühlen.


### 1. Das Array raushauen (`print_array`)

Zuerst wollen wir sehen, was wir überhaupt haben. Du baust eine Funktion, die das Array und seine Länge frisst.

* **Der Plan:** Du rennst mit einer Schleife durch alle Elemente.


* **Wichtig:** Deine Ausgabe muss mit `Array:` anfangen. Pack Kommas zwischen die Zahlen, aber pass auf, dass du nicht über den Rand des Arrays stolperst. C hat keine Leitplanken!



### 2. Die Extremwerte finden (`min` & `max`)

Jetzt suchen wir den kleinsten und den größten Fisch im Teich.

* **Kein Gelaber:** Diese Funktionen benutzen *kein* `printf`. Sie berechnen den Wert und werfen ihn mit `return` zurück.


* **Das Werkzeug:** Benutze exakt dieselbe Parameter-Reihenfolge wie bei `print_array`. In der `main` fängst du die Werte ab und druckst sie mit `Minimum:` bzw. `Maximum:` aus.



### 3. Alles zusammenrechnen (`sum`) – Der Pointer-Trick

Hier wird es interessant. Wir benutzen **Call-by-Reference**.

* **Die Signatur:** Die Funktion kriegt das Array, die Länge und einen **Pointer** auf einen Integer (`int *s`).


* **Die Magie:** Anstatt einen Wert zurückzugeben, geht die Funktion direkt an die Adresse, die der Pointer zeigt, und schreibt die Summe dort rein. In der `main` übergibst du die Adresse deiner Summen-Variable mit dem `&`-Operator.


* **Ausgabe:** Das Ganze startet in der Konsole mit `Summe:`.


### Der Schlachtplan für die Abgabe:

1. **Struktur halten:** Benutze die Vorgabe und ändere die Variablennamen `array` und `len` in der `main` nicht, sonst fliegen die automatischen Tests aus der Kurve.


2. **Sauber bleiben:** Dein Code muss mit `gcc -std=c11 -Wall` ohne Meckern kompilieren.


3. **Formatierung:** Vier Zeilen Ausgabe, keine extra Leerzeilen, nur ganze Zahlen.

Beispiel:
```bash
>gcc -std=c11 -Wall -g solution.c -o solution
> ./solution
Array: 9, 4, 7, 8, 10, 5, 1, 6, 3, 2
Minimum: 1
Maximum: 10
Summe: 55
```

Viel Erfolg. Und denk dran: Zeiger sind deine Freunde, solange du sie nicht ins Nirgendwo zeigen lässt!
