li = list(map(int, input().split()))
li_1 = []
li_2 = []
for i in li:
    if i % 2 == 0:
        li_1.append(i)
    else:
        li_2.append(i)
        
li_1.sort()
li_2.sort(reverse = True)

print(li_1)
print(li_2)