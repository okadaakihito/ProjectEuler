maxp = 1
for i in range(2,1001):
    l = []
    flag = 0
    k = 1
    o = 1
    while True:
        while True:
            k = 10 * k
            if k > i:
                break
        m = k % i
        if m == 0:
            #print("1"+ str(l) + "." + str(i))
            break
        if len(l) != 0:
            if m in l :
                for n in range (0,len(l)):
                    if l[n]==m:
                        p = o - (n + 1)
                        flag = 1
            else:
                l.append(m)
        else:
            l.append(m)
        #print(l)
        if flag == 1:
            if maxp < p :
                maxp = p
                maxi = i
            #    print(maxp)
            #print(i)
            #print("2"+ str(l) + "." + str(i)+ "." + str(m)+ "." + str(p)+ "." + str(maxp))
            break
        k = m
        o=o+1
print(str(maxp)+ "." +str(maxi))
