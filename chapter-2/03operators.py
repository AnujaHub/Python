# arithematic operators
a = 10
b = 3
c = 5
print("a + b =", a + b)  # addition
print("a - b =", a - b)  # subtraction  
print("a * c =", a * c)  # multiplication
print("a / b =", a / b)  # division         
print("a % b =", a % b)  # modulus
print("a ** b =", a ** b)  # exponentiation
print("a // b =", a // b)  # floor division

# comparison operators
print("a == b:", a == b)  # equal to
print("a != b:", a != b)  # not equal to
print("a > b:", a > b)    # greater than
print("a < b:", a < b)    # less than
print("a >= b:", a >= b)  # greater than or equal to
print("a <= b:", a <= b)  # less than or equal to


# logical operators
x = True
y = False
print("x and y:", x and y)  # logical AND
print("x or y:", x or y)    # logical OR
print("not x:", not x)      # logical NOT

# assignment operators
d = 5
print("Initial value of d:", d)
d += 3
print("After d += 3:", d)
d *= 2
print("After d *= 2:", d)
d -= 4
print("After d -= 4:", d)
d /= 2
print("After d /= 2:", d)
d %= 3
print("After d %= 3:", d)
d **= 2
print("After d **= 2:", d)
d //= 2
print("After d //= 2:", d)

# bitwise operators
p = 6  # in binary: 110
q = 3  # in binary: 011
print("p & q =", p & q)  # bitwise AND
print("p | q =", p | q)  # bitwise OR
print("p ^ q =", p ^ q)  # bitwise XOR
print("~p =", ~p)        # bitwise NOT
print("p << 1 =", p << 1)  # left shift
print("p >> 1 =", p >> 1)  # right shift
# identity operators
m = [1, 2, 3]
n = m
o = [1, 2, 3]
print("m is n:", m is n)  # True, because n references the same object as m
print("m is o:", m is o)  # False, because o is a different object

# membership operator
fruits = ["apple", "banana", "cherry"]
print("banana in fruits:", "banana" in fruits)  # True
print("grape not in fruits:", "grape" not in fruits)  # True

# operator precedenc
result = 10 + 5 * 2 ** 2  # exponentiation first,
print("Result of 10 + 5 * 2 ** 2 =", result)  # then multiplication, then addition
# parentheses to change precedenc
result = (10 + 5) * 2 ** 2
print("Result of (10 + 5) * 2 ** 2 =", result)  # parentheses first, then exponentiation, then multiplication
