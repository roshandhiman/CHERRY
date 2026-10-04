# import os
# print(os.listdir("."))
import os
def list_files(path):
    files=os.listdir(path)
    return {"path":path,"files":files}
def read_file(path):
    # if path=="/path/to/directory":
    #     return "ERROR: Invalid placeholder path. Use the exact file path provided by the user."
    # with open(path,"r")as file:
    #     return file.read()
    if not os.path.isabs(path):
        path=os.path.abspath(path)
    if not os.path.exists(path):
        return f"File not found: {path}"
    with open(path,"r")as file:
        return file.read()