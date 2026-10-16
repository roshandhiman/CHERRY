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