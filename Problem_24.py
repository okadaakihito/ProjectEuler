#A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
#
#012   021   102   120   201   210
#
#What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
#
class END(Exception):
    pass
try:
    k=1
    for a in range(0,10):
        for b in range(0,10):
            if b != a: 
                for c in range(0,10):
                    if c != a and c!=b: 
                        for d in range(0,10):
                            if d != a and d != b and d!=c:
                                for e in range(0,10):
                                    if e != a and e != b and e != c and e != d :
                                        for f in range(0,10):
                                            if f != a and f != b and f != c and f != d and f != e :
                                                for g in range(0,10):
                                                    if g != a and g != b and g != c and g != d and g != e  and g != f:
                                                        for h in range(0,10):
                                                            if h != a and h != b and h != c and h != d and h != e  and h != f and h != g :
                                                                for i in range(0,10):
                                                                    if i != a and i != b and i != c and i != d and i != e  and i != f and i != g and i != h :
                                                                        for j in range(0,10):
                                                                            if j != a and j != b and j != c and j != d and j != e  and j != f and j != g and j != h and j != i:
                                                                                if k == 1000000:
                                                                                    letters=str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(g) + str(h) + str(i) + str(j)
                                                                                    print(str(letters) + " is the millionth lexicographic permutation")
                                                                                    raise END
                                                                                print(k)
                                                                                k += 1
except END: 
    print("END")