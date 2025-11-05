# replacing unwanted words

li =["donkey" , "monkey" , "bad" , "dark" , "eww" , "gross"]
with open("files/donkey.txt") as f:
        content = f.read()

for word in li:
    content = content.replace(word , "***")

with open("files/donkey.txt" , "w") as f :
    f.write(content)
        
    