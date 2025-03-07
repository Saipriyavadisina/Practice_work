def safe_division():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
        print(f"Result: {result}")
    except ValueError:
        print("Error: Please enter valid numbers!")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    finally:
        print("Thank you for using the calculator!")
safe_division()