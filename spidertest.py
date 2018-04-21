from LycxlSpider import *
class Spider(spider):
    def main(self):
        self.rex_find()
        print(self.info[0])
if __name__=='__main__':
    caokeyi=Spider('https://www.baidu.com')
    caokeyi.add_rex('<link rel=stylesheet type=text/css href=(.*?)><title>(.*?)</title></head> <body link=#0000cc>')
    caokeyi.main()