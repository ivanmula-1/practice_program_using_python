s = input("Enter string: ")
width = int(input("Enter total width: "))
if len(s) < width:
    s = s + " " * (width - len(s))
print(f"'{s}'")