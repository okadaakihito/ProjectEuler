#Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
#
#For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938  53 = 49714.
#
#What is the total of all the name scores in the file?
#

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
file = open('/Users/okadaakihito/Desktop/names.txt','rt')
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
for x in range(0,lengs):
    namelengs=len(row[x])
    #print(namelengs)
    sums = 0
    #print(row[x])
    for y in range(0,namelengs):
        slices=row[x]
        letters=slices[y:y+1]
        #print(letters)
        #print(dicts[letters])
        sums = sums + dicts[letters]
    #print(x)
    #print(sums)
    #print(point)
    point=point + sums*(x+1)
print(point)
print (row)