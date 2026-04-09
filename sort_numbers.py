numbers = []

while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        break
numbers.sort()
print("Numbers from lowest to highest:", numbers)