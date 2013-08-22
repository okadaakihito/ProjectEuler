import math
import itertools
def create_primenubers(x, y):
    #parrays=[ i for i in range(x,y,2) for r in range(3,maxn+1,2) if i % r == 0 ]
    parrays=[]
    for i in range(x,y,2):
        flag=1
        for r in range(3,maxn(i)+1,2):
            if i % r == 0:
                flag = 0
                break
        if flag == 1 :
            parrays.append(i)
    return parrays

def strset(k):
    strsets=int(str(strlist[k][0])+str(strlist[k][1])+str(strlist[k][2])+str(strlist[k][3]))
    return strsets

def maxn(i):
    maxn=int(math.sqrt(i))
    return maxn

parrays=create_primenubers(1001, 9999)
length=len(parrays)
flag = 0
for i in range(0,length):
    ch = [0 for o in range(100000)]
    arrays=[(str(parrays[i])[j:j+1]) for j in range(0,4)]
    strlist=list(itertools.permutations(arrays))
    strlength=len(strlist)
    parraysn=[strset(k) for k in range(0,strlength) if strset(k) in parrays]
    pn=sorted(set(parraysn), key=parraysn.index)
    pn.sort()
    if len(pn) >= 3:
        for l in range(0,len(pn)):
            for m in range(1,len(pn)-l):
                diff=pn[l+m]-pn[l]
                if ch[diff] == 0:
                    ch[diff]=[]
                ch[diff].append(str(pn[l+m]))
                ch[diff].append(str(pn[l]))
    for o in range(0,100000):
        if ch[o] != 0:
            cho=sorted(set(ch[o]), key=ch[o].index)
            cho.sort()
            if len(cho)==3 and cho[0] != "1487":
                strs=cho[0]+cho[1]+cho[2]
                flag = 1
                print(o)
                print(strs)
    if flag == 1:
        break
#296962999629