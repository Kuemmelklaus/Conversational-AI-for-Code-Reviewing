import sys
import os
from apiflask import APIFlask, Schema, abort
from apiflask.fields import String
sys.path.append(os.getcwd() + "/..")
from dummielinter import Linter
#from apiflask.validators import Length, OneOf

app = APIFlask(__name__, title = "Linter", version = "1.0")

@app.get("/")
def root():
    return {"message": 'use "POST /linter"'}

@app.get("/health")
def health():
    return {"message": "Server is running!"}

class Lin(Schema):
    programmingLanguage = String(required = True)
    code = String(required = True)

@app.post("/linter")
@app.input(Lin, location = "json")
def lint(json_data):
    print(json_data["programmingLanguage"])
    linter = Linter(json_data["programmingLanguage"], json_data["code"])
    return linter.getLint()
