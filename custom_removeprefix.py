s = input("Enter string: ")
prefix = input("Enter prefix to remove: ")
if s[:len(prefix)] == prefix:
    s = s[len(prefix):]
print(s)