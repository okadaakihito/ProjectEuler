
strs = "0."
for i in range (1,1000000):
    strs = strs + str(i)
    if strs[1000000+1:1000000+2] != "":
        d1 = int(strs[2:3])
        d10 = int(strs[11:12])
        d100 = int(strs[100+1:100+2])
        d1000  = int(strs[1000+1:1000+2])
        d10000  = int(strs[10000+1:10000+2])
        d100000  = int(strs[100000+1:100000+2])
        d1000000  = int(strs[1000000+1:1000000+2])
        res = d1*d10*d100*d1000*d10000*d100000*d1000000
        print(d1)
        print(d10)
        print(d100)
        print(d1000)
        print(d10000)
        print(d100000)
        print(d1000000)
        print("##########")
        print(res)
        break