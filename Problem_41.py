import math
for i in range(7654321,0,-2):
    if i % 5 != 0 and i % 3 != 0:
        arrays=[]
        flag = 1
        for j in range(0,7):
            cn = str(i)[j:j+1]
            if cn != "0" and int(cn) <= len(str(i)) and cn not in arrays:
                arrays.append(str(i)[j:j+1])
            else:
                flag = 0
                break
        if flag == 1 :
            maxn=int(math.sqrt(i))
            for r in range(7,maxn+1,2):
                if i % r == 0 :
                    flag = 0
                    break
            if flag == 1 :
                print("####")
                print(i)
                break
#7652413
