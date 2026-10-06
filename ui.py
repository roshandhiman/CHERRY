import tkinter as tk
from main import ask_cherry
window=tk.Tk()
window.title("CHERRY")
window.geometry("700x500")
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
def send_message():
    user=input_box.get()
    chat.insert(tk.END,"YOU -> "+user+"\n")
    resp=ask_cherry(user)
    chat.insert(tk.END,"CHERRY -> "+resp+"\n")
    input_box.delete(0,tk.END)
send_button=tk.Button(window,text="SEND",command=send_message)
send_button.pack()
window.mainloop()