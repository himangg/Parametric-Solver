def swap(l,i,m):
    temp=l[i]
    l[i]=l[m]
    l[m]=temp
def check(l,j):
    i=0
    while i<j:
        if l[i]!=0:
            return False
        i+=1
    else:
        return True
def sort_0(l):
    for j in range(len(l[0])):
        for i in range(len(l)):
            if l[i][j]==0 and check(l[i],j):
                for m in range(len(l)-1,j,-1):
                    if l[m][j]!=0:
                        swap(l,i,m)
                        break
    return l
file=open('maths assignment/assignment 1.txt','r')
l=[]
for i in file.readlines():
    l1=list(map(int,i.split()))
    l.append(l1)
l=sort_0(l)
j,i=0,0
pivot={}
while j<len(l) and i<len(l[j]):
    if l[j][i]==0:
        i+=1
    elif l[j][i]!=1:
        h=l[j][i]
        for m in range(len(l[j])):
            l[j][m]=l[j][m]/h
    else:
        pivot.update({i:j})
        for n in range(j+1,len(l)):
            if l[n][i]!=0:
                h=l[n][i]
                for m in range(len(l[n])):
                    l[n][m]=l[n][m]/h
                for m in range(len(l[n])):
                    l[n][m]=l[n][m]-l[j][m]
                    if l[n][m]<10**(-10) and l[n][m]>(-10**(-10)):
                        l[n][m]=0.0
        j+=1
        i+=1
for i in pivot.keys():
    z=pivot[i]
    for j in range(len(l)):
        if l[j][i]!=0 and j!=z:
            h=l[j][i]
            for m in range(len(l[j])):
                l[j][m]=l[j][m]/h 
            for m in range(len(l[j])):
                l[j][m]=l[j][m]-l[z][m]
                if l[j][m]<10**(-10) and l[j][m]>(-10**(-10)):
                        l[j][m]=0.0
            for m in range(len(l[j])):
                l[j][m]=l[j][m]*h
print('RREF:')
for i in range(len(l)):
    for j in range(len(l[0])):
        print(round(l[i][j],3),end="  ")
    print()
lst,lst1=[],[]
for j in range(len(l[0])):
    lst.append([])
    for i in range(len(l)):
        l[i][j]=round(l[i][j],3)                     ## TO ROUND OFF THE NUMBER ##
for i in range(len(l[0])):
    if i not in pivot.keys():
        h=0
        for m in range(len(l[0])):
            if m in pivot.keys():
                lst[m].append(-l[h][i])
                h+=1
            elif m==i:
                lst[m].append(1)
            else:
                lst[m].append(0)
for i in range(len(l[0])):
    if i not in pivot.keys():
        lst1.append(i+1)
if len(lst[0])==0:                                 ## TO HANDLE THE CASE 
    for i in l[0]:
        print('[0]')
    exit()
flag=False
for i in range(len(lst)):
    for j in range(len(lst[i])):
        if i+1==(len(l[0])//2)+1:
            if flag:
                print('+',end=' ')
            else:
                print(' ',end=' ')
            print('x',lst1[j],end=' ',sep='')
            flag=True
        else:
            print('     ',end='')    
        print('|',lst[i][j],'|',sep='',end=' '*(7-len(str(lst[i][j]))))
    print()
file.close()
