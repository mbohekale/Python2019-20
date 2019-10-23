def listUpdater(lst):
    updList= []
    for elem in lst:
        elem**= 2
        updList.append(elem)
        return updList
list1=[1, 2, 3, 4, 5]
print(listUpdater(list1))
