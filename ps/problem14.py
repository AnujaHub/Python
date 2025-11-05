s = {8,7,12 , "sun" , {1,2}}
 # sets cannot contain other sets, lists, or dicts 
# Sets can only have hashable & immutable elements
# lists, dicts are mutable but not hashable
s.replace(1,"one")
print(s)


# thoda gyaan

# Mutability tells whether an object’s value can change after creation

# Hashability tells whether an object can be used as a set element or dict key
# An object is hashable if it has a hash value that remains constant during its lifetime
