import os
import requests
import re
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
    'Referer':'http://lol.qq.com/'
}
def installmodule(modulename):
    try:
        os.system('pip install {}'.format(modulename))
        print('Done')
    except:
        print('A error,please restart')
def get(weburl):
    web=requests.get(url=weburl)
    web.encoding='utf-8'
    return web.text
def post(weburl,data=None):
    web=requests.post(url=weburl,headers=headers,data=data)
    return web.json()
def getdictionary(w):
    new=''
    a=re.findall("([\s\S]*?): ([\s\S]*?)\n",w)
    for i in a:
        new+='\'{}\':\'{}\',\n'.format(i[0],i[1])
    return '{%s}' % new

if __name__=='__main__':
    print(getdictionary('''
'''))