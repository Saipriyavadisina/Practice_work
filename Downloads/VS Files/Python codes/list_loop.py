n = list(map(int, input().split()))
list_1 = []
for j in n:
    if j%2 != 0:
        x = j ** 2
        list_1.append(x)
print(list_1)