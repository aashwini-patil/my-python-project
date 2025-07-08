from tkinter import *

window = Tk()
window.title("Calculator")
window.geometry("500x500")
# Entry widget for input
e = Entry(window, width = 52 , borderwidth= 5)
e.place(x=0,y=0)
# Button widget
def click(num):
    current = e.get()
    e.delete(0, END)  # Clear the entry field
    e.insert(0, str(current) + str(num))  # Insert the new number   
b = Button(window, text='1',width=12, command=lambda:click('1'))
b.place(x=5,y=60)

b = Button(window, text='2',width=12, command=lambda:click('2'))
b.place(x=80,y=60)

b = Button(window, text='3',width=12, command=lambda:click('3'))
b.place(x=170,y=60)

b = Button(window, text='4',width=12, command=lambda:click('4'))
b.place(x=5,y=120)

b = Button(window, text='5',width=12, command=lambda:click('5'))
b.place(x=80,y=120)

b = Button(window, text='6',width=12, command=lambda:click('6'))
b.place(x=170,y=120)

b = Button(window, text='7',width=12, command=lambda:click('7'))
b.place(x=5,y=180)  

b = Button(window, text='8',width=12, command=lambda:click('8'))
b.place(x=80,y=180)

b = Button(window, text='9',width=12, command=lambda:click('9'))
b.place(x=170,y=180)

b = Button(window, text='0',width=12, command=lambda:click('0'))
b.place(x=5,y=240)

# OPERATION BUTTONS
def add():
    n1 = e.get()
    global math 
    math = 'addition'
    global i 
    i = int(n1)
    e.delete(0, END)


b = Button(window, text='+',width=12, command=add)
b.place(x=80,y=240)

def subtract():
    n1 = e.get()
    global math 
    math = 'subtraction'
    global i 
    i = int(n1)
    e.delete(0, END)

b = Button(window, text='-',width=12, command=subtract)
b.place(x=170,y=240)

def multiply():
    n1 = e.get()
    global math 
    math = 'multiplication'
    global i 
    i = int(n1)
    e.delete(0, END)

b = Button(window, text='*',width=12, command=multiply)
b.place(x=5,y=300)

def divide():
    n1 = e.get()
    global math 
    math = 'division'
    global i 
    i = int(n1)
    e.delete(0, END)

b = Button(window, text='/',width=12, command=divide)
b.place(x=80,y=300)

def euqal():
    n2 = e.get()
    e.delete(0, END)
    if math == 'addition':
        e.insert(0, i + int(n2))
    elif math == 'subtraction':
        e.insert(0, i - int(n2))
    elif math == 'multiplication':
        e.insert(0, i * int(n2))
    elif math == 'division':
        e.insert(0, i / int(n2))

b = Button(window, text='=',width=12, command=euqal)
b.place(x=170,y=300)

b = Button(window, text='Clear',width=12, command=lambda: e.delete(0, END))
b.place(x=5,y=360)

mainloop()