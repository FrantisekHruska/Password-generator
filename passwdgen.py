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

        self.passlength = tk.StringVar()

        self.difficulty_chars = tk.IntVar()
        self.difficulty_numbers = tk.IntVar()
        self.difficulty_punctuation = tk.IntVar()

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

        self.lstbox1 = tk.Checkbutton(parent, text="Characters", variable=self.difficulty_chars)
        self.lstbox1.pack(side="left")

        self.lstbox2 = tk.Checkbutton(parent, text="Numbers", variable=self.difficulty_numbers)
        self.lstbox2.pack(side="left")

        self.lstbox3 = tk.Checkbutton(parent, text="Punctuation", variable=self.difficulty_punctuation)
        self.lstbox3.pack(side="left")

        self.txtbox1 = tk.Entry(parent, textvariable=self.passlength).pack(side="right")
        self.lbl2 = tk.Label(parent, text="Length :").pack(side="right")

    def update_password(self):
        diffstr = ""
        if self.difficulty_chars.get() == 1:
            diffstr += st.ascii_letters
        if self.difficulty_numbers.get() == 1:
            diffstr += st.digits
        if self.difficulty_punctuation.get() == 1:
            diffstr += st.punctuation
        try:
            if diffstr == "":
                password = "Select option"
            elif int(self.passlength.get()) > 25 or int(self.passlength.get()) < 1:
                password = "Must be between 1 and 25"
            else:
                password = self.password_gen(list(diffstr), int(self.passlength.get()))
        except ValueError:
            password = "Must be a number"
        self.lbl1.config(text=password)
        self.btn1.config(command=ppc.copy(password))
        self.lbl1.pack(fill="both")
        # print(self.difficulty_chars.get())
        # print(self.difficulty_numbers.get())
        # print(self.difficulty_punctuatiom.get())

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
