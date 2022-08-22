num1 = input("Enter the first number: ")
num1 = float(num1)
op = input("Enter operator : ")
num2 = input("Enter the second number: ")
num2 = float(num2)
if op=="+":
    print(num1+num2)
elif op=="-":
    print(num1-num2)
elif op=="*":
    print(num1*num2)
else:
    print(num1/num2)
