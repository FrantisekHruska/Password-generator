import random
import string as st
import tkinter as tk


class MainWindow(tk.Tk):
    def __init__(self, screenName=None, baseName=None, className='Tk', useTk=1, sync=0, use=None):
        super().__init__(screenName=screenName,
                         baseName=baseName, useTk=useTk, sync=sync, use=use)
        WIDTH = 620
        HEIGHT = 130
        self.title('Password Generator')
        self.minsize(WIDTH, HEIGHT)
        self.maxsize(WIDTH, HEIGHT)
        self.configure(bg='black')


def passwdgen(length):

    passwd = ''
    chars = list(st.ascii_letters+st.digits)

    for i in range(length):
        passwd += chars[random.randint(0, len(chars)-1)]

    return passwd


def create_widgets(master=None, passwordgenerator=None):
    label_1 = tk.Label(master=master, font=(
        'Calibri', 40, 'bold'), bg='black', fg='green')
    label_1.place(x=25, y=25)
    label_1.config(text=passwordgenerator)
    # print(time.strftime('%H:%M:%S'))
    #label_1.after(1000, create_labels)


def main():
    passlength = int(
        input("How many characters do you want your password to have? \n"))
    root = MainWindow()
    create_widgets(root, passwdgen(passlength))
    root.mainloop()


if __name__ == "__main__":
    main()
