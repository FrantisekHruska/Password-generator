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

        self.difficulty_chars = tk.IntVar()
        self.difficulty_numbers = tk.IntVar()
        self.difficulty_punctuatiom = tk.IntVar()

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

        self.lstbox3 = tk.Checkbutton(parent, text="Punctuation", variable=self.difficulty_punctuatiom)
        self.lstbox3.pack(side="left")

    def update_password(self):
        password = self.password_gen(list(st.digits + st.ascii_letters + st.punctuation))
        self.lbl1.config(text=password)
        self.btn1.config(command=ppc.copy(password))
        self.lbl1.pack(fill="both")
        # print(self.difficulty_chars.get())
        # print(self.difficulty_numbers.get())
        # print(self.difficulty_punctuatiom.get())


    @staticmethod
    def password_gen(chars):
        password_str = ''

        # chars = list(st.printable)

        for i in range(20):
            password_str += chars[random.randint(0, len(chars) - 1)]

        return password_str


if __name__ == "__main__":
    root = MainWindow()
    app = MainApplication(root)
    root.mainloop()
