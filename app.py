import time
import json
from apiflask import APIFlask, Schema
from apiflask.fields import String, Integer, Boolean, List, Field
from linter import Linter

app = APIFlask(__name__, title = "Linter", version = "1.0", docs_ui = "swagger-ui")
app.debug = True

app.config['DESCRIPTION'] = """
This API is trying to give helpful coding advices in Python and hopefully one day in ABAP as well.
"""

@app.get("/")
def root():
    return 'use "POST /linter"'

@app.get("/health")
def health():
    return {"status": "pass", "description": "This API is trying to give helpful coding advices in Python and hopefully one day in ABAP as well."}

class Lin(Schema):
    programmingLanguage = String(
        required = True,
        metadata = {"title": "programming language", "example": "Python"}
    )
    code = String(
        required = True,
        metadata = {"title": "code to be reviewed", "example": 'print("Hello World!")'}
    )

@app.post("/linter")
@app.input(Lin, location = "json")
@app.output({
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
)
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
