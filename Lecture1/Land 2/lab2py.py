john=3
mary=5
adam=6
TotalApple=john+mary+adam
print('john have:',john ,'mary have:',mary,'adam have:',adam,sep=",")
print('TotalApple is:' "=" ,john+mary+adam)
print(TotalApple)
print()
john='3'
mary='5'
adam='8'
totalApple=john+adam+ mary
print(totalApple)
#TypeError: Can't convert 'int' object to str implicitly
print(totalApple+TotalApple)
