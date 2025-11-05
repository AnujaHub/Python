# patterns ahhhhhh

# n = 5
# for i in range(n):              # outer loop for rows
#     for j in range(n - i - 1):  # inner loop for spaces
#         print(" ", end="")
#     for k in range(2 * i + 1):  # inner loop for stars
#         print("*", end="")
#     print()  # move to next line


# n = 5
# i = 0
# for i in range(n):
#     print(" " * (n - i - 1) + "*" * (2 * i + 1))


# n = 3
# for i in range(n):
#     for j in range(i+1):
#         print("*", end="")
#     print("\n")


n = 5

# * * *
# *   *
# * * *

for i in range(n):
    for j in range(n):
        if j == 0 or j == n - 1 or i == 0 or i == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()