# import os
# print(os.listdir("."))
import os
def list_files(path):
    files=os.listdir(path)
    return {"path":path,"files":files}