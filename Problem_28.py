imax=2002
nums = [0 for i in range(imax+1)]
nk = 1
j = 1
k = 1
sums=0
for i in range(1,imax,2):
    nums[i]=j
    nums[i+1]=j
    j=j+1
    #print(i)
    #print(nums[i])
for i in range(1,imax):
    nk = nk + nums[i]
    if k == 1:
        sums= nk -1 + sums
        k = k + 1
    elif k == 2 or k == 3:
        sums= nk + sums
        k = k + 1
    elif k == 4:
        sums= nk + sums
        k = 1
    #print(i)
    #print(nk)
    #print(nums[i])
print(sums)

#669171001