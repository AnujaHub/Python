a = "yo"
b = 'yo'
c = """yo"""
d = '''yo'''
# zero based indexing
# strings in python are immutable , you cannot change them in place
# e/g a[0] = 'y' # this will raise an error

print(length := len(a))

# slicing a string
name = "sunflower"
print(name_slice := name[0:3]) #[0,3)
print(name_slice2 := name[3:9]) #[3,9)

# while solving negative indexing problems convert -ve to +ve 

# negative slicing
# print(neg_slice := name[-6:-1]) 
print(neg_slice := name[-6:])  #since last index is omitted 
print(neg_slice := name[-9:-6]) 

# slicing with skip value 
