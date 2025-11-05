a = ( "name" , 30 , False , 79.6)
print(type(a))

b=(1)
print(type(b))
b=(1,) # to make a single item tuple , we need to add a comma
print(type(b))

# a[0] = "new name" # this will raise an error , because tuples are immutable

print(a.count(30))

# Tuple example
tup = (3, 1, 4, 1, 5, 9, 2, 6, 5)

print("Tuple:", tup)

# Methods
print("Count of 5:", tup.count(5))
print("Index of first 1:", tup.index(1))

# Built-in functions
print("Length:", len(tup))
print("Max value:", max(tup))
print("Min value:", min(tup))
print("Sum:", sum(tup))
print("Sorted tuple:", sorted(tup))  # returns a list

# Operations
tup2 = (10, 20)
print("Concatenation:", tup + tup2)
print("Repetition:", tup * 2)


# existing tuple stays the sameeeeeee