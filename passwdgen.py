import random
import string as st
import tkinter as tk
import pyperclip as ppc


class MainWindow(tk.Tk):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.minsize(width=580, height=100)
        self.maxsize(width=600, height=100)
        self.config(bg='white')
        self.title("Password generator")


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super(MainApplication, self).__init__()
        self.parent = parent
        self.pack(side="top", fill="both", expand=True)
        self.configure(bg='white')
        self.lbl1 = tk.Label(parent, text=password, font=(
            'Calibri', 25, 'bold'), bg='white')
        self.lbl1.pack(fill="both")
        self.btn1 = tk.Button(parent, command=ppc.copy(password))
        self.btn1.config(text="Copy", bg='white')
        self.btn1.pack(side="bottom")


def password_gen():
    password_str = ''
    chars = list(st.ascii_letters + st.digits)

    for i in range(20):
        password_str += chars[random.randint(0, len(chars) - 1)]

    return password_str


if __name__ == "__main__":
    root = MainWindow()
    password = password_gen()
    app = MainApplication(root)
    root.mainloop()
