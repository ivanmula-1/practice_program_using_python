numbers = []

while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        break
if numbers:
    avg = sum(numbers) / len(numbers)
    print("Average:", avg)