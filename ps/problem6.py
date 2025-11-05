# detecing double spaces 
string ="double   spaces"
# count=0
# for i in range(len(string)-1):
#     if(string[i]=="  "):
#         count+=1


# if(count>1):
#     print("double space detecetd")

print(string.find("  "))


# replaciing double spaces with single space
# string=string.replace("  " , " ") #this ain't work strings immutable hoti ha
print(string.replace("  " , " "))
print(string)