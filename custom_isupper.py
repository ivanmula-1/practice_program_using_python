s = input("Enter string: ")
is_upper = all(not c.isalpha() or "A" <= c <= "Z" for c in s)
print(is_upper)
