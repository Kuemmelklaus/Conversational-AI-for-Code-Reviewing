# Conversational-AI-for-Code-Reviewing

This API is trying to give helpful coding advices in Python and ABAP.

# Developer Setup

Developer setup for UNIX systems (Windows/WSL, Linux, Mac).

1. Clone this repository and install the python and node dependencies
    ```
    pip install -r requirements.txt
    cd src/webapp && npm i
    ```
2. Create a file named ***API-Key.env*** in the project's root directory containing your openai API key in the following format:
    ```
    OPENAI_KEY=<your API key>
    ```
3. The webserver can be started at port 5000 with `./run.sh server`. Optionally, `./run.sh webapp` hosts a webapp at port 3000.  You can check if the server is running by sending a ***GET*** request to ***http://localhost:5000/health***. The webapp can be started using `./run.sh webapp`.
6. Send a ***POST*** request to ***http://localhost:5000/caial?model=gpt-4*** containing a ***application/json*** body in the following format:
    ```
    {
        "programmingLanguage": "your Programming language",
        "code": "your code"
    }
    ```

## Docker Setup

To run the application as a container, the following steps are required in addition to the setup above:
- Build the docker container: `docker build --tag caial .`
- Run the container, mounting the api key file: `docker run -it --network=host -v "$(realpath API-Key.env)":/app/API-Key.env caial`

# Directory Tree
```
.
├── assets/                                     - json, python and ABAP files
├── src/
│   ├── api/                                    - apiflask webserver
│   └── webapp/                                 - react webapp
├── .dockerignore
├── .gitignore
├── Dockerfile                                  - creates a docker image
├── README.md                                   - this README
├── requirements.txt                            - pip requirements
└── run.sh                                      - starts either the api server or the react webapp
```

# Architecture
![](architecture.drawio.png)

# Resources

- [guessinggame.py](https://codereview.stackexchange.com/questions/286118/guessing-game-in-python-which-uses-a-while-loop-with-3-guesses,)
- [example.py](https://www.codingem.com/python-linter/)
- [main.py](https://pythongeeks.org/python-calculator/)
- [heap.py](https://www.geeksforgeeks.org/python-program-for-heap-sort/)
- [ABAP examples/](https://github.com/SAP-samples/abap-oo-basics)

# Next Steps

- implement other AIs not just openai
- catch errors from openai (no connection, tokenlimit exceeded, not enough credit)
- handling multiple files with respect to their directory structure
- integration in IDE