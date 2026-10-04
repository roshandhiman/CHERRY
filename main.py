from pydantic_ai import Agent 
# from pydantic_ai.models.openai import OpenAIModel 
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider 
from tools.files import list_files
# print(list_files("."))
model=OpenAIChatModel("qwen2.5-coder:7b",
                  provider=OpenAIProvider(base_url="http://localhost:11434/v1"))
agent=Agent(model,
            system_prompt="Your are CHERRY a helfup personal AI " \
            "assistant you are like a brother to all " \
            "you have a very good brain think proepr like human before answeringg"
            "is user ask to sho the files you can use the tools to show the files instead of askign to the user  .. do it own")
# @agent.tool
@agent.tool_plain
def get_files(path:str):
    return list_files(path)

while True:
    user=input("YOU : ")
    # if user.lower()==("exit") or ("bye"):
    #     break
    if user.lower()=="exit" or user.lower()=="bye":
        break
    r=agent.run_sync(user)
    print("CHERRY : ",r.output)