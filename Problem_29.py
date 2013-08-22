print("start")
#maxpow=pow(100,100)+1
count=0
#print(maxpow)
#arry=[0 for i in range(maxpow)]
arry=[]
for i in range (2,101):
    for j in range (2,101):
        #arry[pow(i,j)]=1
        if pow(i,j) not in arry:
            arry.append(pow(i,j))
for i in arry:
    count=count+1
print(count)

#9183
