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

    def getLint(self):
        return self.lint
    
    #def escape(self, string):
        

    #Constuct
    def __init__(self, programmingLanguage, code):

        self.done = False

        #Select the GPT model ("gpt-3.5-turbo", "gpt-4"...)
        m = "gpt-3.5-turbo-16k"

        #Select the maximum response tokens
        maxTok = 1000

        #load example layout
        with open("../Layout.json", "r") as l:
            layout = l.read()

        #load the openai api key from the file "API-Key.env"
        load_dotenv("../API-Key.env")
        api_key = os.getenv("OPENAI_KEY")
        openai.api_key = api_key

        #initail prompts
        messages = [
            Message("system", "You are a code linter for the " + programmingLanguage + " programming language and your purpose is to give helpful messages regarding coding mistakes or bad habits. You always answer in the JSON format, which contains the fields 'lineFrom', 'lineTo' and 'message'. The message field contains the criticism of the code between the fields lineFrom and lineTo."),
            Message("assistant", "I will use the following template" + layout),
            Message("user", "Here is some " + programmingLanguage + " code:\n" + code)
        ]

        #generate response
        response1 = self.createResponse(m, maxTok, 0.1, messages)

        for choices1 in response1["choices"]:
            try:
                self.lint = json.loads(choices1.message.content)
                self.lint["date"] = datetime.datetime.now().isoformat()
                self.lint["model"] = m
                self.lint["tokens"] = response1.usage.total_tokens
                self.lint["code"] = code
                print(choices1.message.content)
            except json.decoder.JSONDecodeError:
                print("Response is not in JSON!")
                print(choices1.message.content)
                messages.append(Message("user", "Your response was not a valid JSON. Please try again."))
                response2 = self.createResponse(m, maxTok, 0.1, messages)
                for choices2 in response2["choices"]:
                    try:
                        self.lint = json.loads(choices2.message.content)
                        self.lint["date"] = datetime.datetime.now().isoformat()
                        self.lint["model"] = m
                        self.lint["tokens"] = response2.usage.total_tokens
                        self.lint["code"] = code
                        print(choices2.message.content)
                    except json.decoder.JSONDecodeError:
                        print("Response is not in JSON again!")
                        quit()

            self.done = True
