import os
import openai

PROMPT = "portrait of person ,Smooth soft skin, big dreamy eyes, symmetrical, anime wide eyes, soft lighting, detailed face, by makoto shinkai, stanley artgerm lau, wlop, rossdraws, concept art, digital painting, looking into camera"

openai.api_key = "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"

# API Key

# Method 1
response = openai.Image.create(
    prompt = PROMPT,
    n=1,
    size = "256x256",
)

print(response["data"][0]["url"])


#Method 2
# response = openai.Image.acreate(
#     prompt = PROMPT,
#     n=1,
#     size = "256x256",
# )

# print(response["data"][0]["url"])