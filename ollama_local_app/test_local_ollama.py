from openai import OpenAI

MODEL = "llama3.2"
openai = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
query=[{"role": "user", "content": "What is 9*8?"}]

response = openai.chat.completions.create(
 model=MODEL,
 messages=query
)
print("Query asked:" + query[0].get('content'))
print(response.choices[0].message.content)
