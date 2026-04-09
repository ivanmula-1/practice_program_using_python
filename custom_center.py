s = input("Enter string: ")
width = int(input("Enter total width: "))
if len(s) < width:
    total_space = width - len(s)
    left_space = total_space // 2
    right_space = total_space - left_space
    s = " " * left_space + s + " " * right_space
print(f"'{s}'")
