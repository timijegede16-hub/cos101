first_number = float(input("Enter the first number: "))
second_number = float(input("Enter second number: "))
operations = input(" Choose from +, -, *, / : ")

if operations == "+":
    result= first_number + second_number
    print(f"{first_number} + {second_number} = {result}")
    
elif operations=="-":
    result=first_number - second_number
    print(f"{first_number} - {second_number} = {result}")

    
elif operations =="*":
    result=first_number*second_number
    print(f"{first_number} * {second_number} = {result}")

    
elif operations=="/":
    if second_number == 0:
        print("number cant be divided by 0")
    else:
        result=first_number / second_number
        print(f"{first_number} / {second_number} = {result}")
