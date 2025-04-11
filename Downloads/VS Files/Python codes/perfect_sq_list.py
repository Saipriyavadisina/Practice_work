from math import sqrt
list_1 = list(map(int, input().split()))
list_2 = []
for number in list_1:
    if int(sqrt(number)) ** 2 == number:
        list_2.append(number)
print(list_2)