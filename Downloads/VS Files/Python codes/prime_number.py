num = int(input())
is_prime = True
if num <= 1:
    is_prime = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
print(f"{num} is {'a prime' if is_prime else 'not a prime'} number")