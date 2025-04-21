def is_prime(num):
    if num <= 1:
        return "Not a prime"
    for i in range(2, num):
        if num % i == 0:
            return "Not a prime"
    return "Prime"
    
number = int(input())
print(is_prime(number))