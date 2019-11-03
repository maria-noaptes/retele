import pickle
from random import random
from tkinter import *
import socket
from packets import *
from threading import Thread
import requests

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
import json
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

        self.back = Frame(master=self.root, width=700, height=500, bg='blue')
        self.back.pack()
        self.choices = ("News", "Weather")
        self.checklist = ChecklistBox(self.back, self.choices, bd=1, relief="sunken", background="white")
        self.checklist.pack()
        self.buttonSubcribe = Button(self.back, text='Subscribe', command=self.subscribe)
        self.buttonSubcribe.pack()

        self.buttonMessage = Button(self.back, text='New Message', command=self.message)
        self.buttonMessage.pack()

        self.root.mainloop()

    def message(self):
        self.newMessage = NewMessage()
    def subscribe(self):
        p=SUBSCRIBE(1,'weather/temperature/Yassi')
        p1=pickle.dumps(p)
        s.send(p1)
        data=s.recv(1024)
        data1=pickle.loads(data)
        if type(data1)==SUBPACK:
            print('subscribed')
        data2=s.recv(1024)
        data3 = pickle.loads(data2)
        print(data3)
class NewMessage:
    def __init__(self):
        self.root = Tk()
        self.root.title('New Message')      #connect, subscribe, publish, pingreq, unsubscribe
        self.back = Frame(master=self.root, width=500, height=500, bg='white')
        self.back.pack()
        self.entryMessage = Entry(self.back, width=40)
        self.entryMessage.grid(row=0, column=0)
        self.labelTopics = Label(self.back, text='Topics')
        self.labelTopics.grid(row=1, column=0)
        self.choices = [("News", 1),
                        ("Weather", 2)
                        ]
        self.v = IntVar()
        self.v.set(1)
        for topic, number in self.choices:
            self.b = Radiobutton(self.back, text=topic, variable=self.v, value=number)
            self.b.grid(row=number+1, column=0)


        self.buttonApi = Button(self.back, text='Generate temperature', command=self.getTemp)
        self.buttonApi.grid(row=0, column=1)
        self.buttonSend = Button(self.back, text='Send', command=self.send)
        self.buttonSend.grid(row=1, column=1)
        self.root.mainloop()


    def getTemp(self):
        response = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Iasi,ro&units=metric&appid=ac7c75b9937a495021393024d0a90c44')

        json_data = response.json()
        if json_data:
            if 'main' in json_data:
                json_data = json_data.get('main')
                temp = json_data.get('temp')
                self.entryMessage.insert(100, 'Temperatura curenta este ' + str(temp));

    def send(self):
        p=PUBLISH('weather/temperature/Yassi',self.entryMessage.get())
        p1=pickle.dumps(p)
        s.send(p1)
        pass

class Login:
    def __init__(self):
        self.root = Tk()
        self.root.title('Sign in')

        self.labelUser = Label(self.root, text="User ")
        self.labelUser.grid(row=0, column=0)

        self.entryUser = Entry(self.root)
        self.entryUser.insert(10, "Maria")
        self.entryPassword.insert(4,"1234");
        self.entryUser.grid(row=0, column=1)

        self.labelPassword = Label(self.root, text="Password ")
        self.labelPassword.grid(row=1, column=0)

        self.entryPassword = Entry(self.root)
        self.entryPassword.grid(row=1, column=1)

        self.buttonOk = Button(self.root, text='OK', command=self.connect)
        self.buttonOk.grid(row=3, column=3)

        self.root.mainloop()


    def connect(self):
        s.connect(('127.0.0.1',5000))

        packet=CONNECT(random()*10,self.entryUser.get(),self.entryPassword.get())
        p=pickle.dumps(packet)
        s.sendall(p)
        msg = s.recv(1024)
        msg1=pickle.loads(msg)
        if type(msg1) == CONNACK and msg1.flag_confirmare==1:
            print('m-am logat cu succes')
            self.topics = Topics()



login = Login()

