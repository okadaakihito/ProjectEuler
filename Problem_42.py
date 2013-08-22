
import csv
dicts = {
        'A':1,
        'B':2,
        'C':3,
        'D':4,
        'E':5,
        'F':6,
        'G':7,
        'H':8,
        'I':9,
        'J':10,
        'K':11,
        'L':12,
        'M':13,
        'N':14,
        'O':15,
        'P':16,
        'Q':17,
        'R':18,
        'S':19,
        'T':20,
        'U':21,
        'V':22,
        'W':23,
        'X':24,
        'Y':25,
        'Z':26
        }
file = open('words.txt','rt')
try:
    reader = csv.reader(file)
    for row in reader:
        print (row)
finally:
    file.close()
row.sort()
#print (row)
lengs=len(row)
#print(lengs)
point=0
arrays = [0 for i in range(lengs+1)]
for x in range(0,lengs):
    strlengs=len(row[x])
    #print(namelengs)
    sums = 0
    #print(row[x])
    for y in range(0,strlengs):
        slices=row[x]
        letters=slices[y:y+1]
        #print(letters)
        #print(dicts[letters])
        sums = sums + dicts[letters]
    #print(x)
    #print(sums)
    #print(point)
    arrays[x]=sums
maxa=max(arrays)
#print(maxa)
#print(arrays)
#print (row)
tns=[]
for n in range(1,1000):
    tn=1/2*n*(n+1)
    tns.append(tn)
    #print(tn)
    if tn > maxa:
        break
count=0
for x in range(0,lengs):
    if arrays[x] in tns:
        #print(arrays[x])
        #print(count)
        count = count + 1
print(count)

#162
