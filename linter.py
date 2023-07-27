import os
import openai
import datetime
import json
from message import Message
from dotenv import load_dotenv

class Linter:

    #method to create a response with a model, max response tokens, temperature, and message array
    def createResponse(self, mod, tok, tmp, msg):
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
    
    def addFields(self, lint, model, response, code, programmingLanguage):
        lint["date"] = datetime.datetime.now().isoformat()
        lint["model"] = model
        lint["total_tokens"] = response.usage.total_tokens
        lint["completion_tokens"] = response.usage.completion_tokens
        lint["code"] = code
        lint["programmingLanguage"] = programmingLanguage
        return lint


    def getLint(self):
        return self.lint
    
    #def escape(self, string):
        

    #Constuct
    def __init__(self, programmingLanguage, code):

        self.done = False

        #Select the GPT model ("gpt-3.5-turbo", "gpt-4", "gpt-3.5-turbo-16k" ...)
        m = "gpt-3.5-turbo-16k"

        #Select the maximum response tokens
        maxTok = 4000

        #load example layout
        with open("../Layout.json", "r") as l:
            layout = l.read()

        #load few-shot example
        with open("../PythonExamples/example.py") as c:
            expl = c.read()
        
        #load few-shot answer
        with open("../exampleLint.json") as g:
            lint = g.read()

        #load the openai api key from the file "API-Key.env"
        load_dotenv("../API-Key.env")
        api_key = os.getenv("OPENAI_KEY")
        openai.api_key = api_key

        #initail prompts
        messages = [
            Message("system", "You are a code linter for the " + programmingLanguage + " programming language and your purpose is to give helpful messages regarding coding mistakes or bad habits. You always answer in the JSON format, which contains the fields 'lineFrom', 'lineTo' and 'message'. The message field contains the criticism of the code between the fields lineFrom and lineTo."),
            Message("user", "Please help me improve coding in the " + programmingLanguage + " programming language as best as you can. Do not repeat the same message, instead just include 'this criticism can be repeated further down' in the first message which contains the repeating message. Do not mention indentations."),
            Message("assistant", "I will try to give valueble advise using the following template:\n" + layout + "\nPlease provide some code in " + programmingLanguage + "."),
            Message("user", "Here is some Python code:\n" + expl),
            Message("assistant", lint),
            Message("user", "Great answer, please do it again for the following " + programmingLanguage + " code:" + code)
        ]

        #generate response
        print("Generating response ...")
        response1 = self.createResponse(m, maxTok, 0.1, messages)

        for choices1 in response1["choices"]:
            try:
                print(response1)
                print("========================================")
                self.lint = json.loads(choices1.message.content)
                self.lint = self.addFields(self.lint, m, response1, code, programmingLanguage)
                self.done = True
                self.lint["success"] = "True"
                print("Successful after one try.")
                #print(choices1.message.content)
            except json.decoder.JSONDecodeError:
                print("Response is not in JSON!\nRetrying ...")
                #print(choices1.message.content)
                messages.append(Message("user", "Your response was not a valid JSON. Please try again."))
                response2 = self.createResponse(m, maxTok, 0.1, messages)
                for choices2 in response2["choices"]:
                    try:
                        print(response2)
                        print("========================================")
                        self.lint = json.loads(choices2.message.content)
                        self.lint = self.addFields(self.lint, m, response2, code, programmingLanguage)
                        self.done = True
                        self.lint["success"] = "True"
                        print("Successful after two tries.")
                        #print(choices2.message.content)
                    except json.decoder.JSONDecodeError:
                        print("Response is not in JSON again!\nStopped!")
                        self.lint = json.loads('{"success": "False"}')
