import win32api
import win32con

from tkinter import *

root = Tk()


def fuckyou():
    win32api.keybd_event(17, 0, 0, 0)



Button(root, text='我去你妈的', command=fuckyou).grid(row=0, column=0)
mainloop()
