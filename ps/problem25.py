
with open("files/poems.txt") as f:
    content = f.read()

    index = content.find("twinkle")

    print(f"found at {index}")


