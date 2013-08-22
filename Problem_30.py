result = 0
for i in range (0,1000001):
    sums = 0
    for j in range (0,len(str(i))):
        sums = pow(int(str(i)[j:j+1]),5) + sums
        if sums > i :
            break
    if sums == i:
        result = sums +result
        print(sums)
print("result")
print(result-1)

#443839