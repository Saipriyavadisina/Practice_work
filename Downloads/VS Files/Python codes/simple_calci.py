num1 = float(input())
op = input()
num2 = float(input())
if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '*':
    print(num1 * num2)
elif op == '/':
    if num2 != 0:
        print(num1/num2)
    else:
        print("Not divisible by 0")
else:
    print("Invalid Operator")