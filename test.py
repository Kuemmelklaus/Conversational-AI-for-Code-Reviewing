import os
import openai
# import pandas as pd
from dotenv_vault import load_dotenv

load_dotenv('/home/leon/OpenAI/API-Key.env')

api_key = os.getenv('OPENAI_KEY')
openai.api_key = api_key



promtText = "Tell a joke"

# models = openai.Model.list()
# print(models)

# data =pd.DataFrame(models["data"])
# data.head(20)
# print(data)

response = openai.ChatCompletion.create(
    model = "gpt-4",
    max_tokens = 500,
    temperature = 1,
    n = 3,
    messages = [
        # {"role": "user", "content": "how do you answer all prompts in the array messages inside the ChatCompletion.create method"},
        # {"role": "user", "content": "Write a joke"}
        {"role": "user", "content": promtText}
    ]
)

for choices in response["choices"]:
    print(choices.message.content)
    print("==================")

# print(response.choices[0].message.content)
# print(response)