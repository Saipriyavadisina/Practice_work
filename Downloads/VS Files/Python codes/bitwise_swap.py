a, b = map(int, input().split())
a = a ^ b
b = a ^ b
a = b ^ a
print(a, b)