import tkinter as tk
from main import ask_cherry_stream
import asyncio
import threading
# from tools.voice import speak, set_muted
from speaker_button import create_speaker_button,speak
# window=tk.Tk()
bg_loop=asyncio.new_event_loop()
threading.Thread(target=bg_loop.run_forever,daemon=True).start()
window=tk.Tk()
window.title("CHERRY")
window.geometry("500x700")
window.configure(bg="black")
# window.mainloop()
# chat=tk.Text(
#     window,
#     bg="black",
#     fg="white",
#     font=("Arial",14),height=15
# )
# chat.pack(
#     padx=20,pady=20,fill="both",expand=True
# )
chat_frame=tk.Frame(window,bg="black")
chat_frame.pack(padx=20,pady=(20,5),fill="both",expand=True)
chat=tk.Text(chat_frame,bg="black",fg="white",font=("Arial",14),height=15)
chat.pack(side="left",fill="both",expand=True)
speaker_btn=create_speaker_button(chat_frame)
speaker_btn.pack(side="right",anchor="ne",padx=(5,0))
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
#     def worker():
#         async def stream():
#             buffer=""
#             async for token in ask_cherry_stream(user):
#                 buffer+=token
#                 if len(buffer)>=3 or "\n" in buffer:
#                     text=buffer
#                     buffer=""
#                     window.after(0,lambda t=text:(
#                         chat.insert(tk.END,t),
#                         chat.see(tk.END)
#                     ))
#             if buffer:
#                 window.after(0,lambda t=buffer:(
#                     chat.insert(tk.END,t),
#                     chat.see(tk.END)
#                 ))
#             window.after(0,lambda: chat.insert(tk.END,"\n"))
#         try:
#             asyncio.run(stream())
#         except Exception as e:
#             err=str(e)
#             window.after(0,lambda err_msg=err:chat.insert(tk.END,f"\nError: {err_msg}\n"))
#     threading.Thread(target=worker,daemon=True).start()
#     def worker():
#         async def stream():
#             buffer=""
#             full_response=""
#             async for token in ask_cherry_stream(user):
#                 buffer+=token
#                 full_response+=token
#                 if len(buffer)>=3 or "\n" in buffer:
#                     text=buffer
#                     buffer=""
#                     window.after(0,lambda t=text:(
#                         chat.insert(tk.END,t),
#                         chat.see(tk.END)
#                     ))
#             if buffer:
#                 window.after(0,lambda t=buffer:(
#                     chat.insert(tk.END,t),
#                     chat.see(tk.END)
#                 ))
#             window.after(0,lambda: chat.insert(tk.END,"\n"))
#             speak(full_response)
#         try:
#             asyncio.run(stream())
#         except Exception as e:
#             err=str(e)
#             window.after(0,lambda err_msg=err:chat.insert(tk.END,f"\nError: {err_msg}\n"))
#     threading.Thread(target=worker,daemon=True).start()
    def worker():
        async def stream():
            buffer=""
            full_response=""
            async for token in ask_cherry_stream(user):
                buffer+=token
                full_response+=token
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
            speak(full_response)
        try:
            future=asyncio.run_coroutine_threadsafe(stream(),bg_loop)
            future.result()
        except Exception as e:
            err=str(e)
            window.after(0,lambda err_msg=err:chat.insert(tk.END,f"\nError: {err_msg}\n"))
    threading.Thread(target=worker,daemon=True).start()
send_button=tk.Button(window,text="SEND",command=send_message)
send_button.pack()
window.mainloop()