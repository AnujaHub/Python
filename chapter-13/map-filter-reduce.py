l = [1,2,3,4,5]

# lambda function takes x and returns x*X
square = lambda x: x*x


# applies a function to every item in an iterable (like a list or tuple)
sqList = map(square, l)
print(list(sqList))