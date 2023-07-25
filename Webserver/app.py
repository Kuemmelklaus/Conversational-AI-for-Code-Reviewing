import sys
import os
import time
from apiflask import APIFlask, Schema, abort
from apiflask.fields import String
sys.path.append(os.getcwd() + "/..")
from linter import Linter

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
    linter = Linter(json_data["programmingLanguage"], json_data["code"])
    time.sleep(10)
    return linter.getLint()
