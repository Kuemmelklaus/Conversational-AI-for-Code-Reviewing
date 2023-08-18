import os
import openai
import datetime
import json
from message import Message
from dotenv import load_dotenv

class Linter:

    #method to create a response with a model, max response tokens, temperature, and message array
    def create_response(self, mod, tok, tmp, msg):
        mes = []
        for n in msg:
            mes.append(n.get_message())

        r = openai.ChatCompletion.create(
            model = mod,
            max_tokens = tok,
            temperature = tmp,
            n = 1,
            messages = mes
        )
        return r
    
    #add metadata to response JSON
    def add_metadata(self, lint, model, response, code, programmingLanguage, success):
        lint["date"] = datetime.datetime.now().isoformat()
        lint["model"] = model
        lint["total_tokens"] = response.usage.total_tokens
        lint["completion_tokens"] = response.usage.completion_tokens
        lint["code"] = code
        lint["programmingLanguage"] = programmingLanguage
        lint["success"] = success
        return lint


    def get_lint(self):
        return self.lint

    #Constuct
    def __init__(self, programmingLanguage, code):

        self.success = False

        #Select the GPT model ("gpt-3.5-turbo", "gpt-4", "gpt-3.5-turbo-16k" ...)
        m = "gpt-3.5-turbo-16k"

        #Select the maximum response tokens
        maxTok = 2000

        #load example layout
        #with open("./JSON/Layout.json", "r") as l:
        #    layout = l.read()

        #load few-shot example
        #with open("./PythonExamples/example.py") as c:
        with open("./PythonExamples/guessinggame.py") as c:
            example = c.read()
        
        #load few-shot answer
        #with open("./JSON/exampleLint.json") as g:
        with open("./JSON/guessinggameLint.json") as g:
            lint = g.read()

        #load the openai api key from the file "API-Key.env"
        load_dotenv("./API-Key.env")
        api_key = os.getenv("OPENAI_KEY")
        openai.api_key = api_key

        #initail prompts + few-shot example
        messages = [
            Message("system", f"Your task is to review code in the {programmingLanguage} programming language and your purpose is to give helpful messages regarding coding mistakes or bad habits. You always answer in the JSON format, which contains the fields 'lineFrom', 'lineTo' and 'message'. The message field contains the criticism of the code between the fields lineFrom and lineTo. The message can not include inconsistent Indentations or missing docstrings."),
            Message("user", f"Here is some Python code:\n{example}"),
            Message("assistant", lint),
            Message("user", f"Great response! Here is some more {programmingLanguage} code:\n{code}")
        ]

        #generate response
        print("Generating response ...")
        response1 = self.create_response(m, maxTok, 0.1, messages)

        for choices1 in response1["choices"]:
            try:
                print(response1)
                print("\n========================================\n")
                self.lint = json.loads(choices1.message.content)
                self.lint = self.add_metadata(self.lint, m, response1, code, programmingLanguage, True)
                self.success = True
                print("Successful after one try.")
                #print(choices1.message.content)
            except json.decoder.JSONDecodeError:
                print("Response is not in JSON!\nRetrying ...")
                #print(choices1.message.content)
                messages.append(Message("user", "Your response was not a valid JSON. Please try again."))
                response2 = self.create_response(m, maxTok, 0.1, messages)
                for choices2 in response2["choices"]:
                    try:
                        print(response2)
                        print("\n========================================\n")
                        self.lint = json.loads(choices2.message.content)
                        self.lint = self.add_metadata(self.lint, m, response2, code, programmingLanguage, True)
                        self.success = True
                        print("Successful after two tries.")
                        #print(choices2.message.content)
                    except json.decoder.JSONDecodeError:
                        print("Response is not in JSON again!\nStopped!")
                        #self.lint = json.loads('{"success": false}')
