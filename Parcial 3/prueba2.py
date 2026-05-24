from openai import OpenAI

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = "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"
)

completion = client.chat.completions.create(
  model="deepseek-ai/deepseek-v3.2",
  messages=[{"role":"user","content":"cuentame un cuento"}],
  temperature=1,
  top_p=0.95,
  max_tokens=100,
  extra_body={"chat_template_kwargs": {"thinking":False}},
  stream=True
)

for chunk in completion:
  if not getattr(chunk, "choices", None):
    continue
  reasoning = getattr(chunk.choices[0].delta, "reasoning_content", None)
  if reasoning:
    print(reasoning, end="")
  if chunk.choices and chunk.choices[0].delta.content is not None:
    print(chunk.choices[0].delta.content, end="")
  

