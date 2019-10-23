##Your task is to:
##step 1:create an empty list named beatles
##step 2: use the append() method to add the
##list: John,Lennon, Paul McCartney, and George Harrison;
##step 3: use the for loop and the append()method to prompt the user to add the
##following members of the band to the list: Stu,Sutcliffe, and Pete Best;
##step 4: use the del instruction to remove Stu,Sutcliffe and Pete Best from the list;
##step 5: use the insert() method to add Ringo
##Start to the beginning of the list.
beatles =[]
l2=beatles
beatles.append('John')
beatles.append('Lennon')
beatles.append('Paul McCartney')
beatles.append('George Harrison')
print(beatles)
print('-------------')
list1=[]
name = int(input("Enter the length of list: "))
print("Enter names: ")
for i in range(name):
    data=input()
    beatles.append(data)
    
    
