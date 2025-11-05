# Opening a file
f = open("file.txt", "r")   # modes: "r", "w", "a", "x", "rb", "wb"

# 'r'  → read (file must exist)
# 'w'  → write (creates new / overwrites existing file)
# 'a'  → append (adds data to end)
# 'x'  → create new (error if file exists)
# 'b'  → binary mode (add with others like 'rb', 'wb')
# 't'  → text mode (default)
# 'r+' → read + write (file must exist)
# 'w+' → write + read (overwrites existing)
# 'a+' → append + read (creates if not exists)
# 'rb+' / 'wb+' → read + write in binary mode


# Reading
f.read()       # read entire file
f.readline()   # read one line
f.readlines()  # read all lines as list

# Writing
f.write("Hello")   # write text to file
f.writelines(["a\n", "b\n", "c\n"])  # write list of lines

# Position control
f.tell()       # current file cursor position
f.seek(0)      # move cursor to start (0 means beginning)

# Closing
f.close()      # close file manually

# Check if file is readable or writable
f.readable()   # True if file opened in read mode
f.writable()   # True if file opened in write/append mode
