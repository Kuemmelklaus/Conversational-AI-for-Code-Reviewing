
class Message:

    role = ""
    message = ""
    
    def __init__(self, role, msg):
        self.role = role
        self.message = msg
    
    def get_message(self):
        msg = {"role": self.role, "content": self.message}
        return msg
