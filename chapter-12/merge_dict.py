dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 9, 'c': 3}

# The | operator creates a new dictionary.
# Values from the second dictionary (dict2) override those in the first (dict1).
merged_dict = dict1 | dict2

print(merged_dict)
# Output: {'a': 1, 'b': 9, 'c': 3}