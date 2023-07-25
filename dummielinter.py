import json

class Linter:

    def __init__(self, programmingLanguage, code):
        self.done = False
        self.dummie = json.loads('{"success": "true"}')
        self.dummie["programmingLanguage"] = programmingLanguage
        self.dummie["code"] = code
        self.dummie["message"] = "Your code looks goofy!"
        self.done = True

    def getLint(self):
        return self.dummie