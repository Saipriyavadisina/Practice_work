list_1 = list(map(str, input().split()))
list_2 = []
for num in list_1:
    if num.isdigit() and all(int(i) % 2 == 0 for i in num):
        list_2.append(num)
print(list_2)