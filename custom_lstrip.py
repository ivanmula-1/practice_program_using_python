s = input("Enter string with leading spaces: ")
i = 0
while i < len(s) and s[i] == " ":
    i += 1
print(s[i:])