import math

class END(Exception):
    pass
try:
    nmax=100000000000
    for cn in range(145,nmax):
        #Hexagonal
        hn = cn*(2*cn-1)
        #Pentagonal
        if (1+math.sqrt(1+24*hn)) % 6 == 0:
            #Triangle
            if (-1+math.sqrt(1+8*hn)) % 2 == 0:
                    print("####")
                    print(hn)
                    print(cn)
                    #print(i)
                    raise END
except END:
    print(int(cn))
    print("END")