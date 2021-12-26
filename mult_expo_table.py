print("Welcome to the Multiplication/Exponent Table App")

name = input("Hello, What is your name: ").strip()
number = float(input("What number would you like to work with: "))

print(f"Multiplication table for {number}")

for n in range(10):
    print(f"{n} * {number} = {n*number:.2f}")

print(f"Exponent Table for {number}")

for i in range(10):
    print(f"{number} ** {i} = {number**i:.4f}")

message = f"{name} Math is cool"

print(message.title())
print(f"\t {message.lower()}")
print(f"\t\t {message.capitalize()}")

