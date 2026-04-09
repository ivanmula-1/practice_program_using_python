numbers = []

while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        break
numbers.sort(reverse=True)
print("Numbers from highest to lowest:", numbers)