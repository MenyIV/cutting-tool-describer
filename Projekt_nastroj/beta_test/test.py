import tkinter
from tkinter import Tk, Toplevel
from tkinter import *


def main():
    main_window = Tk()
    app = first(main_window)
    main_window.mainloop()


class first:
    def __init__(self, root):
        self.root = root
        self.root.title('First window')
        self.root.geometry('1350x700+0+0')

        single_id = Label(self.root, text="Enter id", font=("Times New Roman", 14), bg='white',
                          fg='black')
        single_id.place(x=200, y=200)

        self.mystring = tkinter.StringVar(self.root)

        self.txt_id = Entry(self.root, textvariable=self.mystring, font=("Times New Roman", 14), bg='white')
        self.txt_id.place(x=300, y=200, width=280)
        btn_search = Button(self.root, command=self.second_window, font=("Times New Roman", 15, 'bold'), text='Get Id')
        btn_search.place(x=300, y=400, width=220, height=35)

    def second_window(self):
        self.root.destroy()
        main_window = Tk()
        app = second(main_window, self)
        main_window.mainloop()

    def return_id(self):
        return self.mystring.get()


class second:
    def __init__(self, root, first):
        self.root = root
        self.root.title('Second window')
        self.root.geometry('1350x700+0+0')
        id = first.return_id()

        get_id = Label(self.root, text=id, font=("Times New Roman", 14), bg='white',
                       fg='black')
        get_id.place(x=200, y=350)


if __name__ == '__main__':
    main()