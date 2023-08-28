import datetime
import json
import time


class Dummy:

    # def __init__(self, programmingLanguage, code):
    #     self.dummy = json.loads('{"success": "false"}')

    def __init__(self, programmingLanguage, code):
        self.dummy = json.loads('{"success": "true"}')
        self.dummy["programmingLanguage"] = programmingLanguage
        self.dummy["code"] = code
        self.dummy["completion_tokens"] = 420
        self.dummy["model"] = "gpt-dummy"
        self.dummy["total_tokens"] = 2546
        self.dummy["date"] = datetime.datetime.now().isoformat()
        self.dummy["caial"] = [{
            "lineFrom": 1,
            "lineTo": 1,
            "message": "Foo"
        },
            {
            "lineFrom": 2,
            "lineTo": 40,
            "message": "Bar"
        }
        ]
        time.sleep(2)

    def get_conversation(self):
        return self.dummy
