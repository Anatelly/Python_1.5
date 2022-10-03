import csv
red='\u001b[41m'
blue='\u001b[44m'
white='\u001b[47m'
end='\u001b[0m'
violet='\u001b[45m'
green='\u001b[42m'

def f1():
    for i in range(3):
        print(white+'\\'*20+ end)
    for i in range(3):
        print(red+'\\'*20+end)
    print()

def f2():
    print(blue+' '*22+end)
    print(' '*10+blue+' '*2+end+' '*10)
    print(blue+' '*22+end)
    print(' '*4+blue+' '*2+end+' '*10+blue+' '*2+end+' '*4)
    print(blue+' '*22+end)
    print()

def f3():
    x=[i for i in range(0,101) if i**0.5%1==0]
    for i in range(len(x)-2,-1,-1):
        print(int(x[i]**0.5),' '*x[i]+green+'\\'*(x[i+1]-x[i])+end)
    print(end='  ')
    s=[str(i) for i in range(101)]
    print(''.join(s[:10]),end='')
    s1=[str(int(i)//10) for i in s[10:]]
    print(''.join(s1))
    s2 = [str(int(i) % 10) for i in s[10:]]
    print(' '*12+''.join(s2))
    print()

def f4():
    c1=c2=0
    with open('books.csv') as csvfile:
        table = list(csv.reader(csvfile, delimiter=';'))
        for row in table[1:]:
            if int(row[6][:4])>=2017: c1+=1
            else: c2+=1
    c1=((c1/(c1+c2))*100)//1
    c2=(100-c1)//1
    print('После 2017: ' + violet + ' '*int(c1) + end, int(c1),'%')
    print()
    print('До 2017:    ' + violet + ' '*int(c2) + end, int(c2),'%')
f1()
f2()
f3()
f4()





