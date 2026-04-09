numbers = []

while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        break
while True:
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        break

    if num in numbers:
        print("Duplicate")
    else:
        print("Unique")
        numbers.append(num)