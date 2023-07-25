import json

class Linter:

    def __init__(self, programmingLanguage, code):
        self.dummie = json.loads('{"success": "true"}')
        self.dummie["programmingLanguage"] = programmingLanguage
        self.dummie["code"] = code
        self.dummie["message"] = "Your code looks goofy!"

    def getLint(self):
        return self.dummie