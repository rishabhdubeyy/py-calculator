def add(num1, num2):
    return num1 + num2

def subtract(num1 , num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1 , num2):
    return num1 / num2

print("Please select Mode: \n" \
    "1. Add \n" \
    "2. Subtract \n" \
    "3. Multiply \n" \
    "4. Divide")

Select= int(input("please select 1,2,3,4: "))

Number_1 = int(input("Enter Number 1: "))
Number_2 = int(input("Enter Number 2: "))

if Select == 1:
    print('Answer is: ', Number_1, '+', Number_2, '=', add(Number_1, Number_2))

elif Select == 2:
    print('Answer is: ', Number_1, '-', Number_2, '=', subtract(Number_1, Number_2))

elif Select == 3:
    print('Answer is: ', Number_1, '*', Number_2, '=', multiply(Number_1, Number_2))

elif Select == 4:
    print('Answer is: ', Number_1, '/', Number_2, '=', divide(Number_1, Number_2))

else:
    print("Invalid Info")
