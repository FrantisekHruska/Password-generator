import random
import string as st
import tkinter as tk


class MainWindow(tk.Tk):
    def __init__(self, screenName=None, baseName=None, className='Tk', useTk=1, sync=0, use=None):
        super().__init__(screenName=screenName,
                         baseName=baseName, useTk=useTk, sync=sync, use=use)
        WIDTH = 130
        HEIGHT = 500
        self.title('Password Generator')
        self.minsize(HEIGHT, WIDTH)
        self.maxsize(HEIGHT, WIDTH)
        self.configure(bg='black')


def passwdgen(passlength=int(
    input("How many characters do you want your password to have? \n")
)):

    passwd = ''
    chars = list(st.ascii_letters+st.digits)

    for i in range(passlength):
        passwd += chars[random.randint(0, len(chars)-1)]

    return passwd


def create_labels(master=None):
    label_1 = tk.Label(master=master, font=(
        'Calibri', 40, 'bold'), bg='black', fg='green')
    label_1.place(x=25, y=25)
    label_1.config(text=passwdgen())
    # print(time.strftime('%H:%M:%S'))
    #label_1.after(1000, create_labels)


def main():
    root = MainWindow()
    create_labels(root)
    root.mainloop()


if __name__ == "__main__":
    main()
