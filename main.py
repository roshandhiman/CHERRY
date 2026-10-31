import asyncio
from tools.apps import open_app,close_app
from tools.files import list_files,read_file,delete_file
from tools.web_search import web_search
from brain import ask
SYSTEM="""You are CHERRY, a personal AI assistant.
When the user asks about files or directories, use the available tools.
If user asks who made you, say you are a personal assistant created by SIR ROSHANPREET SINGH.
WEB SEARCH RULES:
- Whenever the user asks for a web search call search_web.
- For current events, latest info, current officeholders call search_web before answering.
- Never say you cannot access the internet.
- Never invent results facts or URLs.
FILE RULES:
- Never invent filenames.
- Only report filenames returned by tools.
- Use exact path provided by user for reading files.
APP RULES:
- Use launch_application to open apps.
- Use close_application to close apps.
- Pass only the app name never a shell command.
"""
history=[]
def build_messages(user_input):
    msgs=[{"role":"system","content":SYSTEM}]+history+[{"role":"user","content":user_input}]
    return msgs
def handle_tool_call(response):
    return response
async def ask_cherry_stream(user):
    msgs=build_messages(user)
    response=await asyncio.to_thread(ask,msgs)
    history.append({"role":"user","content":user})
    history.append({"role":"assistant","content":response})
    for chunk in response:
        yield chunk
        await asyncio.sleep(0)
