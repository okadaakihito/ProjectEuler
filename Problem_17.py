# -*- coding: utf-8 -*-
print ("Start")
#Initial Array
sums=0
ptns=[[0 for j in range(3)] for i in range(1001)] 
#Calcurating 
for x in range(1,1001):
        if(x == 1):
            ptns[x][0]="one"
            ptns[x][1]=int(len(ptns[x][0])) 
        if(x == 2):
            ptns[x][0]="two"
            ptns[x][1]=int(len(ptns[x][0]))          
        if(x == 3):
            ptns[x][0]="three"
            ptns[x][1]=int(len(ptns[x][0])) 
        if(x == 4):
            ptns[x][0]="four"
            ptns[x][1]=int(len(ptns[x][0]))               
        if(x == 5):
            ptns[x][0]="five"
            ptns[x][1]=int(len(ptns[x][0])) 
        if(x == 6):
            ptns[x][0]="six"
            ptns[x][1]=int(len(ptns[x][0])) 
        if(x == 7):
            ptns[x][0]="seven"
            ptns[x][1]=int(len(ptns[x][0])) 
        if(x == 8):
            ptns[x][0]="eight"
            ptns[x][1]=int(len(ptns[x][0]))                 
        if(x == 9):
            ptns[x][0]="nine"
            ptns[x][1]=int(len(ptns[x][0])) 
        if(x == 10):
            ptns[x][0]="ten"
            ptns[x][1]=int(len(ptns[x][0])) 
        if(x == 11):
            ptns[x][0]="eleven"
            ptns[x][1]=int(len(ptns[x][0])) 
        if(x == 12):
            ptns[x][0]="twelve"
            ptns[x][1]=int(len(ptns[x][0])) 
        if(x == 13):
            ptns[x][0]="thirteen"
            ptns[x][1]=int(len(ptns[x][0]))
        if(x == 15):
            ptns[x][0]="fifteen"
            ptns[x][1]=int(len(ptns[x][0]))
        if(x == 18):
            ptns[x][0]="eighteen"
            ptns[x][1]=int(len(ptns[x][0]))
        if x == 14 or ( x >= 16 and x <= 17 ) or x==19 :
            ptns[x][0]=str(ptns[x-10][0]) + "teen"
            ptns[x][1]=int(len(ptns[x][0]))   
        if(x == 20):
            ptns[x][0]="twenty"
            ptns[x][1]=int(len(ptns[x][0]))
        if x >= 21 and x <= 29 :
            ptns[x][0]=str(ptns[20][0]) + str(ptns[x-20][0])
            ptns[x][1]=int(len(ptns[x][0])) 
        if(x == 30):
            ptns[x][0]="thirty"
            ptns[x][1]=int(len(ptns[x][0]))
        if x >= 31 and x <= 39 :
            ptns[x][0]=str(ptns[30][0]) + str(ptns[x-30][0])
            ptns[x][1]=int(len(ptns[x][0]))
        if(x == 40):
            ptns[x][0]="forty"
            ptns[x][1]=int(len(ptns[x][0]))
        if(x==60 or x==70 or x==90):
            i=int(x/10)
            ptns[x][0]=str(ptns[i][0]) + "ty"
            ptns[x][1]=int(len(ptns[x][0]))
        if(x == 50):
            ptns[x][0]="fifty"
            ptns[x][1]=int(len(ptns[x][0]))  
        if(x == 80):
            ptns[x][0]="eighty"
            ptns[x][1]=int(len(ptns[x][0]))  
        if x >= 41 and x <= 99 and x % 10 != 0:
            i=int(x%10)
            j=int(x-i)
            ptns[x][0]=str(ptns[j][0]) + str(ptns[i][0]) 
            ptns[x][1]=int(len(ptns[x][0]))
        if(x % 100 == 0):
            i=int(x/100)
            ptns[x][0]=str(ptns[i][0]) + "hundred"
            ptns[x][1]=int(len(ptns[x][0]))  
        if x >= 101 and x <= 999 and ( x % 100 != 0 ):
            i=int(x%100)
            j=int(x-i)
            k=int(x/100)
            ptns[x][0]=str(ptns[k][0]) + "hundredand" + str(ptns[i][0])
            ptns[x][1]=int(len(ptns[x][0])) 
        if(x == 1000):
            ptns[x][0]="onethousand"
            ptns[x][1]=int(len(ptns[x][0]))
        print("================== ")
        print(x)
        print (ptns[x][0])
        print (ptns[x][1])
        sums=ptns[x][1]+sums
        print (sums)
#print (ptns[20][20])
print ("End")
