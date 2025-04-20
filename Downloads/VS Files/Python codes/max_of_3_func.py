def max_of_three(a,b,c):
    result = max(a, b, c)
    return result
a, b, c = map(int, input().split())
print(max_of_three(a, b, c))