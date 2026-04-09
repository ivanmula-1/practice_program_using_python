fullname = input("Enter your fullname: ")
snake = '_'.join(word.lower() for word in fullname.split())
print(snake)
