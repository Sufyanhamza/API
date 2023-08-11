import openai

openai.api_key = "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"

response = openai.Completion.create(
  # engine="davinci",
  engine="text-davinci-003",
  prompt="write a copy to sell cowboy hat",
  max_tokens = 200
)

# print(response)
print(response["choices"][0].text)

