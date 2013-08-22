import math
count=0
sums=0
count=0
for i in range (10,100000000):
    if count != 11:
        if i % 10 != 0:
            array=[i]
            for j in range(1,len(str(i))):
                array.append(str(i)[j:j+len(str(i))])
            for j in range(1,len(str(i))):
                array.append(str(i)[0:-j+len(str(i))])
            flag = 1
            for j in array:
                n=int(j)
                if n == 1:
                    flag=0
                    break
                maxn=int(math.sqrt(n))
                for k in range(2,maxn+1):
                    if n % k ==0:
                        flag=0
                        break
            if flag == 1:
                sums=sums+i
                count=count+1
                print(i)
                print(sums)
print(sums)
