import re,requests,os
n=requests.get('https://book.qidian.com/info/1003499719#Catalog')
urllist=re.findall('<a href="(//read.qidian.com/chapter/.*?)" target="_blank" data-eid="qd_G55" data-cid="//read.qidian.com/chapter/.*?" title="首发时间：.*? 章节字数：.*?">(.*?)</a>',n.text)
for i in urllist:
    q=requests.get('https'+[0])
    novel='<div class="read-content j_readContent">([\s\S]*?)</div>'
    with open(i[1],'w')as f:
        f.write(re.findall(novel,q.text)[0])