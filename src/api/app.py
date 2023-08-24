from json import loads
from apiflask import APIFlask, Schema
from apiflask.fields import String, Integer, Boolean, List, Field
from linter import Linter
from dummylinter import Dlinter
from flask_cors import CORS

app = APIFlask(__name__, title = "Linter", version = "1.0", docs_ui = "swagger-ui", spec_path = "/openapi.yaml")
cors = CORS(app)
app.debug = True

app.config["SPEC_FORMAT"] = "yaml"
app.config["DESCRIPTION"] = """
This API is trying to give helpful coding advices in Python and hopefully one day in ABAP as well.
"""

#root website
@app.get("/")
def root():
    return 'use "POST /linter"'

#health request
@app.get("/health")
def health():
    """
    Confirms the server is running
    """
    return {"status": "pass", "description": "This API is trying to give helpful coding advices in Python and hopefully one day in ABAP as well."}


#defining schemas
class Request(Schema):
    programmingLanguage = String(
        required = True,
        metadata = {"title": "Programming language", "example": "Python"}
    )
    code = String(
        required = True,
        metadata = {"title": "Code to be reviewed", "example": 'print("Hello World!")'}
    )

class Query(Schema):
    model = String(
        required = True,
        metadata = {"title": "model that is used to generate the response", "example": "gpt-3.5-turbo-16k"}
    )

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
    failReason = String(
        metadata = {"title": "describes the reason no response was generated", "example": "unsupported Language"}
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

#API request
@app.post("/linter")
@app.input(Request, location = "json")
@app.input(Query, location="query")
@app.output(Example_Response)
def lint(json_data, query_data):
    """
    Reviews code sent in body
    """
    
    def send(model):
        linter = Linter(json_data["programmingLanguage"], json_data["code"], model)
        if linter.success:
            return linter.get_lint()
        return loads('{"success": false, "failReason": "internal"}')

    if query_data != {}:
        match query_data["model"]:
            case "gpt-3.5-turbo-16k":
                return send(query_data["model"])
            case "gpt-4":
                return send(query_data["model"])
            case "dummy":
                dummy = Dlinter(json_data["programmingLanguage"], json_data["code"])
                return dummy.get_lint()
            case _:
                return loads('{"success": false, "failReason": "unsupported Language"}')
            
        
    else:
        return loads('{"success": false, "failReason": "bad query"}')
    
    # #dummy
    # if query_data != {}:
    #     if query_data["dummy"]:
    #         dummy = Dlinter(json_data["programmingLanguage"], json_data["code"])
    #         return dummy.get_lint()
    #     else:
    #         return loads('{"success": false}')

    # #API
    # else:
    #     linter = Linter(json_data["programmingLanguage"], json_data["code"])
    #     if linter.success:
    #         return linter.get_lint()
    #     return loads('{"success": false}')
