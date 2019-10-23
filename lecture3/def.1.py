def evenNumLst(ran):
    lst=[]
    for num in range(ran):
        if num % 2 == 0:
            lst.append(num)
    return lst
print(evenNumLst(11))
print("------------------------")

def oddNumLst(ran):
    lst=[]
    for num in range(ran):
        if num % 2 !=0:
            lst.append(num)
    return lst
print(oddNumLst(11))
