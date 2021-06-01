import time
from time import ctime
import subprocess
import tkinter
import random as r
from tkinter import PhotoImage
top=tkinter.Tk()
top.geometry('400x400')
var1=tkinter.StringVar()
prev='12'
def cur_time():
    import requests as req
    tot=req.get('http://worldtimeapi.org/api/timezone/Asia/Kolkata.txt').text
    loc=tot.find('2021')
    return tot[loc:loc+10]
print('Current Date: ',cur_time())
def gen():
    import string
    s=''
    for i in range(3):
        s+=r.choice(string.ascii_letters)
        s+=r.choice(string.punctuation)
        s+=r.choice(string.digits)
    return s
pw=gen()
i=PhotoImage(file=r'B:\Python\ML\MiniProjects\RandomPassword\image.png')
print('Password: ',pw)
def verification():
    import os
    global prev
    name=var1.get()
    now=cur_time()
    if(now[-2:]!=prev):
        if name==pw:
            prev=now[-2:]
            p=subprocess.call(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
            time.sleep(20) #after 20 secs automatically app closed
            os.system('taskkill /im firefox.exe /f')
        else:
            print('incorrect')
    else:
        print('try tomorrow')
lab=tkinter.Label(top,text='AppLock',font=("Arial", 25)).pack(pady=10)
text=tkinter.Entry(top,textvariable=var1,bd=5,width=30).pack(pady=10)
B=tkinter.Button(top,image=i,command=verification,activebackground='red',bg='light green',fg='black').pack(pady=10)
top.mainloop()
