import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

print(openai.Model.list())
completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "自我介绍下"}
  ]
)

print(completion.choices[0].message.content)