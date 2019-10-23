def sum(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)
sum(2,3,4)
print('-----------')
def intro(a="James Bond", b="Bond"):
    print("My name is", b + ".", a + ".")
intro()
print('-----------')
def intro(a, b="Bond"):
    print("My name is", b + ".", a + ".")
intro("Susan")
print('-----------')
#def sum(a, b=2, c):
#   print(a + b + c)
#sum(a=1, c=3)
print('------------')
def intro(a="James Bond", b="Bond"):
    print("My name is", b + ".", a + ".")
intro(b="Sean Connery")
