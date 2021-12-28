print("Welcome to the grade sorter App")

grade = []
for g in range(1,5):
    grade.append(int(input(f"What is your {g} # (0-100): ")))

print(f"Your grades are: {grade}")
grade.sort(reverse=True)
#grade.reverse()
print(f"Your grades from highest to lowest are: {grade}")

print("The lowest to grades will now be dropped")
print(f"Remove grade: {grade.pop()}")
print(f"Remove grade: {grade.pop()}")

print(f"Your remaining grades are: {grade}")

print(f"Nice Work!, Your highest grade is a: {grade[0]}")