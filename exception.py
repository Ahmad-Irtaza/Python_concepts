def divide_numbers(dividend, divisor):
    try:
        result = dividend / divisor
        print(f"Result of division: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

try:
    dividend = float(input("Enter the dividend: "))
    divisor = float(input("Enter the divisor: "))
    divide_numbers(dividend, divisor)
except ValueError:
    print("Error: Please enter valid numeric values.")
except Exception as e:
    print(f"An unexpected error occurred during input: {e}")
