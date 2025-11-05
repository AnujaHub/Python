'''
RAM:
volatile - data doesn't persist

type :
text files 
binary files
'''

# read
# f = open("chapter-9/file.txt")  
# data = f.read()
# print(data)
# f.close()  


# write , must open file in write
a = " hey hello hi"
# this was made in runtime
f = open("chapter-9/new.txt", "w")
f.write(a)
f.close()
         

f = open("chapter-9/new.txt")
data = f.read()
print(data)
f.close() 