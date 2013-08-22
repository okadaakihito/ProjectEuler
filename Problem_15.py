print ("Start")
#Initial Array
ptns=[[0 for j in range(21)] for i in range(21)] 
#Calcurating First Grids
for x in range(0,21):
        ptns[x][0]=1
        ptns[0][x]=1
        #print(x)
        #print(y)       
        #print (ptns[x][0])
        #print (ptns[0][x])    
#Calcurating Other Grids
for y in range(1,21):
    for x in range(1,21):
        ptns[x][y]=ptns[x-1][y]+ptns[x][y-1]
        #print(x)
        #print(y)
        #print (ptns[x-1][y])
        #print (ptns[x][y-1])
        #print (ptns[x][y])
        #print ("##############")
print (ptns[20][20])
print ("End")
    
    

