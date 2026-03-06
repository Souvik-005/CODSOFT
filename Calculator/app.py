print("...Welcome to My Calculator...")

while True:   
    try:   
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division ")
        print("5. Remainder")
        print("6. Exit")
        choice=int(input("Choose your Operation to perform: "))
        if choice == 1:
            Op1=int(input("Enter 1st Number:: "))
            Op2=int(input("Enter 2nd Number:: "))
            print(f"The Addition of {Op1} and {Op2} is: {Op1+Op2}")
        elif choice == 2:
            Op1=int(input("Enter 1st Number:: "))
            Op2=int(input("Enter 2nd Number:: "))   
            print(f"The Subtraction of {Op1} and {Op2} is: {Op1-Op2}")
        elif choice == 3:
            Op1=int(input("Enter 1st Number:: "))
            Op2=int(input("Enter 2nd Number:: "))
            print(f"The Multiplication of {Op1} and {Op2} is: {Op1*Op2}")
        elif choice == 4:
            Op1=int(input("Enter 1st Number:: "))
            Op2=int(input("Enter 2nd Number:: "))
            if Op2 == 0:
                print("Can't Divide by Zero.")
            else:
                print(f"The Division of {Op1} and {Op2} is: {Op1/Op2}")
                print(f"The Integer Division of {Op1} and {Op2} is: {Op1//Op2}")
        elif choice == 5:
            Op1=int(input("Enter 1st Number:: "))
            Op2=int(input("Enter 2nd Number:: "))
            if Op2 == 0:
                print("Can't Divide by Zero.")
            else:
                print(f"The Remainder of {Op1} and {Op2} is: {Op1%Op2}")   
        elif choice == 6:
            print("Thank you...")
            break
        else:
            print("Invalid Choice , please Select the right Choice.")
    except ValueError:
        print("Enter a Valid Input.")