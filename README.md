# Aufgabenstellung BinaryCounter
Versionen in C++ und Python

## Vorbereitung github
- logge dich auf deinem Github-Account ein
- navigiere zu https://github.com/eneukirchner/BinaryCounter
- erstelle einen Fork dieses Projekts in deinem Github-Account
- Im Terminal deines Raspberrys: ```git clone git@github.com:hierDeinGithubUsername/BinaryCounter.git```

## Programmierung
Auf Basis des existierenden Code-Gerüstes soll ein Modulo-16-Zähler programmiert werden, der den Zählerstand im grafischen
Widget und über die LEDs am Zusatzboard anzeigt.

Spezifikationen:
- Druck auf Taster GPIO17: erhöhe Zählerstand um 1
- Druck auf Taster GPIO22: erniedrige Zählerstand um 1
- Druck auf Taster GPIO27: Zählerstand auf 0 zurücksetzen
- Der Zählvorgang wird durch die fallende Flanke beim Drücken des Tasters ausgelöst. Längeres Drücken löst keinen weiteren Zählvorgang aus.
- Der Zähler soll von 0 bis 15 zählen. Auf den Höchstwert 15 folgt wieder 0. Beim Abwärtszählen folgt auf 0 der Wert 15.
- Anzeige des Zählerstandes im Widget durch QLCDNumber dezimal.
- Anzeige des Zählerstandes am Zusatzboard: dual über die 4 LEDs (GPIO18 = MSB, GPIO25 = LSB). Umrechnung dezimal-dual bitte *nicht* mit 
mehrfach-if-Bedingungen, sondern mittels geeignetem Algorithmus.
- Ein funktionsfähiges Beispielprogramm ist unter ```bin/BinaryCounter``` zu finden.

## Abgabe
Hochladen auf github:
```
git add .
git commit -m "Abgabe"
git push origin main
```



