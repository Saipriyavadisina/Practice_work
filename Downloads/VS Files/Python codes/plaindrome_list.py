list_1 = list(map(str, input().split()))
list_2 = []
for i in list_1:
    if i == i[::-1]:
        list_2.append(i)
print(list_2)