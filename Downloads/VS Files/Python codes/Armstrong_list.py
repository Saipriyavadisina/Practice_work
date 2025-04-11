list_1 = list(map(str, input().split()))
list_2 = []

for number in list_1:
    sum_of_num = 0
    for i in number:
        sum_of_num += int(i) ** len(number)
    if sum_of_num == int(number):
        list_2.append(number)
    
print(list_2)