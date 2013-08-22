#Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
#If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#
#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
#Evaluate the sum of all the amicable numbers under 10000.
import math
amics = 0
for x in range(0,10001):
    #print("##################################")
    sums=0
    if x % 2 == 0:
        limits=math.ceil(x/2)
    else:
        limits=math.ceil(x/3)
    for y in range(1,limits+1):
        if x%y==0 :
            #print(limits)
            #print(x)
            #print(y)
            sums = sums + y
            #print( str(y) + " is the proper divisors of " + str(x) )
    
    #print( str(sums) + " is the sum of the proper divisors of " + str(x) )
    sums2=0
    if sums % 2 == 0:
        limits=math.ceil(sums/2)
    else:
        limits=math.ceil(sums/3)
    for z in range(1,limits+1):
        if sums%z==0 :
            #print(limits)
            #print(x)
            #print(y)
            sums2 = sums2 + z
            #print( str(z) + " is the proper divisors of " + str(sums) ) 
    #print( str(sums2) + " is the sum of the proper divisors of " + str(sums) )
    if sums2 == x and sums != x:
        print("##################################")
        print( str(x) + " is the amicable numbers with " + str(sums) ) 
        amics = amics + sums2
print("The sum of the amicable numbers from 1 to 1000 is " + str(amics) ) 




