# s = input()
# s1 = ""
# for i in s:
#     s1 = i + s1
# print(s1)
num1 = int(input())
num2 = 0
while num1 > 0:
    digit = num1 % 10
    num2 = num2 * 10 + digit
    num1 = num1 // 10
print(num2)