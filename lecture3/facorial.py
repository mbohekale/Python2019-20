def factorialFun(n):
    if n==0:
        return 1
    else:
        return n*factorialFun(n-1)
n = int(input("Enter a number: "))
product =factorialFun(n)
print("The factorial of",n,"is",product)
