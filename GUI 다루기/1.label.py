import tkinter
import tkinter.font as tk_font

window=tkinter.Tk() # 객체
window.title("YUN DAE HEE")  # 제목
window.geometry("640x400+100+100") # 사이즈
window.resizable(False, False)  #  가로 세로 크기 수정 불가 

font = tk_font.Font(family="맑은 고딕" , size=20)
label=tkinter.Label(window, text="파이썬", width=10, height=7, fg="red", relief="solid" , font = font)
label.pack()

window.mainloop()