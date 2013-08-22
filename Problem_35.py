# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?

import math
result = 0
array = []
for i in range (0,1000001):
    if i % 10 != 0 and  i % 2 != 0:
        array = []
        for j in range (0,len(str(i))):
            array.append(int(str(i)[j:j+1]))
        c=0
        cc = c
        for m in range (0,len(str(i))):
            cn=""
            for k in range (0,len(str(i))):
                if cc == len(str(i)) -k:
                    cc = -k
                cn = str(array[k+cc]) + cn
            n=int(cn)
            maxn=int(math.sqrt(n))
            flag=1
            for l in range(2,maxn+1):
                if n % l ==0:
                    flag=0
                    break
            if flag == 1:
                c=c+1
                cc = c
            else:
                break
        if flag == 1 and i != 1:
            print(i)
            result = result +1
print("result")
print(result + 1)

#55