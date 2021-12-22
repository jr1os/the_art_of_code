
name = input("what is your name: ")
print(f"Hello {name}")
print("I will count the number of time that a specific letter occurs a message")
message = input("Please enter a message: ")
counter = 0
letter_occurs = input("Wich letter would you like to count the occurences of: ")
for letter in message:
    if letter ==  "h":
        counter += 1
    
print(f"{name} your message has {counter} {letter}'s in it")