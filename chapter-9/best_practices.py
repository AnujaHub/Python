# ✅ Best practices for file handling in Python

# 1️⃣ Use context manager (automatically closes file)
file_path = "example.txt"

# Writing to file
with open(file_path, "w", encoding="utf-8") as f:
    f.write("Hello, this is a sample text.\n")
    f.write("Always close files properly!\n")

# 2️⃣ Reading from file safely
with open(file_path, "r", encoding="utf-8") as f:
    data = f.read()
    print("File content:\n", data)

# 3️⃣ Appending new data
with open(file_path, "a", encoding="utf-8") as f:
    f.write("This line is appended.\n")

# 4️⃣ Using try-except for error handling
try:
    with open("non_existing.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("⚠️ File not found. Please check the path.")

# 5️⃣ Reading line by line (memory efficient)
with open(file_path, "r", encoding="utf-8") as f:
    for line in f:
        print("Line:", line.strip())

# 6️⃣ Reading all lines at once (if file is small)
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()
    print("List of lines:", lines)
