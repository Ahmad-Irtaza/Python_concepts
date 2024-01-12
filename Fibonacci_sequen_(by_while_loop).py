# Get the limit for the Fibonacci sequence from the user
limit = int(input("Enter the limit for the Fibonacci sequence: "))

# Validate the input
while limit <= 0:
    print("Please enter a positive number as the limit.")
    limit = int(input("Enter the limit for the Fibonacci sequence: "))
a, b = 0, 1

fibonacci_sequence = [a, b]
while a + b <= limit:
    a, b = b, a + b
    fibonacci_sequence.append(b)


print("Fibonacci sequence up to the limit:")
print(fibonacci_sequence)
