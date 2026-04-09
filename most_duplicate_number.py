numbers = []

while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        break
if numbers:
    most_dup = max(set(numbers), key=numbers.count)
    print("Number with most duplicates:", most_dup)

