# rename a file

import os

# Current file name
old_name = "files/old_file.txt"
# New file name
new_name = "files/new_file.txt"

# Rename file
os.rename(old_name, new_name)
print("File renamed successfully!")
