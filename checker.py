from Tkinter import *
from tkFileDialog import askopenfilename
from urllib import *
import sys

available = []

def dialogbox():
       
    try:
        filename = askopenfilename()
        filePath.insert(0, str(filename))
        txt = open(filename)
        
        for i in txt:
            check(site.get(), i)
            
        for line in available:
            list.insert(END, line)

        if len(available) == 0:
            list.insert(END, "No available usernames :(" )
        txt.close()
        
    except:
        pass


def entered(event):
    
    try:
        for i in open(filePath.get()):
            check(site.get(), i)
        for line in available:
            list.insert(END, line)

        if len(available) == 0:
            list.insert(END, "No available usernames :(" )
        txt.close()
    except:
        pass
    

def check(button_value, username):
    
    url = StringVar()
    if button_value == 1:
        url = "http://www.facebook.com/"
    elif button_value == 2:
        url = "http://www.twitter.com/"
    elif button_value == 3:
        url = "http://www.instagram.com/"
           
    og = url + username
    og_name = (urlopen(og)).getcode()
        
    if og_name == 404:
        available.append(username)
        
    else:
        pass
   
app = Tk()
app.geometry("350x400")
app.title('OG Checker')


frame1 = Frame(app,  height=200 )
frame1.place(x=5, y=150)

scroll = Scrollbar(frame1)
scroll.pack(side=RIGHT, fill=Y)

txtVar = StringVar()
statusLabel = Label(app, textvariable=txtVar).place(x=120, y=40)

filePath = Entry(app, width=30)
filePath.bind('<Return>', entered)
filePath.place(x=50, y=60)

button1 = Button(app, text="Browse", command=dialogbox)
button1.place(x=240, y=57)

list = Listbox(frame1,width=53, height= 15, yscrollcommand=scroll.set)
list.pack()

site = IntVar()
fb = Radiobutton(app, text="Facebook", variable=site, value=1).place(x=5, y=120)
twit = Radiobutton(app, text="Twitter", variable=site, value=2).place(x=130, y=120)
ig = Radiobutton(app, text="Instagram", variable=site, value=3).place(x=250, y=120)

scroll.config(command=list.yview)
app.mainloop()



