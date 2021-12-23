print("Welcome to the MPH to MPS Conversion app")  
mph = float(input("What is your speed in miles per hour: "))
mps = mph * 0.44704
# mps = round(mps, 2) other option.
print(f"Your speed in meters per second is {mps:.2f}")