import tkinter
import tkinter.font as tk_font

window=tkinter.Tk()
window.title("test")
window.geometry("600x400+100+100")
window.resizable(False,False) #사이즈 수정 불가

font= tk_font.Font(family="맑은 고딕", size=20)

entry = tkinter.Entry(window , font = font)
entry.grid(row = 0, column=4)
s=""

def 기능(n):
    global s
    s += str(n)
    entry.delete(0 , tkinter.END) #삭제 , 0~ 끝
    entry.insert(0,n) # 넣기 0번째 , 0 을 넣기

def 계산():
    global s
    s = str(eval(s))
    entry.delete(0 , tkinter.END)
    entry.insert(0,s)

for i in range(10):
    b = tkinter.Button(window , text= f"{i}", font = font, command= lambda i=i: 기능(i))
    b.grid(row = i//4+1 , column=i%4)

b = tkinter.Button(window , text= ".", font = font, command= lambda : 기능("."))
b.grid(row =3 , column=2)
b = tkinter.Button(window , text= "-", font = font, command= lambda : 기능("-"))
b.grid(row =4 , column=1)
b = tkinter.Button(window , text= "x", font = font, command= lambda : 기능("x"))
b.grid(row =4 , column=2)
b = tkinter.Button(window , text= "/", font = font, command= lambda : 기능("/"))
b.grid(row =4 , column=3)

결 = tkinter.Button(window , text="=", font = font, command=계산)
결.grid(row=3,column=3)

더 = tkinter.Button(window , text="+", font = font, command=lambda :기능("+"))
더.grid(row = 4 , column=0)


window.mainloop()
