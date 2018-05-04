import re,requests,os
novelurl="https://book.qidian.com/info/1010475081#Catalog"
novelname=input('请输入小说的名字：')
response1=requests.get(novelurl)
response1.encoding='utf-8'
rex1=re.compile('<a href="(//read.qidian.com/chapter/.*?)" target="_blank" data-eid="qd_G55" data-cid="//read.qidian.com/chapter/.*?" title="首发时间：.*? 章节字数：.*?">(.*?)</a>')
novelnamelist=rex1.findall(response1.text)
f=open('{}.txt'.format(novelname,'a')
for i in rex1.findall(response1.text)
    response2=requests.get('https:{}'.format(i[0]))
    response2.encoding='utf-8'
    rex2=re.compile('<div class="read-content j_readContent">([\s\S]*?)</div>')
    novellist=rex2.findall(response2.text)
    try:
        noveltext=str(novellist[0]).replace('<p>','\n')
    except:
        pass
    f.write('{}\n{}'.format(novel[0],novel[1]))
