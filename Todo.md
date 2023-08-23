[10:35] Stanislaw Hüll

- Cleanup (via Pullrequests):
    - Projekt umbenennen: Conversational AI as Linter (caial)
    - Linter Engine parametrisieren in Webapp und Server (Dummy, gpt-4, gpt-3.5-turbo, gpt-3.5-turbo-16k ...) und Dummy ausgabe erlauben
    - Dateistruktur aufräumen
        - Dateien unter src/linter und src/webapp
        - Persönliche Notizen entfernen
    - README:
        - Dev Setup komprimieren:
            - Virtualenv Setup entfernen (Teil des zu erwartenden Basisverständnis)
            - Verzeichnisbaum:
                - Nicht notwendigerweise jede Datei erwähnen, Ordner sind genug (plus evtl. Kommentar in Dateien)
                - Handelsübliche Dateien (z.B. React Komponenten) nicht beschriften oder als solche kennzeichnen
    - Shellscript zum Starten von Linter Server und Webapp
    - Max Token Size an Engine anpassen
    - Docker:
        - Baseimage Python Version aktualisieren
        - Ein einzelnes Dockerimage für Linter Server und Webapp
    - Architekturdiagramm aktualisieren (oder rausschmeißen)
- Präsentation
    - Termin (mglw. Summer Summit)
- Next Steps (in Doku und Präsentation aufnehmen):
    - (major) Anbindung an fähige Linter
    - (minor) Error Handling (Kontextlänge überschritten, kein Guthaben, Verbindungsfehler, ...)
    - (major) Umgang mit über mehrere Dateien und Verzeichnisse verteilter Codebase
    - (major) Integration in IDEs

