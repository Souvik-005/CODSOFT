import random
import string

try:
    chars1=string.ascii_letters + string.digits + string.punctuation
    chars2=string.ascii_letters + string.digits
    password=""
    length=int(input("Enter the length of password:: "))
    print("The complexity of the password : ")
    print("1. Low ")
    print("2. Moderate ")
    print("3. Strong ")
    complexity=int(input(" Choose between 1 & 2 & 3 : "))
    if complexity == 1:
        for i in range(length):
            password += random.choice(chars2)
        print(f"Generate Password : {password}")
    elif complexity == 2:
        if length < 2:
            print("Password length must be at least 2 for Moderate complexity.")
        else:
            password += random.choice(string.ascii_uppercase)
            password += random.choice(string.digits)
            for i in range(length-2):
                password += random.choice(chars2)
            temp_list=list(password)
            random.shuffle(temp_list)
            temp_password="".join(temp_list)
            print(f"Generate Password : {temp_password}")
    elif complexity == 3:
        if length < 4:
            print("Password length must be at least 4 for strong complexity.")
        else:
            password += random.choice(string.ascii_uppercase)
            password += random.choice(string.ascii_lowercase) 
            password += random.choice(string.digits)
            password += random.choice(string.punctuation)
            for i in range(length-4):
                password += random.choice(chars1)
            temp_list=list(password)
            random.shuffle(temp_list)
            temp_password="".join(temp_list)
            print(f"Generate Password : {temp_password}")
    else:
        print("Invalid input , choose between 1 & 2 & 3 .")


except ValueError as e:
    print(f"There is an error: Please enter valid input.")

