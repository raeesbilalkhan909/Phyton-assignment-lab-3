numbers = []
for i in range(10):
    numbers.append(float(input(f"Enter number {i + 1}: ")))

even = 0
odd = 0
for n in numbers:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1

print("Sum:", sum(numbers))
print("Average:", sum(numbers) / len(numbers))
print("Largest number:", max(numbers))
print("Smallest number:", min(numbers))
print("Even numbers:", even)
print("Odd numbers:", odd)
