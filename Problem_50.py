import eggs

pns=eggs.create_pns(3, 1000000)

lengsmax=0
flag = 0
for i in range(len(pns)-1,0,-1):
    pnsset=-10
    count=0
    pnsfacts=[]
    for j in range(0,len(pns)):
        pnsset=pns[j]+pnsset
        pnsfacts.append(pns[j])
        count += 1
        #print("#############")
        #print(pns[i])
        #print(pns[j])
        #print(pnsfacts)
        #print(pnsset)
        if pnsset > pns[i]:
            break
        elif pnsset == pns[i]:
            lengs=len(pnsfacts)
            print("#############")
            print(pns[i])
            print(pnsfacts)
            if lengs > lengsmax:
                lenmax=lengs
                maxpns=pns[i]
                flag = 1
                break
        if flag == 1:
            break
print(lenmax)
print(maxpns)

#997651
