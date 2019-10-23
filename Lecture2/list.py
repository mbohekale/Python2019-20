myList = [1,10,3,12,13,42]
length = (len(myList))
print(length//2)

for i in range(length//2):
    myList[i],myList[length - i -1]= myList[length - i-1],myList[i]
print(myList)
