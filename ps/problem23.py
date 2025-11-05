
n = int(input("enter n:"))

# range(start, stop, step)

def print_pattern(n):
    for i in range(n, 0 , -1):
         print("*" * i)

print_pattern(n)