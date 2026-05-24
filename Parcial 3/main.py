from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI()

# Cliente de NVIDIA
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="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"
)

# Modelo de entrada
class Prompt(BaseModel):
    message: str


@app.post("/chat")
def chat(prompt: Prompt):
    completion = client.chat.completions.create(
        model="deepseek-ai/deepseek-v4-flash",
        messages=[{"role": "user", "content": prompt.message}],
        temperature=1,
        top_p=0.95,
        max_tokens=1024,
        stream=False  # aquí sin streaming para empezar fácil
    )

    response = completion.choices[0].message.content
    return {"response": response}