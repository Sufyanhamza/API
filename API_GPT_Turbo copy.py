# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai

openai.api_key = "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"

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "user", "content": "Where was it played?"}
    ]
)

print(response['choices'][0]['message'].content)