#function add
def add():
    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))
    return n1+n2
  
#function substract
def subtract():
    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))
    return n1 - n2

#function multiply
def multiply():
    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))
    return n1 * n2

#function dividen
def divide():
    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))
    return n1 / n2

#add input
if __name__ == "__main__":
    while True:    
        choice = input("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit\n")

        if choice == '1':
            print("The sum is:",add())

        elif choice == '2':
            print("The difference is:",subtract())
        
        elif choice == '3':
            print("The product is:",multiply())
        
        elif choice == '4':
            print("The quotient is:",divide())
        
        elif choice == '5':
            break
        
        else:
            print("Enter correct choice!!")
