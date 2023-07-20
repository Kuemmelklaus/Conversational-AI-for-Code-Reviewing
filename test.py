import os
import openai
import json
from dotenv import load_dotenv

with open("./ABAPExamples/zcl_abap_to_json.clas.abap", "r") as code: 
    promtText = code.read()

with open("./Layout.json", "r") as l: 
    layout = l.read()

load_dotenv("./API-Key.env")

api_key = os.getenv("OPENAI_KEY")
openai.api_key = api_key

response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    max_tokens = 1000,
    temperature = 0.3,
    n = 1,
    messages = [
        {"role": "system", "content": "Your name is 'ABAP-Linter' and your purpose is to assist development in the ABAP language."},
        {"role": "user", "content": "Always answer in a systematic scheme. This has to includes a grading of a specific section of code from 0 to 10, the first and last line where this graded code is written and a reason for that given grade."},
        {"role": "assistant", "content": 'I will answer prompts using .json in the following format: ' + layout},
        # {"role": "assistant", "content": 'I will answer prompts in the following format: \n"lineFrom": 25, \n"lineTo": 49, \n"grade": 4, \n"reason": "This function is named "add" although it performs an arithmetic multiplication. Please rename the function."'},
        {"role": "user", "content": promtText}
    ]
)

for choices in response["choices"]:
    print(choices.message.content)
    print("===========================")

# print(response.choices[0].message.content)
# print(response)