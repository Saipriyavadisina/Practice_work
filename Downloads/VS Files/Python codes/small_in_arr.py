arr = list(map(int, input().split()))
small = arr[0]
big = arr[0]
for i in arr:
    if i < small:
        small = i
    
    if i > big:
        big = i
print("biggest in array is :", big)
print("smallest of array is :", small)