# try:
#     a = int(input("enter number"))
#     print(a)
# except Exception as e:
#    print(e)


# 1. ZeroDivisionError
try:
    x = 5 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

# 2. FileNotFoundError
try:
    f = open("nofile.txt")
except FileNotFoundError:
    print("File not found!")

# 3. ValueError
try:
    num = int("abc")
except ValueError:
    print("Invalid value for conversion!")

# 4. TypeError
try:
    result = "2" + 2
except TypeError:
    print("Can't add string and number!")

# 5. IndexError
try:
    li = [1, 2, 3]
    print(li[5])
except IndexError:
    print("Index out of range!")

# 6. KeyError
try:
    d = {"name": "Sunflower"}
    print(d["age"])
except KeyError:
    print("Key not found in dictionary!")
