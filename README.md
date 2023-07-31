# ChatGPT ABAP Linter

# Developer Setup

Developer setup for UNIX systems (Windows/WSL, Linux, Mac).

1. Clone this repository
2. Create a file named ***API-Key.env*** in the main directory containing your openai API key in the following format:
    ```
    OPENAI_KEY=<your API key>
    ```
3. Install all required python packages
4. Start the webserver inside the ./Webserver/ folder with `flask run`
5. Send a ***POST*** request to ***http://127.0.0.1:5000/linter*** containing a ***application/json*** body in the following format:
    ```
    {
        "programmingLanguage": "your Programming language",
        "code": "your code"
    }
    ```


# Directory Tree
```
.
├── ABAPExamples/                               - contains example code in ABAP
│   ├── zcl_abap_to_json.clas.abap              - 
│   └── zcl_fs_ref_perf_testing.clas.abap       - 
├── PythonExamples/                             - contains example code in Python
│   ├── example.py                              - used as a few-shot prompt
│   ├── heap.py                                 - 
│   └── main.py                                 - 
├── Webserver/                                  - 
│   └── app.py                                  - contains the flask webserver
├── .gitignore                                  - labels the files ignored by git
├── Layout.json                                 - format for the GPT output
├── LayoutTemplate.json                         - example GPT output
├── README.md                                   - this README
├── architecture.drawio.png                     - picture explaining the architecture 
├── client.json                                 - example of POST request body
├── dummielinter.py                             - just returns some message
├── exampleLint.json                            - used as a few-shot prompt
├── jsonify.py                                  - script to convert code into the correct format for JSON
├── linter.py                                   - called by the flask server, sends requests to the openai API
├── message.py                                  - generates messages in the format used by the openai API
├── prompts.txt                                 - contains different prompts
├── requirements.txt                            - pip requirements
└── test.py                                     - script that directly sends requests to the openai API
```








![](architecture.drawio.png)

...

# Todo

- [x] Python Code für's Prototyping verwenden
- [x] Few-Shot Prompt
- [x] JSON Validierung mit Retry

- [ ] Code Review vs "Linter"
- [ ] Dev Readme
- [ ] OpenAPI Spec erzeugen
- [ ] Dockerisieren des Webservers

## Future

- [ ] Iterative Ausgabe via generators()

## Erledigt

- [x] Random Seed - geht nicht
