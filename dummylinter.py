import json

class Dlinter:

    def __init__(self, programmingLanguage, code):
        self.dummy = json.loads('{"success": "true"}')
        self.dummy["programmingLanguage"] = programmingLanguage
        self.dummy["code"] = code
        self.dummy["lint"] = [{
            "lineFrom": 1,
            "lineTo": 1,
            "message": "foo"
        },
        {
            "lineFrom": 2,
            "lineTo": 4,
            "message": "bar"
        }
        ]

    def get_lint(self):
        return self.dummy