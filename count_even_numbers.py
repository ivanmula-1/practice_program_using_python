count_even = 0
for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    if num % 2 == 0:
        count_even += 1

print(f"Total even numbers: {count_even}")