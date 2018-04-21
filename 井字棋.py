#-*-coding:utf8;-*-
import random
import os
list1=['①','②','③','④','⑤','⑥','⑦','⑧','⑨']
list2=[]
def ai():
    n=random.randint(0,8)
    if n in list2:
        return ai()
    else:
        list2.append(n)
        return n
while True:
    os.system('cls')
    print(''' ┌─┬─┬─┐
 │{}│{}│{}│
 ├─┼─┼─┤
 │{}│{}│{}│
 ├─┼─┼─┤
 │{}│{}│{}│
 └─┴─┴─┘
	'''.format(list1[0],list1[1],list1[2],list1[3],list1[4],list1[5],list1[6],list1[7],list1[8]))
    n=int(input('●请输入'))-1
    os.system('cls')
    list2.append(n)
    if list1[n]!='●' and list1[n]!='▲':
        list1[n]='●'
    else:
        print('输入错误，请重新输入')
        continue
    print(''' ┌─┬─┬─┐
 │{}│{}│{}│
 ├─┼─┼─┤
 │{}│{}│{}│
 ├─┼─┼─┤
 │{}│{}│{}│
 └─┴─┴─┘
	'''.format(list1[0],list1[1],list1[2],list1[3],list1[4],list1[5],list1[6],list1[7],list1[8]))
    if (list1[0]=='●' and list1[1] =='●'and list1[2]=='●'):
        print('●赢了')
        input()
        break
    if (list1[3]=='●' and list1[4]=='●' and list1[5]=='●'):
        print('●赢了')
        input()
        break
    if (list1[6]=='●' and list1[7]=='●' and list1[8]=='●'):
        print('●赢了')
        input()
        break
    if (list1[0]=='●' and list1[4]=='●' and list1[8]=='●'):
        print('●赢了')
        input()
        break
    if (list1[2]=='●' and list1[3]=='●' and list1[6]=='●'):
        print('●赢了')
        input()
        break
    if (list1[0]=='●' and list1[3]=='●' and list1[6]=='●'):
        print('●赢了')
        input()
        break
    if (list1[1]=='●' and list1[4]=='●' and list1[7]=='●'):
        print('●赢了')
        input()
        break
    if (list1[2]=='●' and list1[5]=='●' and list1[8]=='●'):
        print('●赢了')
        input()
        break
    a=list(set(list1))
    an=int(input('▲请输入'))-1
    os.system('cls')
    if (list1[0]=='▲' and list1[1] =='▲'and list1[2]=='▲'):
        print('▲赢了')
        input()
        break
    if (list1[3]=='▲' and list1[4]=='▲' and list1[5]=='▲'):
        print('▲赢了')
        input()
        break
    if (list1[6]=='▲' and list1[7]=='▲' and list1[8]=='▲'):
        print('▲赢了')
        input()
        break
    if (list1[0]=='▲' and list1[4]=='▲' and list1[8]=='▲'):
        print('▲赢了')
        input()
        break
    if (list1[2]=='▲' and list1[3]=='▲' and list1[6]=='▲'):
        print('▲赢了')
        input()
        break
    if (list1[0]=='▲' and list1[3]=='▲' and list1[6]=='●'):
        print('▲赢了')
        input()
        break
    if (list1[1]=='▲' and list1[4]=='▲' and list1[7]=='●'):
        print('▲赢了')
        input()
        break
    if (list1[2]=='▲' and list1[5]=='▲' and list1[8]=='●'):
        print('▲赢了')
        input()
        break
    if a==['●','▲'] or a==['▲','●']:
        input('结束')
        break
    list1[an]='▲'
