import openai 
from os import getenv
from datetime import datetime
from json import loads, decoder
from message import Message
from dotenv import load_dotenv

class Linter:

    #method to create a response with a model, max response tokens, temperature, and message array
    def create_response(self, mod, tok, tmp, msg):
        mes = []
        for n in msg:
            mes.append(n.get_message())

        response = openai.ChatCompletion.create(
            model = mod,
            max_tokens = tok,
            temperature = tmp,
            n = 1,
            messages = mes
        )
        return response

    #add metadata to response JSON
    def add_metadata(self, lint, model, response, code, programming_language, success):
        lint["date"] = datetime.now().isoformat()
        lint["model"] = model
        lint["total_tokens"] = response.usage.total_tokens
        lint["completion_tokens"] = response.usage.completion_tokens
        lint["code"] = code
        lint["programmingLanguage"] = programming_language
        lint["success"] = success
        return lint

    #initail prompts + few-shot example
    def create_prompt(self, programming_language, code):

        #Python prompt
        if programming_language == "python":
            #load few-shot example
            with open("./PythonExamples/guessinggame.py") as c:
                example = c.read()
            #load few-shot answer
            with open("./JSON/guessinggameLint.json") as g:
                lint = g.read()
            
            messages = [
                Message("system", f"Your task is to review code in the {programming_language} programming language and your purpose is to give helpful messages regarding coding mistakes or bad habits. You always answer in the JSON format, which contains the fields 'lineFrom', 'lineTo' and 'message'. The message field contains the criticism of the code between the fields lineFrom and lineTo. The message can not include inconsistent Indentations or missing docstrings."),
                Message("user", f"Here is some Python code:\n{example}"),
                Message("assistant", lint),
                Message("user", f"Great response! Here is some more {programming_language} code:\n{code}")
            ]
            return messages

        #ABAP prompt
        elif programming_language == "abap":
            #load example layout
            with open("./JSON/Layout.json", "r") as l:
                layout = l.read()

            messages = [
                Message("system", f"Your task is to review code in the {programming_language} programming language and your purpose is to give helpful messages regarding coding mistakes or bad habits. You always answer in the JSON format, which contains an array inside the field 'lint'. All objects inside 'lint' contain the fields 'lineFrom', 'lineTo' and 'message'. The message field contains the criticism of the code between the fields lineFrom and lineTo. The message can not include inconsistent Indentations or missing docstrings. Your layout should look like this: {layout}"),
                Message("user", f"Here is some {programming_language} code:\n{code}")
            ]
            return messages

        #unsupported programming language
        else:
            raise Exception("Unsupported programming language!")

    def get_lint(self):
        return self.lint

    #Constuct containing API request
    def __init__(self, programming_language, code):

        self.success = False

        #Select the GPT model ("gpt-3.5-turbo", "gpt-4", "gpt-3.5-turbo-16k" ...)
        model = "gpt-3.5-turbo-16k"

        #Select the maximum response tokens
        max_tokens = 9999

        #load the openai api key from the file "API-Key.env"
        load_dotenv("./API-Key.env")
        key = getenv("OPENAI_KEY")
        openai.api_key = key

        #initail prompts + few-shot example
        try:
            messages = self.create_prompt(programming_language, code)
        except Exception as exception:
            print(exception)
            quit()

        #generate response
        print("Generating response ...")
        response1 = self.create_response(model, max_tokens, 0.1, messages)

        for choices1 in response1["choices"]:
            try:
                print(response1)
                print("\n========================================\n")
                self.lint = loads(choices1.message.content)
                self.lint = self.add_metadata(self.lint, model, response1, code, programming_language, True)
                self.success = True
                print("Successful after one try.")

            except decoder.JSONDecodeError:
                print("Response is not in JSON!\nRetrying ...")
                messages.append(Message("assistant", choices1.message.content))
                messages.append(Message("user", "Your response was not a valid JSON. Please try again without any strings attached to your response."))

                #creating 2nd response
                response2 = self.create_response(model, max_tokens + response1.usage.completion_tokens, 0.1, messages)

                for choices2 in response2["choices"]:
                    try:
                        print(response2)
                        print("\n========================================\n")
                        self.lint = loads(choices2.message.content)
                        self.lint = self.add_metadata(self.lint, model, response2, code, programming_language, True)
                        self.success = True
                        print("Successful after two tries.")
                    except decoder.JSONDecodeError:
                        print("Response is not in JSON again!\nStopped!")
