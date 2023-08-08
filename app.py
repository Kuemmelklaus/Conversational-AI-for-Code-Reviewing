import time
import json
from apiflask import APIFlask, Schema
from apiflask.fields import String, Integer, Boolean, List, Field, Nested, Raw
from linter import Linter

app = APIFlask(__name__, title = "Linter", version = "1.0", docs_ui = "swagger-ui", spec_path = "/openapi.yaml")
app.debug = True

app.config["SPEC_FORMAT"] = "yaml"
app.config["DESCRIPTION"] = """
This API is trying to give helpful coding advices in Python and hopefully one day in ABAP as well.
"""

@app.get("/")
def root():
    return 'use "POST /linter"'

@app.get("/health")
def health():
    """
    Confirms the server is running
    """
    return {"status": "pass", "description": "This API is trying to give helpful coding advices in Python and hopefully one day in ABAP as well."}

class Request(Schema):
    programmingLanguage = String(
        required = True,
        metadata = {"title": "Programming language", "example": "Python"}
    )
    code = String(
        required = True,
        metadata = {"title": "Code to be reviewed", "example": 'print("Hello World!")'}
    )

class Lint1(Schema):
    lineFrom = Integer(
        metadata = {"title": "Starting line", "example": 1}
    )
    lineTo = Integer(
        metadata = {"title": "Ending line", "example": 5}
    )
    message = String(
        metadata = {"title": "Code review", "example": "The 'except' block in the 'submit' function catches all exceptions without specifying which exceptions to catch. It is generally recommended to catch specific exceptions rather than catching all exceptions, as it can make it harder to debug and handle specific errors."}
    )

class Lint2(Schema):
    lineFrom = Integer(
        metadata = {"title": "Starting line", "example": 12}
    )
    lineTo = Integer(
        metadata = {"title": "Ending line", "example": 12}
    )
    message = String(
        metadata = {"title": "Code review", "example": "There is a trailing comma in the list. It is not necessary and can be removed."}
    )

    """{
        lineFrom = Integer(
            metadata = {}
        )
        lineTo = Integer(
            metadata = {}
        )
        message = String(
            metafata = {}
        )
    },
    {
        lineFrom = Integer(
            metadata = {}
        )
        lineTo = Integer(
            metadata = {}
        )
        message = String(
            metafata = {}
        )
    }"""

class Example_Response(Schema):
    code = String(
        metadata = {"title": "Code to be reviewed", "example": 'print("Hello World!")'}
    )
    completion_tokens = Integer(
        metadata = {"title": "Tokens used to create the response", "example": 420}
    )
    date = String(
        metadata = {"title": "Time when the response was created", "example": "2023-08-01T11:30:22.514049"}
    )
    model = String(
        metadata = {"title": "The name of the model which created the response", "example": "gpt-3.5-turbo-16k"}
    )
    programmingLanguage = String(
        metadata = {"title": "Programming language", "example": "Python"}
    )
    success = Boolean(
        required = True,
        metadata = {"title": "Confirms that the response is valid", "example": True}
    )
    total_tokens = Integer(
        metadata = {"title": "Tokens used which contains the request and the response", "example": 2696}
    )
    lint = List(Field,
        metadata = {"title": "Contains the reviews", "example": [{
            "lineFrom": 1,
            "lineTo": 2,
            "message": "The 'except' block in the 'submit' function catches all exceptions without specifying which exceptions to catch. It is generally recommended to catch specific exceptions rather than catching all exceptions, as it can make it harder to debug and handle specific errors."
        },
        {
            "lineFrom": 12,
            "lineTo": 12,
            "message": "There is a trailing comma in the list. It is not necessary and can be removed."
        }
    ]})

#    [{
#        lineFrom = Integer(example = 1),
#        "lineTo": 2,
#        "message": "The 'except' block in the 'submit' function catches all exceptions without specifying which exceptions to catch. It is generally recommended to catch specific exceptions rather than catching all exceptions, as it can make it harder to debug and handle specific errors."
#    },
#    {
#        "lineFrom": 12,
#        "lineTo": 12,
#        "message": "There is a trailing comma in the list. It is not necessary and can be removed."
#    }]

@app.post("/linter")
@app.input(Request, location = "json")
@app.output(Example_Response)
def lint(json_data):
    """
    Reviews code sent in body
    """
    linter = Linter(json_data["programmingLanguage"], json_data["code"])
    i = 0
    while(not linter.done):
        time.sleep(1)
        if(i < 300):
            print("Timemout!")
            return json.loads('{"success": false}')
        i += 1
    return linter.get_lint()


"""@app.output({
    "code": String(example = 'print("Hello World!")'),
    "completion_tokens": Integer(example = 420),
    "date": String(example = "2023-08-01T11:30:22.514049"),
    "model": String(example = "gpt-3.5-turbo-16k"),
    "programmingLanguage": String(example = "Python"),
    "success": Boolean(example = True),
    "total_tokens": Integer(example = 2696),
    "lint": Field(example = [{
        "lineFrom": 1,
        "lineTo": 2,
        "message": "The 'except' block in the 'submit' function catches all exceptions without specifying which exceptions to catch. It is generally recommended to catch specific exceptions rather than catching all exceptions, as it can make it harder to debug and handle specific errors."
    },
    {
        "lineFrom": 12,
        "lineTo": 12,
        "message": "There is a trailing comma in the list. It is not necessary and can be removed."
    }
    ]
    )
}
)"""