import tkinter
import tkinter.font as tk_font
from math import *
window=tkinter.Tk() # 객체
window.title("YUN DAE HEE")  # 제목
window.geometry("720x480+100+100") # 사이즈
window.resizable(False, False)  #  가로 세로 크기 수정 불가 
font = tk_font.Font(family="궁서" , size=10)

# 엔트리 하나 
entry=tkinter.Entry(window , font = font,width=120)
entry.pack()

# 엔트리에 적힌 내용이 그대로 버튼을 누르면 라벨에 표시가 되도록하기 
def 가져오기():
    label.config(text=str(entry.get()))

# 버튼 
button = tkinter.Button(window, text ="가져오기",overrelief="solid", width=15, command=가져오기)
button.pack()

# 라벨 하나
label=tkinter.Label(window, text="결과", width=30, height=7, fg="red", relief="solid" , font = font)
label.pack()





window.mainloop()