s = input("Enter string: ")
result = ""
for c in s:
    if "A" <= c <= "Z":
        result += chr(ord(c) + 32)
    elif "a" <= c <= "z":
        result += chr(ord(c) - 32)
    else:
        result += c
print(result)