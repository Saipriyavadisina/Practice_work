number = input()
sum_of_number = 0
for i in number:
    sum_of_number += int(i) ** len(number)
if sum_of_number == int(number):
    print(number, "is Armstrong number")
else:
    print(number, "is not Armstrong number")