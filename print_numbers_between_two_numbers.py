num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

start = min(num1, num2)
end = max(num1, num2)

for num in range(start + 1, end):
    print(num)