from decimal import *
maximum=0
getcontext().prec = 4000
for d in range(1,1001):
    f=str(Decimal(Decimal(1)/Decimal(d)))
    for x in range(1,10):
        for y in range(2000,5000):
            letters1=f[x:x+y]
            letters2=f[x+y:x+2*y]
            lengs=len(letters1)
            if letters1 != "" and letters1 == letters2 and lengs > 300:
                print("d = "+ str(d) +",letters =" + str(letters1) + "\tf =" + str(f))
                if y > maximum :
                    done=d
                    fin=f
                    finletters=letters2
                    maximum=y
                break
print("done ." + str(done))
print("fin ." + str(fin))
print("finletters ." + str(finletters))
print("maximum ." + str(maximum))