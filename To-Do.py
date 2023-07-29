import tkinter as tk
from tkinter import messagebox

def newTask():
    task = my_entry.get()
    if task:
        lb.insert(tk.END, task)
        my_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("warning", "Please enter some task.")

def deleteTask():
    lb.delete(tk.ANCHOR)

ws = tk.Tk()
ws.geometry('500x450+500+200')
ws.title('1st Internship Project')
ws.config(bg='#223441')
ws.resizable(width=False, height=False)

lb = tk.Listbox(ws, width=25, height=8, font=('Times', 18), bd=0, fg='#464646', highlightthickness=0, selectbackground='#a6a6a6', activestyle="none")
lb.pack(pady=10)

sb = tk.Scrollbar(ws, command=lb.yview)
sb.pack(side=tk.RIGHT, fill=tk.Y)
lb.config(yscrollcommand=sb.set)

my_entry = tk.Entry(ws, font=('times', 24))
my_entry.pack(pady=20)

button_frame = tk.Frame(ws)
button_frame.pack(pady=20)

btn_params = [
    ('Add Task', '#c5f776', newTask),
    ('Delete Task', '#ff8b61', deleteTask)
]

for text, bg, command in btn_params:
    btn = tk.Button(button_frame, text=text, font=('times 14'), bg=bg, padx=20, pady=10, command=command)
    btn.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

ws.mainloop()
