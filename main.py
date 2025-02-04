import random
import string as st
import tkinter as tk
from tkinter import messagebox
from sys import platform
import pyperclip as ppc


class MainWindow(tk.Tk):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.geometry('700x80')
        self.resizable(False, False)
        self.config(bg='white')
        self.title("Password generator")

        if platform == 'win32':
            self.iconbitmap('./img/key.ico')
            self.geometry('620x80')


class MainApplication(tk.Frame):

    def __init__(self, parent):
        super(MainApplication, self).__init__()

        self.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.config(bg='white')

        self.password_length = tk.IntVar(parent, value=20)

        self.difficulty_chars = tk.BooleanVar(parent, value=True)
        self.difficulty_numbers = tk.BooleanVar(parent, value=True)
        self.difficulty_punctuation = tk.BooleanVar(parent)

        self.lbl_1 = tk.Label(parent, text=None, font=(
            'Helvetica', 30), bg='white')

        self.lbl_1.pack(side=tk.TOP)

        self.btn_3 = tk.Button(parent, text='Exit', command=parent.destroy, bg='lightgreen', width=10)
        self.btn_3.pack(side=tk.LEFT)

        self.btn_1 = tk.Button(parent)
        self.btn_1.config(text="Copy", bg='lightgreen', width=10)
        self.btn_1.pack(side=tk.LEFT)

        self.btn_2 = tk.Button(parent, text="Generate", command=self.update_password, bg='lightgreen', width=10)
        self.btn_2.pack(side=tk.LEFT)

        self.checkbox_1 = tk.Checkbutton(parent, text="Characters", variable=self.difficulty_chars)
        self.checkbox_1.pack(side=tk.LEFT)

        self.checkbox_2 = tk.Checkbutton(parent, text="Numbers", variable=self.difficulty_numbers)
        self.checkbox_2.pack(side=tk.LEFT)

        self.checkbox_3 = tk.Checkbutton(parent, text="Punctuation", variable=self.difficulty_punctuation)
        self.checkbox_3.pack(side=tk.LEFT)

        self.lbl_2 = tk.Label(parent, textvariable=self.password_length, width=2, height=2).pack(side=tk.RIGHT)
        # self.lbl2 = tk.Label(parent, text="Length :").pack(side="right")

        self.slider_1 = tk.Scale(parent, from_=5, to=25, orient=tk.HORIZONTAL, length=85, width=20,
                                 variable=self.password_length, sliderlength=10, bd=0, showvalue=False).pack(
            side=tk.RIGHT)
        # self.update_password()

    def update_password(self):
        try:
            password = self.password_gen(self.set_difficulty(), int(self.password_length.get()))
            self.lbl_1.config(text=password)
            self.btn_1.config(command=ppc.copy(password))
        except ValueError:
            self.difficulty_chars.set(True)
            messagebox.showerror(title='Error', message="Tick at least one checkbox")

    def set_difficulty(self):
        password_difficulty = ''
        if self.difficulty_chars.get():
            password_difficulty += st.ascii_letters
        if self.difficulty_numbers.get():
            password_difficulty += st.digits
        if self.difficulty_punctuation.get():
            password_difficulty += st.punctuation
        return list(password_difficulty)

    @staticmethod
    def password_gen(chars, length):
        password_str = ''
        for i in range(length):
            password_str += chars[random.randint(0, len(chars) - 1)]
        return password_str


if __name__ == "__main__":
    root = MainWindow()
    app = MainApplication(root)
    root.mainloop()
