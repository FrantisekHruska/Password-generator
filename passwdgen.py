import random
import string as st
import tkinter as tk
import pyperclip as ppc


class MainWindow(tk.Tk):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.geometry('500x150')
        self.resizable(False, False)
        self.config(bg='white')
        self.title("Password generator")


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super(MainApplication, self).__init__()
        self.parent = parent
        self.pack(side="top", fill="both", expand=True)
        self.configure(bg='lightgreen')

        self.lbl_1 = tk.Label(parent, text=None, font=(
            'Calibri', 25, 'bold'), bg='white')

        self.lbl_1.pack(fill="both")

        self.btn3 = tk.Button(parent, text='Exit', command=parent.destroy, bg='lightgreen')
        self.btn3.pack(side="bottom", fill='x')

        self.btn1 = tk.Button(parent)
        self.btn1.config(text="Copy", bg='lightgreen')
        self.btn1.pack(side="bottom", fill='x')

        self.btn2 = tk.Button(parent, text="Generate", command=self.update_password, bg='lightgreen')
        self.btn2.pack(side="bottom", fill='x')

    def update_password(self):
        password = self.password_gen()
        self.lbl_1.config(text=password)
        self.btn1.config(command=ppc.copy(password))
        self.lbl_1.pack(fill="both")

    @staticmethod
    def password_gen():
        password_str = ''
        chars = list(st.ascii_letters + st.digits)
        # chars = list(st.printable)

        for i in range(20):
            password_str += chars[random.randint(0, len(chars) - 1)]

        return password_str


if __name__ == "__main__":
    root = MainWindow()
    app = MainApplication(root)
    root.mainloop()
