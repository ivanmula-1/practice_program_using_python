custom_endswith.pys = input("Enter string: ")
suffix = input("Enter suffix: ")
if s[-len(suffix):] == suffix:
    print(True)
else:
    print(False)