#A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
#A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
#
#As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
#
#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
import math
res=0
abndnt=[]
pi=[0 for i in range(28124)]
for x in range(0,28123):
    #print("##################################")
    sums=0
    if x % 2 == 0:
        limits=int(math.ceil(x/2))
        inc=1
    else:
        limits=int(math.ceil(x/3))
        inc=2
    for y in range(1,limits+1,inc):
        if x%y==0 :
            sums = sums + y
    if sums > x :
        abndnt.append(x)
#print(abndnt)
lengs=len(abndnt)
for z in range(0,lengs):
    for a in range(z,lengs):
        reserve=abndnt[z]+abndnt[a]
        if reserve > 28123 :
            break
        else:
            if pi[reserve] == 0:
                pi[reserve]=1
for b in range(1,28124):
    if pi[b] == 0:
        res=res+b
print(str(res) + " is result")

