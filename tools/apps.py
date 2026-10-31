import os
import subprocess
def get_installed_apps():
    apps=[]
    for d in ["/Applications","/System/Applications","/System/Applications/Utilities"]:
        if os.path.exists(d):
            apps+=[f[:-4] for f in os.listdir(d) if f.endswith(".app")]
    return apps
def find_app_name(name):
    clean=name.lower().replace(" ","")
    apps=get_installed_apps()
    for a in apps:
        if clean==a.lower().replace(" ",""):
            return a
    for a in apps:
        if clean in a.lower().replace(" ",""):
            return a
    return name
# def open_app(name:str):
#     name=name.strip()
#     if not name:
#         return "Please Provide Correct App Name"
#     try:
#         result=subprocess.run(
#             ["open","-a",name],
#             capture_output=True,
#             text=True,
#             timeout=10
#         )
#         if result.returncode==0:
#             return f"Opened {name} successfully."
#         return f"could not open {name}"
#     except subprocess.TimeoutExpired:
#         return f"Opening {name} timed out"
#     except Exception as e:
#         return f"Error opening {name} :{e}"
def open_app(name:str):
    name=name.strip()
    if not name:
        return "Please Provide Correct App Name"
    target=find_app_name(name)
    try:
        result=subprocess.run(["open","-a",target],capture_output=True,text=True,timeout=10)
        if result.returncode==0:
            return f"Opened {target} successfully."
        return f"could not open {name}"
    except subprocess.TimeoutExpired:
        return f"Opening {name} timed out"
    except Exception as e:
        return f"Error opening {name} :{e}"
# def close_app(name:str)->str:
#     name=name.strip()
#     if not name:
#         return "Error: Apllication name is empty"
#     try:
#         result=subprocess.run(
#             ["osascript","-e",f'Tell application "{name}" to quit'],
#             capture_output=True,
#             text=True,
#             timeout=15
#         )
#         if result.returncode==0:
#             return f"Close command succeeded for {name}."
#         return f"Could not close {name}:{result.stderr.strip()}"
#     except subprocess.TimeoutExpired:
#         return f"Closing {name}  tomied out."
#     except Exception as e:
#         return f"Eroor closing {name}:{e}"
def close_app(name:str)->str:
    name=name.strip()
    if not name:
        return "Error: Application name is empty"
    target=find_app_name(name)
    try:
        result=subprocess.run(["osascript","-e",f'Tell application "{target}" to quit'],capture_output=True,text=True,timeout=15)
        if result.returncode==0:
            return f"Close command succeeded for {target}."
        return f"Could not close {name}:{result.stderr.strip()}"
    except subprocess.TimeoutExpired:
        return f"Closing {name} timed out."
    except Exception as e:
        return f"Error closing {name}:{e}"