#n! means n  (n  1)  ...  3  2  1
#
#For example, 10! = 10  9  ...  3  2  1 = 3628800,
#and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
#Find the sum of the digits in the number 100!

print('program start')
nums=1
for x in range(100,0,-1):
    nums=nums*x
    print(x)
    print(nums)
slices = str(nums)
lengs = len(slices)
sums=0
print(lengs)
for x in range(0,lengs):
    digits = slices[x:x+1]
    sums = int(digits) + sums
    print(digits)
    print(sums)
print('the sum of the digits in the number 100! is ' + str(sums))
print('program end')