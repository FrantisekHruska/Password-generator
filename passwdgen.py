import random
import string as st
import tkinter as tk
from tkinter import messagebox
import pyperclip as ppc


class MainWindow(tk.Tk):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.geometry('800x150')
        self.resizable(False, False)
        self.config(bg='white')
        self.title("Password generator")


class MainApplication(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        super(MainApplication, self).__init__()
        self.parent = parent
        self.pack(side="top", fill="both", expand=True)
        self.configure(bg='lightgreen')

        self.passlength = tk.IntVar(parent, value=20)

        self.difficulty_chars = tk.BooleanVar(parent, value=True)
        self.difficulty_numbers = tk.BooleanVar(parent, value=True)
        self.difficulty_punctuation = tk.BooleanVar(parent)

        self.lbl1 = tk.Label(parent, text=None, font=(
            'Calibri', 25, 'bold'), bg='white')

        self.lbl1.pack(fill="both")

        self.btn3 = tk.Button(parent, text='Exit', command=parent.destroy, bg='lightgreen')
        self.btn3.pack(side="bottom", fill='x')

        self.btn1 = tk.Button(parent)
        self.btn1.config(text="Copy", bg='lightgreen')
        self.btn1.pack(side="bottom", fill='x')

        self.btn2 = tk.Button(parent, text="Generate", command=self.update_password, bg='lightgreen')
        self.btn2.pack(side="bottom", fill='x')

        self.checkbox_1 = tk.Checkbutton(parent, text="Characters", variable=self.difficulty_chars)
        self.checkbox_1.pack(side="left")

        self.checkbox_2 = tk.Checkbutton(parent, text="Numbers", variable=self.difficulty_numbers)
        self.checkbox_2.pack(side="left")

        self.checkbox_3 = tk.Checkbutton(parent, text="Punctuation", variable=self.difficulty_punctuation)
        self.checkbox_3.pack(side="left")

        self.textbox_1 = tk.Entry(parent, textvariable=self.passlength).pack(side="right")
        self.lbl2 = tk.Label(parent, text="Length :").pack(side="right")

    def update_password(self):
        try:

            diffstr = ''
            if not self.difficulty_chars.get() and not self.difficulty_numbers.get() and not self.difficulty_punctuation.get():
                self.difficulty_chars.set(True)
                messagebox.showerror(title='Error', message="Check atleast one checkbox")

            if self.difficulty_chars.get():
                diffstr += st.ascii_letters
            if self.difficulty_numbers.get():
                diffstr += st.digits
            if self.difficulty_punctuation.get():
                diffstr += st.punctuation

            if self.passlength.get() < 1:
                self.passlength.set(1)
            if self.passlength.get() > 25:
                self.passlength.set(25)
            else:
                password = self.password_gen(list(diffstr), int(self.passlength.get()))

            self.lbl1.config(text=password)
            self.btn1.config(command=ppc.copy(password))
            self.lbl1.pack(fill="both")
        except ValueError:
            pass

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
