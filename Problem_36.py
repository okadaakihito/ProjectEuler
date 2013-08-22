sums = 0
for i in range (1,1000000):
    if i % 10 != 0:
        if i == int(str(i)[::-1]):
            ic = i
            bnstr = ""
            while ic != 0:
                bn = ic % 2
                if bn == 1:
                    ic = (ic -1)/2
                else:
                    ic = ic/2
                bnstr = str(int(bn)) + bnstr
            if bnstr == bnstr[::-1]:
                sums = sums + i
                print("#################")
                print(i)
                print(bnstr)
                print(sums)
print("#################")
print(sums)

#872187