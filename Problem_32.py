print("start")
result = 0
resultarray =[]
for i in range (1,1000000):
    for l in range (1,1000000):
        flag = 0
        array=[]
        var = i * l
        total = len(str(i)) + len(str(l)) + len (str(var))
        totalstring=str(i)+str(l)+str(var)
        if (total == 9):
            #print(totalstring)
            for j in range (0,len(str(totalstring))):
                k = int(str(totalstring)[j:j+1])
                if k not in array and k != 0:
                    array.append(k)
                else:
                    flag = 1
                    break
            if flag == 0:
                if var not in resultarray:
                    result = var + result
                    print(str(i) + "." + str(l) + "." + str(var))
                    resultarray.append(var)
        elif (total > 9):
            #print(total)
            break
print("result")
print(result)

#45228