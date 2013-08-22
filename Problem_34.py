# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.
import math
result = 0
for i in range (0,10000001):
    sums = 0
    for j in range (0,len(str(i))):
        sums = math.factorial(int(str(i)[j:j+1])) + sums
        if sums > i :
            break
    if sums == i and sums != 1 and sums != 2:
        result = sums +result
        print(sums)
print("result")
print(result)

#40730