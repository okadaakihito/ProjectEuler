import math

class END(Exception):
    pass
try:
    nmax=10000
    d=0
    for n in range(1,nmax):
        for i in range(1,nmax-n-1):
            pb=(n+i)*(3*(n+i)-1)/2
            ps=n*(3*n-1)/2
            pm=pb-ps
            pp=pb+ps
            pmn = (1+math.sqrt(1+24*pm))/6
            pmni = int(pmn)
            ppn = (1+math.sqrt(1+24*pp))/6
            ppni = int(ppn)
            if pmn == pmni and ppn == ppni:
                #print("####")
                #print(pb)
                #print(ps)
                #print(pm)
                #print(pmn)
                #print(pmni)
                #print(ppn)
                #print(pp)
                #print(ppni)
                #print(n)
                #print(i)
                raise END
except END:
    print(int(pm))
    print("END")