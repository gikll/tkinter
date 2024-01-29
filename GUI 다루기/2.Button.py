import tkinter

window=tkinter.Tk()
window.title("YUN DAE HEE")
window.geometry("640x400+100+100")
window.resizable(False, False)

count=0

def countUP():
    global count
    count +=1
    label.config(text=str(count)) # 

def countDown():
    global count
    count -=1
    label.config(text=str(count))

label = tkinter.Label(window, text="0")
label.pack()

button = tkinter.Button(window, text ="up",overrelief="solid", width=15, command=countUP, repeatdelay=1000, repeatinterval=100)
button.pack()

button2 = tkinter.Button(window, text ="down",overrelief="solid", width=15, command=countDown, repeatdelay=1000, repeatinterval=100)
button2.pack()

window.mainloop()