import re,requests,os,sys,threading
f=open('web.txt','r')
info=f.read().split('\n')
f.close()
def get_novel(i):
    novelurl=i
    response1=requests.get(novelurl)
    response1.encoding='utf-8'
    rex1=re.compile('<a href="(//read.qidian.com/chapter/.*?)" target="_blank" data-eid="qd_G55" data-cid="//read.qidian.com/chapter/.*?" title="首发时间：.*? 章节字数：.*?">(.*?)</a>')
    noveldirectoryname=re.compile('''<title>《(.*?)》.*?</title>''')
    noveldirectoryname=noveldirectoryname.findall(response1.text)
    os.chdir(sys.path[0])
    os.chdir('novel/')
    f=open('{}.txt'.format(noveldirectoryname[0]),'a')
    novelnamelist=rex1.findall(response1.text)
    times=0
    for i in novelnamelist:
        response2=requests.get('https:{}'.format(i[0]))
        response2.encoding='utf-8'
        rex2=re.compile('<div class="read-content j_readContent">([\s\S]*?)</div>')
        novel=rex2.findall(response2.text)
        noveltext=str(novel[0]).replace('<p>','\n')
        f.write('\n\n{}{}'.format(i[1],str(novel[0]).replace('<p>','\n')))
        times+=1
        print('《{}》'.format(noveldirectoryname[0]),end='')
        hb=times/len(novelnamelist)*100
        print('下载进度为%.2f'%hb,end='')
        print('%')
    print('《{}》下载完成！'.format(noveldirectoryname[0]))
    f.close()
if __name__=='__main__':
    name=1
    for i in info:
        threading.Thread(target=get_novel,args=(i,),name='thread-{}'.format(name)).start()
        name+=1
