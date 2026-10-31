import os
import socket
from dotenv import load_dotenv
from google import genai
from openai import OpenAI
load_dotenv()
def has_internet():
    try:
        socket.setdefaulttimeout(2)
        socket.create_connection(("8.8.8.8",53))
        return True
    except:
        return False
gemini_client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
openai_client=OpenAI(api_key=os.getenv("OEPN_AI_API_KEY"))
groq_client=OpenAI(api_key=os.getenv("GROQ_API_KEY"),base_url="https://api.groq.com/openai/v1")
openrouter_client=OpenAI(api_key=os.getenv("OPENROUTER_API_KEY"),base_url="https://openrouter.ai/api/v1")
deepseek_client=OpenAI(api_key=os.getenv("DEEPSEEK_API_KEY"),base_url="https://api.deepseek.com")
nvidia_client=OpenAI(api_key=os.getenv("NVIDIA_API_KEY"),base_url="https://integrate.api.nvidia.com/v1")
ollama_client=OpenAI(api_key="ollama",base_url="http://localhost:11434/v1")
def ask_gemini(messages):
    text="\n".join(f"{m['role']}: {m['content']}" for m in messages)
    r=gemini_client.models.generate_content(model="gemini-2.5-flash",contents=text)
    return r.text
def ask_openai(messages):
    r=openai_client.chat.completions.create(model="gpt-4o-mini",messages=messages)
    return r.choices[0].message.content
def ask_groq(messages):
    r=groq_client.chat.completions.create(model="llama-3.3-70b-versatile",messages=messages)
    return r.choices[0].message.content
def ask_openrouter(messages):
    r=openrouter_client.chat.completions.create(model="mistralai/mistral-7b-instruct",messages=messages)
    return r.choices[0].message.content
def ask_deepseek(messages):
    r=deepseek_client.chat.completions.create(model="deepseek-chat",messages=messages)
    return r.choices[0].message.content
def ask_nvidia(messages):
    r=nvidia_client.chat.completions.create(model="meta/llama-3.1-70b-instruct",messages=messages)
    return r.choices[0].message.content
def ask_ollama(messages):
    text="\n".join(f"{m['role']}: {m['content']}" for m in messages)
    r=ollama_client.chat.completions.create(model="qwen3.5:9b",messages=messages,extra_body={"think":False})
    return r.choices[0].message.content
def ask(messages):
    if not has_internet():
        return ask_ollama(messages)
    providers=[ask_gemini,ask_groq,ask_openrouter,ask_deepseek,ask_nvidia,ask_openai,ask_ollama]
    for fn in providers:
        try:
            return fn(messages)
        except:
            continue
    return "All models failed."

