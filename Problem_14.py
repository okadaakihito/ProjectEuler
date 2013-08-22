print ("Start")
#n=13
maxi=1
for n in range(1000000,100000,-1):
    i=1
    nc=n
    if n % 10000 == 0:
        print ("Now,calurating n = " + str(n))
    while True:
        if n % 2 == 0:
            n=n/2
            #print ("n = " + str(n))
        else:
            n=3*n+1
            #print ("n = " + str(n))
        i+=1
        if n == 1:
            if i > maxi:
                print ( str(nc) + " is maximum now ,n = " + str(n) + " i =" + str(i))
                maxi = i
                maxn = nc
            break
print ( str(maxn) + " is Longest Collatz sequence ," + str(maxi) + "terms")
print ("End")
    
    

