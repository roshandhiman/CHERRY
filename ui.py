import tkinter as tk
window=tk.Tk()
window.title("CHERRY")
window.geometry("700x500")
window.configure(bg="black")
# window.mainloop()
chat=tk.Text(
    window,
    bg="black",
    fg="white",
    font=("Arial",14)
)
chat.pack(
    padx=20,pady=20,fill="both",expand=True
)
window.mainloop()