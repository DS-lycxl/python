import re,requests,os
novelurl="https://book.qidian.com/info/1010933712#Catalog"
noveldirectoryname=input("小说文件夹名:")
response1=requests.get(novelurl)
response1.encoding='utf-8'
rex1=re.compile('<a href="(//read.qidian.com/chapter/.*?)" target="_blank" data-eid="qd_G55" data-cid="//read.qidian.com/chapter/.*?" title="首发时间：.*? 章节字数：.*?">(.*?)</a>')
novelnamelist=rex1.findall(response1.text)
# os.mkdir(noveldirectoryname)
os.chdir(noveldirectoryname)
for i in novelnamelist:
    response2=requests.get('https:{}'.format(i[0]))
    response2.encoding='utf-8'
    rex2=re.compile('<div class="read-content j_readContent">([\s\S]*?)</div>')
    try:
        noveltext=str(rex2.findall(response2.text)[0]).replace('<p>','\n')
    except:
        pass
    with open('{}.txt'.format(i[1]),'w')as f:
        f.write(noveltext)
        f.close()