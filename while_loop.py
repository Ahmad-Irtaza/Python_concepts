countdown_start = int(input("Enter a number to start the countdown: "))

while countdown_start <= 0:
    print("Please enter a positive number.")
    countdown_start = int(input("Enter a number to start the countdown: "))

while countdown_start > 0:
    print(countdown_start)
    countdown_start -= 1

print("finish")
