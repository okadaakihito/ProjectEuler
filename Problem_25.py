class END(Exception):
    pass
try:
    term1=1
    term2=1
    i=3
    while 1:
        term3=term1+term2
        lengs=len(str(term3))
        if lengs == 1000:
            print("lengs is 1000 digits , " + str(term3) )
            print(i)
            raise END
        term1=term2
        term2=term3
        i += 1
except END: 
    print("END")