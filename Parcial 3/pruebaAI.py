import os

from flask.cli import load_dotenv
from openai import OpenAI

prompt = input("Escribe tu algo: ")
load_dotenv()
client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = os.getenv("NVIDIA_API_KEY")
)


completion = client.chat.completions.create(
  model="deepseek-ai/deepseek-v4-flash",
  messages=[{"content":prompt,"role":"user"}],
  temperature=1,
  top_p=0.95,
  max_tokens=500,
  extra_body={"chat_template_kwargs":{"thinking":True,"reasoning_effort":"high"}},
  stream=True
)

for chunk in completion:
  if not getattr(chunk, "choices", None):
    continue
  reasoning = getattr(chunk.choices[0].delta, "reasoning", None) or getattr(chunk.choices[0].delta, "reasoning_content", None)
  if reasoning:
    print(reasoning, end="")
  if chunk.choices and chunk.choices[0].delta.content is not None:
    print(chunk.choices[0].delta.content, end="")
  


