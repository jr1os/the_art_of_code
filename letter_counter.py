
name = input("what is your name: ").title().strip()
print(f"Hello {name}")
print("I will count the number of time that a specific letter occurs a message")
message = input("Please enter a message: ").lower()
letter_occurs = input("Wich letter would you like to count the occurences of: ").lower()
counter = message.count(letter_occurs)
"""
for letter in message:
    if letter ==  letter_occurs:
        counter += 1
        """

    
print(f"{name} your message has {counter} {letter_occurs}'s in it")