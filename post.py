import requests
import hashlib
md5 = hashlib.md5()
s=input('请输入英文：')
md5.update('20180416000147177{}123u5dIq_UmJztYIET930YS'.format(s))
header={'q':'{}'.format(s),
'from':'auto',
'to':'zh',
'appid':20180416000147177,
'salt':123,
'sign':md5.hexdigest()
}
r.requests.post('http://api.fanyi.baidu.com/api/trans/vip/translate',headers=header)
print(r)
