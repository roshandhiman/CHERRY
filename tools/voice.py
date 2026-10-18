import subprocess
import threading
_muted=False
def set_muted(value):
    global _muted 
    _muted = value 
def spead(text):
    if _muted or not text.strip():
        return 
    def run():
        subprocess.run(
            ["say","-v","Samantha",text],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    threading.Thread(target=run,daemon=True).start()