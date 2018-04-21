import re,requests,os
class spider():
    def __init__(self,url,rex="",headers={}):
        self.url=url
        self.rex=rex
        self.headers=headers
        html=requests.get(self.url)
        html.encoding='utf-8'
        self.html=html.text
    def rex_find(self):
        reg=re.compile(self.rex)
        self.info=reg.findall(self.html)
        return self.info
    def add_rex(self,rex):
        self.rex=rex
    def post(self):
        self.response=requests.post(url=self.url,headers=self.headers).json()
    def get_html(self):
        return self.html