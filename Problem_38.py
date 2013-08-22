panmax = 0
for i in range(1,10000):
    strings = ""
    flag = 1
    arrays=[]
    for j in range(1,20):
        strings = strings  + str(i * j)
        if len(strings) == 9:
            break
    if len(strings) == 9:
        for k in range (0,10):
            num=strings[k:k+1]
            #print(k)
            if num not in arrays and num != "0":
                arrays.append(num)
            else:
                flag = 0
                break
        if int(strings) > panmax and flag == 1 :
            panmax = int(strings)
            print("##################")
            print(arrays)
            print(len(strings))
            print(i)
            print(j)
            print(strings)

print(panmax)
#