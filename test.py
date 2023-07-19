import os
import openai
import json
# import pandas as pd
from dotenv import load_dotenv

load_dotenv("./API-Key.env")

api_key = os.getenv("OPENAI_KEY")
openai.api_key = api_key

promtText = "METHOD if_oo_adt_classrun~main. \n SELECT * FROM /DMO/FLIGHT INTO TABLE @DATA(flights). \n DATA(json_writer) = cl_sxml_string_writer=>create( type = if_sxml=>co_xt_json ). \n CALL TRANSFORMATION id SOURCE flights = flights \n RESULT XML json_writer."

# models = openai.Model.list()
# print(models)

# data =pd.DataFrame(models["data"])
# data.head(20)
# print(data)

response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    max_tokens = 500,
    temperature = 0.3,
    n = 1,
    messages = [
        {"role": "system", "content": "Your name is 'ABAP-Linter' and your purpose is to assist development in the ABAP language."},
        {"role": "user", "content": "Always answer in a systematic scheme. This has to includes the first and last line, a grading from 0 to 10 and a reason for that given grade."},
        {"role": "assistant", "content": 'I will answer prompts in the following format: \n"lineFrom": 25, \n"lineTo": 49, \n"grade": 4, \n"reason": "This function is named "add" although it performs an arithmetic multiplication. Please rename the function."'},
        {"role": "user", "content": promtText}
    ]
)

for choices in response["choices"]:
    print(choices.message.content)
    print("==================")

# print(response.choices[0].message.content)
print(response)