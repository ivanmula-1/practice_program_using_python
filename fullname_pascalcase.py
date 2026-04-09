fullname = input("Enter your fullname: ")
pascal = ''.join(word.capitalize() for word in fullname.split())
print(pascal)