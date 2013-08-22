arrayi = []
arrayj = []
for i in range (10,100):
    for j in range (10,100):
        if ( i % 10 != 0 ) and  ( j % 10 != 0 ) and ( j % 11 != 0 ) and ( i % 11 != 0 ) and ( i != j ) and ( i < j ):
            a1 = i / j
            i1 = str(i)[0:1]
            i2 = str(i)[1:2]
            j1 = str(j)[0:1]
            j2 = str(j)[1:2]

            #print(i)
            #print(i1)
            #print(i2)
            #print(j)
            #print(j1)
            #print(j2)

            a2 = 0

            if i1 == j1:
                a2 = int(i2) / int(j2)
            if i1 == j2:
                a2 = int(i2) / int(j1)
            if i2 == j1:
                a2 = int(i1) / int(j2)
            if i2 == j2:
                a2 = int(i1) / int(j1)
            if a1 == a2 :
                print("it's pair")
                print(i)
                arrayi.append(i)
                print(j)
                arrayj.append(j)
print(arrayi)
print(arrayj)
producti = 1
productj = 1
for i in  range (0,len(arrayi)) :
    producti = arrayi[i] * producti
    print(producti)
for j in  range (0,len(arrayj)) :
    productj = arrayj[j] * productj
    print(productj)
print(productj/producti)
