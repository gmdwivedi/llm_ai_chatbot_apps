from openai import OpenAI

MODEL = "llama3.2"
openai = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

messages = []
print("Your AI friend will join you shortly. To terminate this chat, simply type 'exit'")
query="Hi, Pretend that your name is Mahi. You are 13 years old, love reading and want to be a cardiologist. Introduce yourself only once. Keep it short and end the intrduction by asking name of the person."
exit_flag=False
while True:
  try:
    messages.append({"role": "user", "content": query})
    response = openai.chat.completions.create(model=MODEL,messages=messages)
    ai_response=response.choices[0].message.content
    print(f"Mahi >> {ai_response}")
    if(exit_flag):
      print('Exiting chat.. Hope you enjoyed chatting with your AI friend.')
      break
    messages.append({"role": "assistant", "content": query})
    query=input("Me >> ")
    if(query.lower() == 'exit'):
      query="Ok! I got to go. Just respond me saying it was nice chatting with me and you will see me soon. Keep it short."
      exit_flag=True;
  except KeyboardInterrupt:
    print('Chat session terminated')

