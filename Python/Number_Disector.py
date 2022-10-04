#Name:Ashish Ramesh
#Github ID : AshishRamesh

import random
input_1 = input('Enter the value between 1 to 60 : ')

#Checks if input is between 0 and 60
if int(input_1) <= 60 and int(input_1) > 0 :
    print('Ok')
    c = int(input_1) / 2
    c = round(c)
    
    #Checks if c is less than 20 and if it isnt than reduces it to less than 20 for b
    if c > 20:
        b = c - 20
        a = int(input_1) - c - b
        if a > 20:
            e = (a - 20)
            a = a - e
            b = b + e
        print(f'a = {a} , b = {b} , c = {c}')
        d = a+b+c
        print('The sum of a,b,c is = '+ str(d))
    
    #If c < 20 than c is subtracted with a random number and the value is assigned to b
    else:
        b = c - random.randint(0,10)
        a = int(input_1) - c - b
        print(f'a = {a} , b = {b} , c = {c}')
        d = a+b+c
        print('The sum of a,b,c is = '+ str(d))
else:
    print('Cannot compute!!!!')
    exit()