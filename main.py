from pydantic_ai import Agent 
# from pydantic_ai.models.openai import OpenAIModel 
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider 
from tools.files import list_files,read_file
# from tools.files import list_files
# print(list_files("."))
provider=OpenAIProvider(base_url="http://localhost:11434/v1",
                        api_key="ollama")
model=OpenAIChatModel("qwen2.5:1.5b",
                #provider=OpenAIProvider(base_url="http://localhost:11434/v1"))
                provider=provider)
agent=Agent(model,
            system_prompt=("""
You are CHERRY, a personal AI assistant.
When the user asks about files or directories,
use the available tools.
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
while True:
    user=input("YOU : ")
    # if user.lower()==("exit") or ("bye"):
    #     break
    if user.lower()=="exit" or user.lower()=="bye":
        break
    r=agent.run_sync(user)
    print("CHERRY : ",r.output)