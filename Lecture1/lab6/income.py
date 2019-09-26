income = int(input("Enter the income : "))
if income < 85.525:
    tax = 18/100*income - 556.2
if income > 85.525:
    tax = 14,839.2 + 32/100*income + 85.528

print("The tax is: ",round(tax,0),"Thalers")
