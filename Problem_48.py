sums=0
for i in range(1,1001):
    prod=1
    for j in range(1,i+1):
        prod=prod*i
    sums=sums+prod
length=len(str(sums))
print(sums)
print(str(sums)[length-10:length])