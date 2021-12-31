import math
print("Welcome to the right triangle solver App")

side_a = float(input("What is the first leg of the triangle: "))
side_b = float(input("What is the second leg of the triangle: "))


hypotenuse = math.sqrt((side_a**2) + (side_b**2))
area = (side_a * side_b) / 2

print(f"For a triangle with leg of {side_a} and {side_b} the hypotenuse is: {hypotenuse:.2f}")
print(f"For a triangle with leg of {side_a} and {side_b} the area is: {area:.2f}")