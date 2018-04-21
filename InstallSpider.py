import click,os,sys,shutil
@click.command()
@click.option('--install',help='要安装的爬虫的名字',default='')
@click.option('--uninstall',help='要卸载的爬虫的名字',default='')
def install(install,uninstall):
    if uninstall != '':
        try:
            shutil.rmtree(uninstall)
            print('卸载成功')
        except:
            print('卸载失败')
    if install!='':
        try:
            os.mkdir(install)
            os.chdir(install)
            with open('{}.py'.format(install), 'w')as file:
                file.write('''from LycxlSpider import *
import sys,os
class Spider(spider):
    def main(self):
        pass
if __name__=='__main__':
    sys.path.append(os.getcwd())''')
            with open('LycxlSpider.py','w')as file:
                file.write('''import re,requests,os,sys
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
        return self.html''')
            print('安装完成')
        except:
            print('路径冲突，请换一个名字尝试')
if __name__=='__main__':
    install()