import re
import urllib.request
import os
from tkinter import *
import tkinter.messagebox
import tkinter
import urllib.parse
import threading
import sys
# response=urllib.request.urlopen("https://www.readnovel.com/book/25486493000600701#Catalog")
# html=response.read().decode("utf-8")
# f=r'<a href="//(.*?)" target="_blank" data-cid=".*?" title="首发时间：.*?章节字数：.*?">(.*?)</a>'
# urllist=re.findall(f,html)
# try:
#     os.mkdir("下载成功后到这里查看")
# except:
#     pass
# os.chdir('下载成功后到这里查看')
# for each in range(50):
#     print('小说',urllist[each][1],'正在下载')
#     response=urllib.request.urlopen("http://"+urllist[each][0])
#     html=response.read().decode("utf-8")
#     fn=r"""
#         <div class="read-content j_readContent">
#             (.*?)
#         </div>
#         """
#     n=re.findall(fn,html)
#     n=str(n[0]).replace('<p>',' ')
#     with open('%s.txt'%urllist[each][1],'w')as f:
#         f.write(n)
#     print('小说',urllist[each][1],'下载完成')
#     if each==49:
#         print("下载完成！请在程序根目录下的文件夹查看！")
root=Tk()
root.title("批量下载小说")
Label(root, text="min章").grid(row=0)
Label(root, text="max章").grid(row=1,pady=0)
Label(root, text="小说目录").grid(row=2,pady=0)
photo=PhotoImage(file='Logo.png')
imgLabel=Label(root,image=photo)
imgLabel.grid(row=1, column=2, padx=10, pady=0)
e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
e1.grid(row=0, column=1, padx=10,pady=0)
e2.grid(row=1, column=1, padx=10,pady=0)
e3.grid(row=2, column=1, padx=10,pady=0)
def thread2_get():
    response = urllib.request.Request(str(e3.get()))
    response.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")
    response.add_header("Referer","https://www.baidu.com")
    response=urllib.request.urlopen(response)
    html = response.read().decode('utf-8')
    f =r'<a href="//(read.qidian.com/chapter/.*?)" target="_blank" data-eid=".*?" data-cid=".*?" title="首发时间：.*? 章节字数：.*?">(.*?)</a>'
    urllist = re.findall(f, html)
    for each in range(int(e1.get())-1,int(e2.get()),2):
        print('{}正在下载'.format(urllist[each][1]))
        if urllist==[]:
            tkinter.messagebox.showerror('错误','获取数据错误')
            break
        response = urllib.request.urlopen("http://" + urllist[each][0])
        html = response.read().decode("utf-8")
        fn = r'<div class="read-content j_readContent">([\s\S]*?)</div>'
        n = re.findall(fn, html)
        n = str(n[0]).replace('<p>', '\n')#n=n[0].replace('<p>','\n')不行
        with open('{}.txt'.format(urllist[each][1]), 'w')as f:#str(open(urllist[each][1]))+'.txt')也可以
            f.write(str(n))
            f.close()
            print('{}下载完成'.format(urllist[each][1]))
def thread1_get():
    response = urllib.request.urlopen(str(e3.get()))
    html = response.read().decode("utf-8")
    f =r'<a href="//(read.qidian.com/chapter/.*?)" target="_blank" data-eid=".*?" data-cid=".*?" title="首发时间：.*? 章节字数：.*?">(.*?)</a>'
    urllist = re.findall(f, html)
    for each in range(int(e1.get()), int(e2.get()),2):
        print('{}正在下载'.format(urllist[each][1]))
        if urllist==[]:
            tkinter.messagebox.showerror('错误','获取数据错误')
            break
        response = urllib.request.urlopen("http://" + urllist[each][0])
        html = response.read().decode("utf-8")
        fn = r'<div class="read-content j_readContent">([\s\S]*?)</div>'
        n = re.findall(fn, html)
        n = str(n[0]).replace('<p>', '\n')  # n=n[0].replace('<p>','\n')不行
        with open('{}.txt'.format(urllist[each][1]), 'w')as f:
            f.write(str(n))
            f.close()
            print('{}下载完成'.format(urllist[each][1]))
def main():
    response = urllib.request.urlopen(str(e3.get()))
    html = response.read().decode('utf-8')
    f = r'''<em>(.*?)</em>'''
    title = re.findall(f, html)
    print(sys.path[0])
    try:
        os.mkdir(title[0])
        os.chdir(title[0])
    except FileExistsError:
        os.chdir(title[0])
    t1=threading.Thread(name='t1',target=thread1_get())
    t2=threading.Thread(name='t2',target=thread2_get())
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    tkinter.messagebox.showinfo("下载器提示", "下载已经完成")
    root.quit()
Button(root, text="开始下载", width=10, command=main).grid(row=4, column=1, sticky=W, padx=10, pady=5)
Button(root, text="退出", width=10, command=root.quit).grid(row=4, column=2, sticky=E, padx=10, pady=5)
root.mainloop()