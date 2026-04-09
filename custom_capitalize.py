s = input("Enter string: ")
if s:
    first = s[0]
    rest = s[1:]
    if "a" <= first <= "z":
        first = chr(ord(first) - 32)
    new_rest = ""
    for c in rest:
        if "A" <= c <= "Z":
            new_rest += chr(ord(c) + 32)
        else:
            new_rest += c
    s = first + new_rest
print(s)