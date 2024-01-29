import tkinter
from math import *

window=tkinter.Tk()
window.title("YUN DAE HEE")
window.geometry("640x480+100+100")
window.resizable(False, False)

#def calc():
#    label.config(text="결과="+str(eval(entry.get())))

def click():
    label.config(text="결과="+str(eval(entry.get())))


entry=tkinter.Entry(window)
#entry.bind("<Return>", calc)
entry.pack()

button = tkinter.Button(window, text ="click",overrelief="solid", width=15, command=click)
button.pack()

label=tkinter.Label(window)
label.pack()

window.mainloop()