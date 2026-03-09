num1 = (float(input('Enter first number: ')))
num2 = (float(input('Enter second number: ')))

if num1 < num2:
    print(f"The smallest number is {num1}")
if num2 < num1:
    print(f"The smallest number is {num2}")
else:
    print("The numbers are equal")
