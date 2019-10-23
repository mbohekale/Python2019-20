secret_number = 777
number = int(input("Enter a number:"))
while secret_number != number:
    print('Ha Ha')
    secret_number -= 1
    if secret_number == number:
        break
print("and the magician should say the following words: "
              ,"Well done muggle! You are free now.")
    
    
