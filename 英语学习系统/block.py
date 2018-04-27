import timeit,random,os,time
nl=[]
def get_number():
    global nl
    number=random.randint(1,25)
    if number not in nl:
        nl.append(number)
    else:
        get_number()
def main():
    for i in range(25):
        get_number()
    a=0
    for i in nl:
        if a==5:
            print('\n',end='')
            a=0
        print(i,end='\t')
        a+=1
    input('\n按下回车结束...')
def s(word,sleeptime):
    print(word)
    time.sleep(sleeptime)
if __name__=='__main__':
    s('欢迎来到舒尔特方格游戏',1)
    input('按下回车键以开始...')
    s('准备好了么',1)
    s(3,1)
    s(2,1)
    s(1,1)
    s('开始计时',0.5)
    start=time.time()
    os.system('clear')
    main()
    over=time.time()
    os.system('clear')
    print('你的时间是{}秒'.format(over-start))