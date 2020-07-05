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

        self.lbl_1 = tk.Label(parent, text=None, font=(
            'Calibri', 25, 'bold'), bg='white')

        self.lbl_1.pack(fill="both")

        self.btn2 = tk.Button(parent, text="Generate", command=self.update_password, bg='white')
        self.btn2.pack(side="bottom")

        self.btn1 = tk.Button(parent)
        self.btn1.config(text="Copy", bg='white')
        self.btn1.pack(side="bottom")

    def update_password(self):
        password_local = self.password_gen()
        self.lbl_1.config(text=password_local)
        self.btn1.config(command=ppc.copy(password_local))
        self.lbl_1.pack(fill="both")

    @staticmethod
    def password_gen():
        password_str = ''
        chars = list(st.ascii_letters + st.digits)

        for i in range(20):
            password_str += chars[random.randint(0, len(chars) - 1)]

        return password_str



if __name__ == "__main__":
    root = MainWindow()
    app = MainApplication(root)
    root.mainloop()
