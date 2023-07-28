# ChatGPT ABAP Linter

# Developer Setup

Developer setup for UNIX systems (Windows/WSL, Linux, Mac).

1. Clone this repository
2. Create a file named "API-Key.env" containing your openai API key in the following format:
    ```
    OPENAI_KEY=<your API key>
    ```
3. Install all required python packages
4. Start the webserver inside the Webserver/ folder with `flask run`

![](architecture.drawio.png)

...

# Todo

- [x] Python Code für's Prototyping verwenden
- [ ] Few-Shot Prompt
- [x] JSON Validierung mit Retry

- [ ] Code Review vs "Linter"
- [ ] Dev Readme
- [ ] OpenAPI Spec erzeugen
- [ ] Dockerisieren des Webservers

## Future

- [ ] Iterative Ausgabe via generators()

## Erledigt

- [x] Random Seed - geht nicht
