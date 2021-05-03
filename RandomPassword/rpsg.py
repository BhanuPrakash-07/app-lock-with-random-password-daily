import time
from time import ctime
import subprocess
import tkinter
import random as r
from tkinter import PhotoImage
top=tkinter.Tk()
top.geometry('400x400')
var1=tkinter.StringVar()
prev='02'
def cur_time():
    import requests as req
    return req.get('http://worldtimeapi.org/api/timezone/Asia/Kolkata.txt').text[53:72]
print(cur_time())
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
print(pw)
def verification():
    import os
    global prev
    name=var1.get()
    now=cur_time()
    if(now[8:10]!=prev):
        if name==pw:
            p=subprocess.call(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
            time.sleep(10)
            os.system('taskkill /im firefox.exe /f')
            prev=now[8:10]
        else:
            print('incorrect')
    else:
        print('try tomorrow')
lab=tkinter.Label(top,text='AppLock',font=("Arial", 25)).pack(pady=10)
text=tkinter.Entry(top,textvariable=var1,bd=5,width=30).pack(pady=10)
B=tkinter.Button(top,image=i,command=verification,activebackground='red',bg='light green',fg='black').pack(pady=10)
top.mainloop()
