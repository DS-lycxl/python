"""
__author__='李霆宇'
time='2017-3-4'
version='0.0.1'
how_to_use='这个程序可以与机器人聊天。在输入框里输入要发送的内容，CTRL+X发送。'
"""
import requests
from tkinter import *
import sys
root = Tk()
root.title('机器人聊天器')
text = Text(root, height=15, width=60)
text.grid(row=0, column=0, columnspan=2, sticky=W)
e1 = Text(root, height=5, width=70)
e1.grid(row=1, column=0, columnspan=2)
requestnumber = 0
text.insert(INSERT, '使用快捷键“CTRL+X”快速发送信息\n机器人准备就绪\n')
label = Label(root, text='祝 制 机\n您 作 器\n使 者 人\n用 ： AI\n愉 炼 由\n快 狱 图\n |  屮 灵\n降 降 提\n龙 龙 供').grid(
    row=0, column=1, sticky=E)


def chat(event):
    message = e1.get('0.0', END)
    e1.delete('0.0', END)
    global requestnumber
    if requestnumber == 5:
        text.delete('0.0', END)
        requestnumber = 0
    if message != '':
        text.insert(INSERT, '你：{}'.format(message))
        usermessage = message
        formdata = {
            "key": "c782b14e97b347598dde2c7b9d50d6d9",
            "info": usermessage,
            "userid": "123456",
        }
        url = r'http://www.tuling123.com/openapi/api'
        robotmessage = requests.post(url=url, data=formdata)
        robotmessagejson = robotmessage.json()
        text.insert(INSERT, '机器人：{}\n'.format(robotmessagejson['text']))
        requestnumber += 1


Btn = Button(root, text="发送", width=10, command=chat)
Button(root, text="退出", width=60, command=sys.exit).grid(
    row=2, column=0, columnspan=2)
Btn.bind_all('<Control-x>', chat)
mainloop()
