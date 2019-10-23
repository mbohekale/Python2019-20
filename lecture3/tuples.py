myTuple= (1, 10, 100,1000)
print(myTuple[0])
print(myTuple[1])
print(myTuple[1:])
print(myTuple[:-2])
for elem in myTuple:
      print(elem)
print('---------')

var = 123
t1 = (1, )
t2 = (2, )
t3 = (3,var)
t1, t2, t3 = t2, t3, t1
print(t1, t2,t3)
