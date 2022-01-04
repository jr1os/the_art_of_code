print("Welcome To The Temperature conversion Program.")
temp_f = float(input("what is the given temperature in degrees fahrenheit: "))
temp_c = ((temp_f - 32) * 5) / 9
temp_k = temp_c + 273.15
print(f"Degrees Fahrenheit :\t {temp_f:.4f}")
print(f"Degrees Celcius:\t {temp_c:.4f}")
print(f"Degrees Kelvin:\t\t {temp_k:.4f}")