# import os
# print(os.listdir("."))
import os
def list_files(path):
    files=os.listdir(path)
    return {"path":path,"files":files}
def read_file(path):
    if path=="/path/to/directory":
        return "ERROR: Invalid placeholder path. Use the exact file path provided by the user."
    with open(path,"r")as file:
        return file.read()