# properties of a set
# 1. unordered
# 2. mutable
# 3. no duplicate items

# EMPPTY SET
empty_set = set()
# USING set{} creats an empty dictionary
# Creating a set
fruits = {"apple", "banana", "mango", "cherry"}
print("Original set:", fruits)

# add()
fruits.add("orange")
print("\nAfter add():", fruits)

# update()
fruits.update(["grape", "kiwi"])
print("After update():", fruits)

# remove()
fruits.remove("banana")   # error if not found
print("\nAfter remove('banana'):", fruits)

# discard()
fruits.discard("pear")    # no error if not found
print("After discard('pear'):", fruits)

# pop()
removed = fruits.pop()
print(f"\nAfter pop(): removed {removed}")
print("Set now:", fruits)

# copy()
copy_fruits = fruits.copy()
print("\nCopy of set:", copy_fruits)

# clear()
fruits.clear()
print("After clear():", fruits)


# --- Set operations ---

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("\nUnion:", a.union(b))
print("Intersection:", a.intersection(b))
print("Difference:", a.difference(b))

