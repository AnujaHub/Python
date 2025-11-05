
data = ["name" , 30 , False , 79.6]

print(data)
print(data[0])
# we could do this in string , 
# but assigning a new item to a string is not possible , 
# because strings are immutable

# this is how we assign a new item to a list
data.append("new id") #at end
print(data)
data.insert(1 , "new name") # at index 1
print(data)
numbers=[4,67,8939,68]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
data.remove(False) #pop
print(data)
