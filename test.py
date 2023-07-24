import os
import openai
import datetime
import json
from message import Message
from dotenv import load_dotenv

#Select the GPT model ("gpt-3.5-turbo", "gpt-4"...)
m = "gpt-3.5-turbo"

#with open("./ABAPExamples/zcl_abap_to_json.clas.abap", "r") as c:
#    promtText = c.read()

#with open("./ABAPExamples/zcl_fs_ref_perf_testing.clas.abap", "r") as c:
#    promtText = c.read()

with open("./PythonExanples/main.py") as c:
    promtText = c.read()

with open("./Layout.json", "r") as l:
    layout = l.read()

#load the openai api key from the file "API-Key.env"
load_dotenv("./API-Key.env")
api_key = os.getenv("OPENAI_KEY")
openai.api_key = api_key

messages = [
    Message("system", "Your name is 'ABAP-Linter' and your purpose is to assist development in the ABAP language."),
    Message("user", "Always answer in a systematic scheme. This has to includes a rating of a specific section of code from 0 to 10, the first and last line where this rated code is written and a reason for that given rating. For example if some old fashioned method is used, make a suggestion how to replace this method. Please dont rate any empty lines but remember to still count the new line characters when generating 'lineFrom' and 'lineTo'."),
    Message("assistant", "I will answer prompts using .json in the following format: " + layout),
    Message("user", promtText)
]

for i in messages:
    print(i.getMessage())

print("========================")

def createResponse(mod, tmp, msg):
    mes = []
    for n in msg:
        mes.append(n.getMessage())
    
    r = openai.ChatCompletion.create(
        model = mod,
        max_tokens = 2000,
        temperature = tmp,
        n = 1,
        messages = mes
    )
    return r

#generate response
#response = openai.ChatCompletion.create(
#    model = m,
#    max_tokens = 2000,
#    temperature = 0.1,
#    n = 1,
#    messages = [
#        {"role": "system", "content": "Your name is 'ABAP-Linter' and your purpose is to assist development in the ABAP language."},
#        {"role": "user", "content": "Always answer in a systematic scheme. This has to includes a rating of a specific section of code from 0 to 10, the first and last line where this rated code is written and a reason for that given rating. For example if some old fashioned method is used, make a suggestion how to replace this method. Please dont rate any empty lines but remember to still count the new line characters when generating 'lineFrom' and 'lineTo'."},
#        {"role": "assistant", "content": "I will answer prompts using .json in the following format: " + layout},
#        {"role": "user", "content": "Do not rate simple statements such as 'ENDCLASS'. Please make an effort to count the lines correctly."},
#        {"role": "assistant", "content": "I will continue rating only valuable sections of code. Please input some ABAP code."},
#        {"role": "user", "content": promtText}
#    ]
#)

response1 = createResponse(m, 0.1, messages)

#formatting response into json
for choices in response1["choices"]:
    try:
        lint = json.loads(choices.message.content)
        lint["date"] = datetime.datetime.now().isoformat()
        lint["model"] = m
        lint["tokens"] = response1.usage.total_tokens
        print(lint)
    except:
        print("Response is not in json!")
        print("Retring ...")
        messages.append(Message("assistant", choices.message.content))
        messages.append(Message("user", "Your response was not a valid JSON. Please try again."))
        response2 = createResponse(m, 0.1, messages)
        for choices in response1["choices"]:
            try:
                lint = json.loads(choices.message.content)
                lint["date"] = datetime.datetime.now().isoformat()
                lint["model"] = m
                lint["tokens"] = response1.usage.total_tokens
                print(lint)
            except:
                print("Response is not in json again!")
    
    print("===========================")
    print(choices.message.content)
    print("===========================")
    print(response1.usage)

#for choices in response["choices"]:
#    print("{")
#    print('"date": "' + datetime.datetime.now().isoformat() + '",')
#    print('"model": "' + m + '",')
#    print('"tokens": ' + str(response.usage.total_tokens) + ',')
#    print(choices.message.content.replace("{", "", 1))
#    print("===========================")

# print(choices.message.content)
