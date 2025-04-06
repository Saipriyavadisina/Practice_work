def odd_num(n):
    for i in range(n):
        if i % 2 == 0:
            continue
        print(i, end =" ")
   
x = int(input())
odd_num(x)