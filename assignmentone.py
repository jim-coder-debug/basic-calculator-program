print("this is a simple calculator")

num1=float(input("enter the first number:"))
num2=float(input("enter the second number:"))

operator=input("input the operation for calculation either +, -, /, * :")

if operator is '+' :
    result=num1 +num2
    print(result)
elif operator is '-':
    result =num1 -num2
    print(result)
elif operator is '*':
    result= num1 * num2
    print(result)
elif operator is '/':
    result=num1/num2
    print(result)
else:
    print("invalid input")

