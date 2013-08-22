'''
Created on 2013/06/07

@author: okadaakihito
'''

def isPalindromic(number):
        strN = str(number)
        strReverse = strN[::-1]
        return strN == strReverse


maxProduct = 0
for i in range(100,1000):
    for j in range(100,1000):
        product = i*j
        if isPalindromic(product):
            if maxProduct < product:
                maxProduct = product

print (maxProduct)
