Upper_Case_Count = 0
Lower_Case_Count = 0
Digit_Count = 0 
Special_Character_Count = 0

PSWD = input("ENTER PASSWORD (Lenght 6-16)\n: ")

if len(PSWD) < 6:
    print("Password to short !!")
elif len(PSWD) > 16:
    print("Password to long !!")
else:
    for i in PSWD:
        if i.isalpha():
            if i.isupper():
                Upper_Case_Count +=1
            elif i.islower():
                Lower_Case_Count += 1
        elif i.isdigit():
            Digit_Count +=1
        else:
            Special_Character_Count += 1

    # check password pattern
    if Upper_Case_Count == 0 or Lower_Case_Count == 0 or Digit_Count == 0 or Special_Character_Count == 0:
        print("Weak Password !!! (suggest password include Upper, Lower, Number and Symbol)")
    else:
        print("Strong Password :)")
        