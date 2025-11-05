# username validation

username = input("Enter your username:")

while(len(username)<10):
    print("username must be at least 10 characters")
    username = input("Enter your username:")