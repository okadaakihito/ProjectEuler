# -*- coding: utf-8 -*-

count=0
maxnums = 200
maxnum = maxnums +1
for i in range (0,maxnum,200):
    for j in range (0,maxnum,100):
        for k in range (0,maxnum,50):
            for l in range (0,maxnum,20):
                for m in range (0,maxnum,10):
                    for n in range (0,maxnum,5):
                        for o in range (0,maxnum,2):
                            for p in range (0,maxnum,1):
                                sums = i + j + k + l + m + n + o + p
                                if sums == maxnums :
                                    count = count +1
                                    #print(count)
                                elif sums > maxnums :
                                    break
print(count)

#73682