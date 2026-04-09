numbers = []

for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
duplicates = [n for n in numbers if numbers.count(n) > 1]
duplicates = list(dict.fromkeys(duplicates))
print("Numbers with duplicates:", duplicates)