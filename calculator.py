import tkinter as tk
from math import sqrt, factorial

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "√":
        entry.insert(tk.END, "sqrt(")
    elif text == "!":
        entry.insert(tk.END, "!")
    elif text == "⌫":  # Clear (backspace) button
        entry.delete(len(entry.get()) - 1)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.configure(bg="#f0f0f0")

entry = tk.Entry(root, font=("Arial", 24), bd=5, relief=tk.GROOVE, justify=tk.RIGHT)
entry.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

buttons_frame = tk.Frame(root, bg="#f0f0f0")
buttons_frame.pack(fill=tk.BOTH, expand=True)

button_text = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C", "√", "!", "⌫"  # Added factorial and clear (backspace) buttons
]

for i, text in enumerate(button_text):
    btn = tk.Button(buttons_frame, text=text, font=("Arial", 20), relief=tk.GROOVE, padx=20, pady=20)
    btn.grid(row=i // 4, column=i % 4, sticky=tk.NSEW)
    btn.bind("<Button-1>", on_click)

buttons_frame.grid_columnconfigure(0, weight=1)
buttons_frame.grid_columnconfigure(1, weight=1)
buttons_frame.grid_columnconfigure(2, weight=1)
buttons_frame.grid_columnconfigure(3, weight=1)

buttons_frame.grid_rowconfigure(0, weight=1)
buttons_frame.grid_rowconfigure(1, weight=1)
buttons_frame.grid_rowconfigure(2, weight=1)
buttons_frame.grid_rowconfigure(3, weight=1)
buttons_frame.grid_rowconfigure(4, weight=1)

root.mainloop()
