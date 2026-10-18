import tkinter as tk
from main import ask_cherry_stream
import asyncio
import threading
from tools.voice import speak, set_muted
window=tk.Tk()
window.title("CHERRY")
window.geometry("500x700")
window.configure(bg="black")
# window.mainloop()
chat=tk.Text(
    window,
    bg="black",
    fg="white",
    font=("Arial",14),height=15
)
chat.pack(
    padx=20,pady=20,fill="both",expand=True
)
input_box=tk.Entry(window,bg="black",fg="white",font=("Arial",14))
input_box.pack(padx=20,pady=10,fill="x")
# def send_message():
#     user=input_box.get()
#     chat.insert(tk.END,"YOU -> "+user+"\n")
#     resp=ask_cherry(user)
#     chat.insert(tk.END,"CHERRY -> "+resp+"\n")
#     input_box.delete(0,tk.END)
def send_message():
    user=input_box.get().strip()
    if not user:
        return
    chat.insert(tk.END, "YOU -> "+user+"\n")
    chat.insert(tk.END,"CHERRY -> ")
    input_box.delete(0,tk.END)
    # def worker():
    #     async def stream():
    #         async for token in ask_cherry_stream(user):
    #             window.after(0,lambda t=token:(
    #                 chat.insert(tk.END,t),
    #                 chat.insert(tk.END,"\n")
    #             ))
    #     asyncio.run(stream())
    #     window.after(0,lambda: chat.insert(tk.END,"\n"))
    # threading.Thread(target=worker,daemon=True).start()
    def worker():
        async def stream():
            buffer=""
            async for token in ask_cherry_stream(user):
                buffer+=token
                if len(buffer)>=3 or "\n" in buffer:
                    text=buffer
                    buffer=""
                    window.after(0,lambda t=text:(
                        chat.insert(tk.END,t),
                        chat.see(tk.END)
                    ))
            if buffer:
                window.after(0,lambda t=buffer:(
                    chat.insert(tk.END,t),
                    chat.see(tk.END)
                ))
            window.after(0,lambda: chat.insert(tk.END,"\n"))
        try:
            asyncio.run(stream())
        except Exception as e :
            window.after(
                0,
                lambda:chat.insert(tk.END,f"\nError: {e}\n")
            )
    threading.Thread(target=worker,daemon=True).start()
send_button=tk.Button(window,text="SEND",command=send_message)
send_button.pack()
window.mainloop()