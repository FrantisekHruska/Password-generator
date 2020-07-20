import random
import string as st
import tkinter as tk
from tkinter import messagebox
import pyperclip as ppc


class MainWindow(tk.Tk):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.geometry('620x80')
        self.resizable(False, False)
        self.config(bg='white')
        self.title("Password generator")


class MainApplication(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        super(MainApplication, self).__init__()
        # self.parent = parent
        self.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.config(bg='white')

        self.passlength = tk.IntVar(parent, value=20)

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

        self.lbl_2 = tk.Label(parent, textvariable=self.passlength, width=2, height=2).pack(side=tk.LEFT)
        # self.lbl2 = tk.Label(parent, text="Length :").pack(side="right")

        self.slider_1 = tk.Scale(parent, from_=5, to=25, orient=tk.HORIZONTAL, length=85, width=20,
                                 variable=self.passlength, sliderlength=10, bd=0, showvalue=False).pack(side=tk.RIGHT)

    def update_password(self):
        diffstr = ''

        if self.difficulty_chars.get():
            diffstr += st.ascii_letters
        if self.difficulty_numbers.get():
            diffstr += st.digits
        if self.difficulty_punctuation.get():
            diffstr += st.punctuation

        try:
            password = self.password_gen(list(diffstr), int(self.passlength.get()))
            self.lbl_1.config(text=password)
            self.btn_1.config(command=ppc.copy(password))
        except ValueError:
            self.difficulty_chars.set(True)
            messagebox.showerror(title='Error', message="Check at least one checkbox")

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
