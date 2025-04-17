def is_even(num):
    if num % 2 == 0:
        return "is even."
    else:
        return "is odd."
number = int(input())
print(number, is_even(number))