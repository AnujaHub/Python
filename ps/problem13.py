dictionary={}

i = 0 
for i in range(4):
    name=input("enter name:")
    lang=input("enter language:")
    dictionary[name] = lang

print(dictionary)


# we need not hande duplicate keys in dictionary
# if we enter same key again, it will update the value of that key
