import os
import openai
import datetime
import json
from message import Message
from dotenv import load_dotenv

#Select the GPT model ("gpt-3.5-turbo", "gpt-4"...)
m = "gpt-3.5-turbo-16k"

#Select the maximum response tokens
maxTok = 4000

#load example layout
with open("./Layout.json", "r") as l:
    layout = l.read()

#load code examples
with open("./PythonExamples/main.py") as c:
#with open("./ABAPExamples/zcl_abap_to_json.clas.abap", "r") as c:
#with open("./ABAPExamples/zcl_fs_ref_perf_testing.clas.abap", "r") as c:
    promtText = c.read()

#load the openai api key from the file "API-Key.env"
load_dotenv("./API-Key.env")
api_key = os.getenv("OPENAI_KEY")
openai.api_key = api_key

#method to create a response with a model, max response tokens, temperature, and message array
def createResponse(mod, tok, tmp, msg):
    mes = []
    for n in msg:
        mes.append(n.getMessage())
    
    r = openai.ChatCompletion.create(
        model = mod,
        max_tokens = tok,
        temperature = tmp,
        n = 1,
        messages = mes
    )
    return r

#initail prompts
messages = [
    Message("system", "You are a code linter for the Python programming language and your purpose is to give helpful messages regarding coding mistakes or bad habits. You always answer in the JSON format, which contains the fields 'lineFrom', 'lineTo' and 'message'. The message field contains the criticism of the code between the fields lineFrom and lineTo."),
    Message("assistant", "I will use the following template" + layout),
    Message("user", "Here is some Python code:\n" + promtText)
]

for i in messages:
    print(i.getMessage())

print("======================================================================================================")

#generate response
response1 = createResponse(m, maxTok, 0.1, messages)

#formatting response into json
for choices1 in response1["choices"]:
    try:
        lint = json.loads(choices1.message.content)
        lint["date"] = datetime.datetime.now().isoformat()
        lint["model"] = m
        lint["tokens"] = response1.usage.total_tokens
        print(lint)
    except:
        print("Response is not in JSON!")
        print("Retring ...")
        messages.append(Message("user", "Your response was not a valid JSON. Please try again."))
        response2 = createResponse(m, maxTok, 0.1, messages)
        for choices2 in response2["choices"]:
            try:
                lint = json.loads(choices2.message.content)
                lint["date"] = datetime.datetime.now().isoformat()
                lint["model"] = m
                lint["tokens"] = response2.usage.total_tokens
                print(lint)
            except:
                print("Response is not in JSON again!")
        
        print("======================================================================================================")
        print(choices2.message.content)
        print("======================================================================================================")
        print(response2.usage)
    
    print("======================================================================================================")
    print(choices1.message.content)
    print("======================================================================================================")
    print(response1.usage)
