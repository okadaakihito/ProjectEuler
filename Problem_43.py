#!/usr/bin/python
import itertools
arrays = [0,1,2,3,4,5,6,7,8,9]
lists = list(itertools.permutations(arrays))
length=len(lists)
count=0
sums=0
print(length)
for j in range(0,length):
    flag = 1
    if lists[j][0] == 0:
        flag = 0
    if lists[j][3] % 2 != 0 and flag == 1 :
        flag = 0
    if lists[j][5] != 0 and lists[j][5] != 5  and flag == 1 :
        flag = 0
    ch3=lists[j][2]+lists[j][3]+lists[j][4]
    if (ch3) % 3 != 0 and flag == 1 :
        flag = 0
    ch7=lists[j][4]*2+int(str(lists[j][5])+str(lists[j][6]))
    if ch7 % 7 != 0 and flag == 1 :
        flag = 0
    ch11 = lists[j][5]+lists[j][7]-lists[j][6]
    if (ch11 != 0) and ( ch11 % 11 != 0)  and flag == 1 :
        flag = 0
    ch13 = int(str(lists[j][6]) + str(lists[j][7]) + str(lists[j][8]))
    if ch13 % 13 != 0 and flag == 1 :
        flag = 0
    ch17 = int(str(lists[j][7]) + str(lists[j][8]) + str(lists[j][9]))
    if ch17 % 17 != 0 and flag == 1 :
        flag = 0
    if flag == 1 :
        count = count + 1
        sums  =  sums + int(str(lists[j][0]) + str(lists[j][1]) + str(lists[j][2])+str(lists[j][3]) + str(lists[j][4]) + str(lists[j][5])+str(lists[j][6])+str(lists[j][7]) + str(lists[j][8]) + str(lists[j][9]))
        print(lists[j])
print(count)
print(sums)

#16695334890
