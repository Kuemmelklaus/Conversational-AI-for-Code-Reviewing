from flask import Flask, jsonify
import random
import string

app = Flask(__name__)

def generate_random_text(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

@app.route('/text', methods=['GET'])
def get_random_text():
    random_text = generate_random_text(20)  # Change the length as needed
    response = {'random_text': random_text}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
