import time
from tkinter import *  # 导入tkinter模块内容

from pykeyboard import PyKeyboard

k = PyKeyboard()

def callback():
    k.tap_key(k.up_key)
    # k.press_key("Up")
    # time.sleep(1)
    # k.release_key("Up")


def callback2():
    k.tap_key(k.down_key)
    # k.press_key("Down")
    # time.sleep(1)
    # k.release_key("Down")

root = Tk()  # 初始框声明

frame1 = Frame(root)  # 声明模块
frame2 = Frame(root)
frame3 = Frame(root)
# 创建一个文本Label对象
var = StringVar()  # 声明可变变量
var.set("WPS助手")

textLabel = Label(frame1,  # 绑定到模块1
                  textvariable=var,  # 文本量变
                  justify=RIGHT,  # 字体位置
                  font=(50),
                  fg='red')
textLabel.pack(side=LEFT)  # 整体位置

imgLabel = Label(frame1)
imgLabel.pack(side=LEFT)
# 加按钮
thebutton = Button(frame2, text='上一页', font=( 35), fg='purple', command=callback)  # 按下按钮执行 函数
thebutton.pack()
thebutton2 = Button(frame3, text='下一页', font=( 35), fg='purple', command=callback2)
thebutton2.pack()
frame1.pack(padx=10, pady=10)
frame2.pack(padx=50, pady=50)
frame3.pack(padx=50, pady=50)

root.mainloop()
