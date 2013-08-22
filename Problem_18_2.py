print ("Debug : Start")
lists = [75,95,64,17,47,82,18,35,87,10,20,4,82,47,65,19,1,23,75,3,34,88,2,77,73,7,63,67,99,65,4,28,6,16,70,92,41,41,26,56,83,40,80,70,33,41,48,72,33,47,32,37,16,94,29,53,71,44,65,25,43,91,52,97,51,14,70,11,33,28,77,73,17,78,39,68,17,57,91,71,52,38,17,14,91,43,58,50,27,29,48,63,66,4,68,89,53,67,30,73,16,69,87,40,31,4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]
ptns=[[0 for i in range(32)] for j in range(32)] 
lines=[0 for i in range(32)]
lines2=[0 for i in range(32)]
count=0
sums=0
ptnsmax=0
sumsmax=0
line=0
data=0
lines2[1]=75
for y in range(1,16):
    for x in range(1,16):
        if y >= x :
            ptns[y][x]=lists[count]
            count=count+1
            #print(count)
for y in range(1,15):
    print("####################")
    data=1
    count=1
    for x in range(1,16,2):
        #print(y)
        #print(x)
        if y + 1  >= x :
                lines[data]=lines2[count]+ptns[y+1][x]
                print("####################")
                print(data)
                print(ptns[y+1][x])
                print(lines2[count])
                print(lines[data])
                data = data +1
                if ptns[y+1][x+1] != 0 :
                    print("####################")
                    lines[data]=lines2[count]+ptns[y+1][x+1]
                    #else :
                    #    line[x]=ptns[y][x]+ptns[y+1][x]
                    #    data = data +1
                    #    line[x]=ptns[y][x]+ptns[y+1][x+1]
                    #    data = data +1
                    print(data)
                    print(ptns[y+1][x+1])
                    print(lines2[count])
                    print(lines[data])
                    data = data +1
                    count = count +1
    for x in range(1,32):
        lines2[x]=lines[x]
for x in range(1,32):
    if sumsmax < lines[x]:
        sumsmax=lines[x]
print("####################")
print("####################")
print("###sumsmax#################" + str(sumsmax))

     
    


            #print("update !! ptnsmax=" + str(sums))
#print("sums =" + str(sums))   