import os
import openai
import datetime
import json
from dotenv import load_dotenv

m = "gpt-3.5-turbo"

#with open("./ABAPExamples/zcl_abap_to_json.clas.abap", "r") as c:
#    promtText = c.read()

with open("./ABAPExamples/zcl_fs_ref_perf_testing.clas.abap", "r") as c:
    promtText = c.read()

with open("./Layout.json", "r") as l:
    layout = l.read()

load_dotenv("./API-Key.env")

api_key = os.getenv("OPENAI_KEY")
openai.api_key = api_key

response = openai.ChatCompletion.create(
    model = m,
    max_tokens = 2000,
    temperature = 0.2,
    n = 1,
    messages = [
        {"role": "system", "content": "Your name is 'ABAP-Linter' and your purpose is to assist development in the ABAP language."},
        {"role": "user", "content": "Always answer in a systematic scheme. This has to includes a rating of a specific section of code from 0 to 10, the first and last line where this rated code is written and a reason for that given rating (watch out for empty lines). For example if some old fashioned method is used, make a suggestion how to replace this method. Please dont rate any empty lines."},
        {"role": "assistant", "content": "I will answer prompts using .json in the following format: " + layout},
        {"role": "user", "content": promtText}
    ]
)

for choices in response["choices"]:
    try:
        lint = json.loads(choices.message.content)
        lint["date"] = datetime.datetime.now().isoformat()
        lint["model"] = m
        lint["tokens"] = response.usage.total_tokens
        print(lint)
    except:
        print("Response is not in json")
    print("===========================")
    print(choices.message.content)
    print("===========================")
    print(response.usage)

#for choices in response["choices"]:
#    print("{")
#    print('"date": "' + datetime.datetime.now().isoformat() + '",')
#    print('"model": "' + m + '",')
#    print('"tokens": ' + str(response.usage.total_tokens) + ',')
#    print(choices.message.content.replace("{", "", 1))
#    print("===========================")

# print(choices.message.content)
