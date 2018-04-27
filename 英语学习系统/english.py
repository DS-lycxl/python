import os,pickle,getch
def init():
    print('1 - 输入单词')
    print('2 - 获取单词')
    print('3 - 提升注意力小游戏')
    print('4 - 初始化')
    print('q - 退出程序')
if __name__=='__main__':
    os.system('clear')
    while True:
        init()
        number=getch.getch()
        if number=='1':
            s=0
            os.system('clear')
            askchinese=input('Chinese:')
            askenglish=input('English:')
            file=open('log.pkl','rb')
            mylist=pickle.load(file)
            file.close()
            f=open('log.pkl','wb')
            mylist.append({askchinese:askenglish})
            pickle.dump(mylist,f)
            f.close()
            os.system('clear')
            print('成功保存:\t{}-{}'.format(askchinese,askenglish))
        if number=='2':
            os.system('clear')
            file=open('log.pkl','rb')
            mylist=pickle.load(file)
            file.close()
            print('你的成果：')
            print(mylist)
        if number=='3':
            os.system('clear')
            os.system('python3 block.py')
        if number=='4':
            file=open('log.pkl','wb')
            pickle.dump([],file)
            file.close()
            os.system('clear')
        if number=='q':
            os.system('clear')
            break