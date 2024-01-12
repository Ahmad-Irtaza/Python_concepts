limit = int(input("Enter the limit for the Fibonacci sequence: "))

while limit <= 0:
    print("Please enter a positive number as the limit.")
    limit = int(input("Enter the limit for the Fibonacci sequence: "))

fibonacci_sequence = [0, 1]

a, b = 0, 1
for _ in range(2, limit):
    a, b = b, a + b
    if b > limit:
        break
    fibonacci_sequence.append(b)

print("Fibonacci sequence up to the limit:")
print(fibonacci_sequence)
