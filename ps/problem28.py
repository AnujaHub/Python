source_file = "files/this.txt"
destination_file = "files/copyThis.txt"

try:
    # 1. Open source in read binary mode ('rb')
    with open(source_file, 'rb') as source:
        # 2. Open destination in write binary mode ('wb')
        with open(destination_file, 'wb') as destination:
            # 3. Read content from source and write to destination
            destination.write(source.read())
    
    print("File copied manually using basic I/O.")

except FileNotFoundError:
    print(f"Error: Source file '{source_file}' not found.")