"""
__author__=李霆宇
__time__=2018/3/30 23:20
__version__=0.0.1
"""
n=int(input("请输入要到达的位数："))
NumList=[2,3,5,7]
OverList=[]
TestList=[]
for i in range(11,n):
    if i%2!=0 and i%3!=0 and i%5!=0:
        NumList.append(i)
for i in range(len(NumList)):
    for it in range(len(NumList)):
        if NumList[i]+NumList[it]>=6:
            print("{}+{}={}".format(NumList[it],NumList[i],NumList[i]+NumList[it]))
            OverList.append(NumList[i]+NumList[it])
Run=list(set(OverList))
for i in Run:
    if i%2!=0:
        Run.remove(i)
# print(Run)
for i in range(len(Run)-1):
    if Run[i+1]-Run[i]==2:
        print("√",end=" ")
    else:
        print("x",end=" ")
input()