li_1 = list(map(int, input().split()))
new_li_1 = []
for i in li_1:
    if i > 50:
        new_li_1.append(i * i)
print(li_1)
print(new_li_1)