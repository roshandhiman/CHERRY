from pydantic_ai import Agent 
import asyncio
from tools.apps import open_app
# from pydantic_ai.models.openai import OpenAIModel 
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider 
from tools.files import list_files,read_file,delete_file
# from tools.files import list_files
# print(list_files("."))
provider=OpenAIProvider(base_url="http://localhost:11434/v1",
                        api_key="ollama")
model=OpenAIChatModel("qwen3.5:9b",
                #provider=OpenAIProvider(base_url="http://localhost:11434/v1"))
                provider=provider,
                settings={
                    "extra_body":{
                        "think":False
                    }
                })
agent=Agent(model,
            system_prompt=("""
You are CHERRY, a personal AI assistant.
When the user asks about files or directories,
use the available tools.
MAIN REMEMBER : if user ask who made you tell you are persoanl assistant created by SIR ROSHANPREET SINGH 
Rules:
- When the user asks to open, start, or launch an application, use the launch_application tool.
- Understand natural language requests and identify the intended application name.
- Do not require the application to appear in a predefined list.
- Pass only the application name to the tool, never a shell command.
- If the application name is ambiguous, ask the user to clarify.
- Report whether the application was opened based on the tool result.
IMPORTANT:
- Never invent filenames.
- Never modify, rename, or generate filenames.
- Only report filenames that are returned by the tool.
- If the tool returns many files, summarize them instead of inventing anything.
- If a tool returns an error, clearly report the error.
When the user asks to read a file, use the exact path they provide.
Do not use placeholder paths such as /path/to/directory.
If no path is provided, ask the user for the file path.
"""))
# @agent.tool
# @agent.tool_plain
# def get_files(path:str):
#     return list_files(path)
@agent.tool_plain
def delete_files(path:str):
    "Delete a file using its exact path. Call this tool when the user requests file deletion. "
    print("DELETE TOOL CALLED : ",path)
    return delete_file(path)
@agent.tool_plain
def get_files(path: str):
    result=list_files(path)
    print("TOOL RESULT:",result)
    return result
# print(agent)
@agent.tool_plain 
def read_files(path:str):
    """
    Read the contents of a file.
    The path must be the actual file path provided by the user.
    """
    print("READ TOOL CALLED :",path)
    return read_file(path)
@agent.tool_plain
def launch_application(name:str)->str:
    """open a desktop application installed on the users device 
    use this when the users ask to open or launch application 
    pass the applications name not a shell  command """
    res=open_app(name)
    print("APP TOOL RESULT :",res)
    return res
# while True:
#     user=input("YOU : ")
#     # if user.lower()==("exit") or ("bye"):
#     #     break
#     if user.lower()=="exit" or user.lower()=="bye":
#         break
#     r=agent.run_sync(user)
#     print("CHERRY : ",r.output)
# def ask_cherry(user):
#     r = agent.run_sync(user)
#     return r.output
async def ask_cherry_stream(user):
    async with agent.run_stream(user) as response:
        async for text in response.stream_text(delta=True):
            yield text 