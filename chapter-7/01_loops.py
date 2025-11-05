# 1️⃣ For loop
for i in range(3):
    print("For loop:", i)

# 2️⃣ For-each loop (list iteration)
fruits = ["apple", "mango", "banana"]
for fruit in fruits:
    print("Fruit:", fruit)

# 3️⃣ While loop
count = 0
while count < 3:
    print("While loop:", count)
    count += 1

# 4️⃣ Nested loops
for i in range(2):
    for j in range(2):
        print(f"Nested loop: i={i}, j={j}")

# 5️⃣ Break statement : completely exits the current loop
for i in range(5):
    if i == 3:
        break
    print("Break example:", i)

# 6️⃣ Continue statement : skips the current iteration and continues with the next
for i in range(5):
    if i == 2:
        continue
    print("Continue example:", i)

# 7️⃣ Else with loop (executes if loop completes normally)
for i in range(3):
    print("Loop:", i)
else:
    print("Loop ended without break")

# 8️⃣ Infinite loop (commented out to prevent execution)
# while True:               
#     print("This is an infinite loop")
