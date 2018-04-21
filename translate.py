import requests
import random
word=input('请输入你要翻译的词：')
headers={
'Accept':'application/json, text/javascript, */*; q=0.01',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.9',
'Connection':'keep-alive',
'Content-Length':'204',
'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
'Cookie':'OUTFOX_SEARCH_USER_ID_NCOO=1108625929.744807; _ntes_nnid=f81ea1987eba7e9f00c338dc859c8ef6,1500373463076; OUTFOX_SEARCH_USER_ID=-920355853@60.10.254.201; P_INFO=lianyu_xianglong@163.com|1519112581|0|other|00&99|bej&1518607121&other#bej&null#10#0#0|&0||lianyu_xianglong@163.com; JSESSIONID=aaaVmEL6iuetK_sH6Laiw; ___rl__test__cookies=1520428440533',
'Host':'fanyi.youdao.com',
'Origin':'http://fanyi.youdao.com',
'Referer':'ttp://fanyi.youdao.com/',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
'X-Requested-With':'XMLHttpRequest',
}
salt=str(random.randint(1,10))
appid='59cdcb8200b2fdb7'
appkey='lobr0xVKdfr3AvJzB7YDvlARfF5q7Efe'
formdata={
'q':word,
'from':'AUTO',
'to':'AUTO',
'salt':salt,
'sign':appid+word+salt+appkey,
'appKey':appid

}
request=requests.post(url='https://openapi.youdao.com/api',headers=headers,data=formdata)
print(request.text)
# ['smartResult']['entries'][1]