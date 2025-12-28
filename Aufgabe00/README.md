# Aufgabe 00

Diese Aufgabe beschäftigt sich mit den Basics von Git.
Für diese Aufgabe würde ich das Nutzen von einem Terminal ohne die Nutzung einer IDE empfehlen.

## ein kleiner Git-Guide

> **Hinweis vorneweg:**  
> Git ist nicht nur ein Tool. Git ist ein Lifestyle. Und zwar einer, bei dem du dich regelmäßig selbst verfluchst, weil du deine Branches verhunzt hast. Aber keine Sorge — wir gehen das zusammen durch.

Git ist ein freies verteiltes Versionsverwaltungssystem und der weltweite Standard für Softwareprojekten.
Also kurz gesagt das Tool, mit dem sich jeder Entwickler wenigstens ein wenig auskennen sollte.

## 1. Dein erstes Repo

Du hast einen Ordner mit Code und willst, dass Git sich drum kümmert.

```console
git init
```

Zack. Jetzt wohnt in .git/ ein kleines Monster, das alles mitbekommt, was du tust. Löschen, umbenennen, um drei Uhr nachts committen — es sieht alles.

## 2. Dateien hinzufügen
```console
git add mein_code.py
git add .
```
`git add .` heißt: „Ich will, dass Git sich an ALLES hier erinnert.“\
Pro-Tipp: Mach das nicht blind. Sonst landet auch deine geheime pw.txt im Repo.
Schreibe dir lieber ein umfangreiches [`.gitignore`](../.gitignore) wie in diesem Repository um die ganzen unnötigen extra files nicht zu adden.

## 3. Committen
```console
git commit -m "Mein erster Commit"
```
Ein Commit ist ein Schnappschuss. Denk an ein Savegame in deinem Lieblingsspiel.\
Und wie beim Savegame: wenn du keins machst, darfst du beim nächsten Crash wieder von vorne anfangen.

## 4. Status-Check
```console
git status
```
Dein bester Freund. Git sagt dir:
- „Hey, diese Datei kenn ich nicht.“
- „Die da wurde geändert.“
- „Alles sauber, ab nach Hause.“

## 5. Branches
Ein Branch ist einfach ein Paralleluniversum deiner Arbeit.
```console
git branch feature-x
git checkout feature-x

# zum Löschen von Branches nutze:
git branch -d feature-x

# zum Auflisten aller Branches nutze:
git branch -a
```
Boom. Jetzt bist du im neuen Universum. Dein Code kann dort alles kaputt machen, ohne dass main was davon merkt.
Perfekt also, falls man mit mehreren Leuten gleichzeitig an einem Projekt arbeitet.\
Pro-Tipp: Der Befehl `git checkout -b feature-x` erzeugt und besucht den Branch sofort.\
Debugging-Tipp: Du kannst auch `git checkout alten_commit` nutzen um einen früheren Projektzustand zu checken.

## 6. Zusammenführen (Merge)
Irgendwann willst du deine Parallelwelt zurück in die Hauptwelt schieben:
```console
git checkout main
git merge feature-x
```
Wenn Git brav ist: alles klappt.\
Wenn Git zickt: Merge-Konflikt. Willkommen in der Hölle. Aber hey, wenigstens bist du nicht allein. Weg aus der Hölle: Versuchen mit IDE zu fixen oder aber Datei für Datei durchgehen wie [hier](https://docs.github.com/de/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-using-the-command-line) beschrieben.

## 7. Remote Repos
Dein Code soll ins Internet?
```console
git remote add origin git@github.com:deinname/deinrepo.git
git push -u origin main
```
Jetzt liegt dein Baby auf GitHub.\
Regel Nummer 1: Push niemals direkt nach main, wenn du nicht sicher bist.\
Regel Nummer 2: Lies Regel Nummer 1 nochmal.

Wobei es in den meisten Fällen sinnvoll ist erst das Repository auf Github oder einem ähnlichen Tool zu erstellen und dieses Repository dann lokal zu klonen.
Dabei kannst du dann auch Online entsprechend Mitglieder deiner Gruppe schon ins Repository hinzufügen.

## 8. Clone
Du willst nicht bei Null anfangen, sondern dir einfach ein bestehendes Repo ziehen?
Willst du den Code aus dem Internet auf deinem Rechner haben, und/oder sollen deine Kollegen aus der Schule am gleichen Projekt mitarbeiten können?
```console
git clone https://github.com/irgendwer/cooles-projekt.git
```
Das ist wie Copy-Paste auf Steroiden: Git holt dir den ganzen Code, alle Branches und die komplette Historie.\
Danach hast du lokal einen Ordner mit allem drin.

## 9. Fork
„Forken“ machst du normalerweise auf GitHub, nicht auf der Kommandozeile.\
Das heißt: du klickst auf Fork und bekommst eine eigene Kopie des Repos unter deinem Account.

Das ist praktisch, wenn du zum Projekt beitragen willst, ohne direkt am Original rumzupfuschen.\
Danach kannst du dein Fork clonen:
```console
git clone https://github.com/deinname/cooles-projekt.git
```
Jetzt bastelst du in deinem Fork, schickst irgendwann einen Pull Request — und hoffst, dass deine Änderungen ins Original wandern.
## 10. Pull vs. Fetch
`git pull` = „Hol alles runter und misch es direkt in meine Arbeit.“

`git fetch` = „Hol alles runter, aber fass meinen Code bloß nicht an.“

## 11. Log
```console
git log --oneline --graph --decorate --all
```
Übersetzt: „Zeig mir den Wahnsinn in bunter ASCII-Grafik.“\
Das ist wie Google Maps für deine Commits. Du wirst es brauchen.

## 12. Letzter aber wichtigster Tipp
Mach Commits, als würdest du Nachrichten an dein zukünftiges Ich schreiben.\
Denn glaub mir: dein zukünftiges Ich wird fluchen, wenn du Messages wie „fix“ oder „update stuff“ liest.

> Merksatz zum Mitnehmen:
> Git vergisst nichts. Aber du schon. Also committe früh, committe oft, und sei nett zu deinem zukünftigen Ich.

## Aufgabe 00.0
Nun versuche einmal einfach den Inhalt von `egal.txt` anzupassen und diesen zu **adden**, zu **committen** und zu **pushen**.
<details>
<summary> deine erste Fehlermeldung</summary>

Hahaha, hast du gerade so eine böse Fehlermeldung gesehen?

<pre><code style="color: red;">
FAILED Aufgabe00/test_00.py::test_branch - AssertionError: Branch 'local-branch' does not exist
FAILED Aufgabe00/test_00.py::test_branch_file - AssertionError: File 'Aufgabe00/test.txt' not found in branch 'local-branch'
</code></pre>

Keine Panik!  
Wenn du alles richtig gemacht hast, dann **solltest** du genau diese Meldung bekommen haben.  
Das heißt: alles läuft wie geplant. 🎉

Du kannst also unbesorgt mit dem nächsten Schritt weitermachen.

</details>

## Aufgabe 00.1

Um das zu beheben, musst du jetzt dein Wissen anwenden:

1. **Checken, wo du bist:**  
   Stelle sicher, dass du im `master` oder `main` Branch bist.
2. **Neuen Branch erstellen:**  
   Erstelle einen neuen Branch namens `local-branch`.
3. **In den neuen Branch wechseln:**  
   Den Branch `local-branch` aus checken.
4. **Datei anlegen und bearbeiten:**  
   Erstelle die Datei `test.txt` im Ordner `Aufgabe00` und ändere sie nach Belieben.
5. **Datei hinzufügen und committen:**  
    Adde und committe also die Datei `test.txt`.\
    Schau dir anschließend das Commit-Log an: `git log`
6. **Zurück zum Hauptbranch:**  
   Wechsel zurück zu master oder main Branch.
7. **Testen:**  
   Um zu prüfen, ob alles geklappt hat, versuche jetzt nochmal zu pushen.

Wenn der Push erfolgreich war, kannst du dich jetzt an die anderen Aufgaben wagen.  
**Jede Aufgabe lebt in ihrem eigenen Ordner** – praktisch, um nichts kaputtzumachen.

Mein Tipp: geh die Aufgaben der Reihe nach durch.  
Die Reihenfolge hat nämlich schon ihren Sinn, sonst wird es schnell chaotisch und frustrierend.

