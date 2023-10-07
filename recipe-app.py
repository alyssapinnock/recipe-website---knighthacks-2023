import openai
import json

openai.api_key = "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"

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages = [{"role": "user", "content": "What is the purpose of life?"}]
)
print(completion)
print(f"Type of output: {type(completion)}")
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(completion, f, ensure_ascii=False, indent=4)
