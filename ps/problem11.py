dictionary = {
    "namaste": "hello",
    "dost": "friend",
    "shukriya": "thank you"
}

find = input("Enter a Hindi word whose translation you want to find: ")
print(dictionary.get(find))# returns 'friend'

