print("...Welcome to My Calculator...")

while True:   
    try:   
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division ")
        print("5. Remainder")
        print("6. Exit")
        Op1=int(input("Enter 1st Number:: "))
        Op2=int(input("Enter 2nd Number:: "))
        choice=int(input("Choose your Operation to perform: "))
        if choice == 1:
            print(f"The Addition of {Op1} and {Op2} is: {Op1+Op2}")
        elif choice == 2:
                print(f"The Subtraction of {Op1} and {Op2} is: {Op1-Op2}")
        elif choice == 3:
            print(f"The Multiplication of {Op1} and {Op2} is: {Op1*Op2}")
        elif choice == 4:
            if Op2 == 0:
                print("Can't Divide by Zero.")
            else:
                print(f"The Division of {Op1} and {Op2} is: {Op1/Op2}")
                print(f"The Integer Division of {Op1} and {Op2} is: {Op1//Op2}")
        elif choice == 5:
            if Op2 == 0:
                print("Can't Divide by Zero.")
            else:
                print(f"The Remainder of {Op1} and {Op2} is: {Op1%Op2}")   
        elif choice == 6:
            break
        else:
            print("Invalid Choice , please Select the right Choice.")
    except ValueError:
        print("Enter a Valid Input.")
print("Thank you...")