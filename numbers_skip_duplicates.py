numbers = []

for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
    seen = []
    for n in numbers:
        if n not in seen:
            print(n)
            seen.append(n)