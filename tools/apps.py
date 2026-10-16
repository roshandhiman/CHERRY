import subprocess
def open_app(name:str):
    name=name.strip()
    if not name:
        return "Please Provide Correct App Name"
    try:
        result=subprocess.run(
            ["open","-a",name],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode==0:
            return f"Opened {name} successfully."
        return f"could not open {name}"
    except subprocess.TimeoutExpired:
        return f"Opening {name} timed out"
    except Exception as e:
        return f"Error opening {name} :{e}"
def close_app(name:str)->str:
    name=name.strip()
    if not name:
        return "Error: Apllication name is empty"
    try:
        result=subprocess.run(
            ["osascript","-e",f'Tell application "{name}" to quit'],
            capture_output=True,
            text=True,
            timeout=15
        )
        if result.returncode==0:
            return f"Close command succeeded for {name}."
        return f"Could not close {name}:{result.stderr.strip()}"
    except subprocess.TimeoutExpired:
        return f"Closing {name}  tomied out."
    except Exception as e:
        return f"Eroor closing {name}:{e}"