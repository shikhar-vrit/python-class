num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

if num > 100:
    print(f"{num} is big number")

if num >= 1 and num <= 10:
    print(f"{num} is small number.")

