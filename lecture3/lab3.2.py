def daysInMonth(year,month):
    leap = False
    if year%400==0:
        leap = True
    elif year%100==0:
        leap = False
    elif year%4==0:
        leap = True
    return leap
testYears =[1900, 2000, 2016, 1987]
testMonths = [2,2,1,11]
testResults= [28, 29, 31,30]
for i in range(len(testYears)):
    yr = testYears[i]
    mo = testMonths[i]
    print(yr,mo,"->",end="")
    result = daysInMonth(yr,mo)
    if result==testResults[i]:
        print("Failed")
    else:
        print("OK")

    
    


