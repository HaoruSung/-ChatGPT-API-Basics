import openai

# load and set our key
openai.api_key = open("key.txt", "r").read().strip("\n")

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", # this is "ChatGPT" $0.002 per 1k tokens
  messages=[{"role": "user", "content": "Who is the President of the United States in 2023?"}]
)

print(completion)

reply_content = completion.choices[0].message.content
print(reply_content)