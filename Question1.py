total = 0
for i in range(1, 6):
    marks = float(input(f"Enter marks of subject {i} (out of 100): "))
    total += marks

percentage = total / 500 * 100

if percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

result = "Pass" if percentage >= 50 else "Fail"

print("Total marks:", total, "/ 500")
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)
print("Result:", result)
