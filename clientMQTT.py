from tkinter import *

class ChecklistBox(Frame):
    def __init__(self, parent, choices, **kwargs):
        Frame.__init__(self, parent, **kwargs)

        self.vars = []
        bg = self.cget("background")
        for choice in choices:
            var = StringVar(value=choice)
            self.vars.append(var)
            cb = Checkbutton(self, var=var, text=choice, onvalue=choice, offvalue="",
                             anchor="w", width=20, background=bg, relief="flat", highlightthickness=0)
            cb.pack(side="top", fill="x", anchor="w")

    def getCheckedItems(self):
        values = []
        for var in self.vars:
            value = var.get()
            if value:
                values.append(value)
        return values


class Topics:
    def __init__(self):
        self.root = Tk()
        self.root.title('Subscribed Topics')
        self.back = Frame(master=self.root, width=500, height=500, bg='white')
        self.back.pack()
        self.choices = ("News", "Weather")
        self.checklist = ChecklistBox(self.back, self.choices, bd=1, relief="sunken", background="white")
        self.checklist.pack()
        print("choices:", self.checklist.getCheckedItems())

        self.buttonMessage = Button(self.back, text='New Message', command=self.message)
        self.buttonMessage.pack()

        self.root.mainloop()

    def message(self):
        self.newMessage = NewMessage()
        #self.root.destroy()


class NewMessage:
    def __init__(self):
        self.root = Tk()
        self.root.title('New Message')
        self.back = Frame(master=self.root, width=500, height=500, bg='white')
        self.back.pack()
        self.entryMessage = Entry(self.back)
        self.entryMessage.grid(row=0, column=0)
        self.root.mainloop()


class Login:
    def __init__(self):
        self.root = Tk()
        self.root.title('Sign in')

        self.labelUser = Label(self.root, text="User ")
        self.labelUser.grid(row=0, column=0)

        self.entryUser = Entry(self.root)
        self.entryUser.insert(10, "Maria")
        self.entryUser.grid(row=0, column=1)

        self.labelPassword = Label(self.root, text="Password ")
        self.labelPassword.grid(row=1, column=0)

        self.entryPassword = Entry(self.root)
        self.entryPassword.grid(row=1, column=1)

        self.buttonOk = Button(self.root, text='OK', command=self.connect)
        self.buttonOk.grid(row=3, column=3)

        self.root.mainloop()
        #self.root.destroy()

    def connect(self):
        self.topics = Topics()
        #self.root.destroy()
'''back = tk.Frame(root, width=500, height=500, bg='white')
back.pack()'''

login = Login()

