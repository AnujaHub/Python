# Dictionary : collection of key-value pairs

# proerties of dictionary
# 1. unordered      
# 2. mutable
# 3. indexed by keys
# 4. keys are unique

# EMPTY DICTIONARY
empty_dict = {}

# its used bcz its faster : O(1) search time complexity
info = {
    "name": "Sunflower",
    "age": 19,
    "city": "Pune"
}

print("Original dictionary:", info)

# get()
print("\nget():", info.get("age"))
print("get() with default:", info.get("course", "Not Found"))

# keys(), values(), items()
print("\nKeys:", list(info.keys()))
print("Values:", list(info.values()))
print("Items:", list(info.items()))

# update()
info.update({"course": "AI", "city": "Mumbai"})
print("\nAfter update():", info)

# pop()
info.pop("age")
print("\nAfter pop('age'):", info)

# popitem()
info.popitem()
print("\nAfter popitem():", info)

# copy()
copy_info = info.copy()
print("\nCopy of dictionary:", copy_info)

# clear()
info.clear()
print("\nAfter clear():", info)
