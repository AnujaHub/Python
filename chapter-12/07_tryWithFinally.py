try:
    a = int(input("enter number"))
    print(a)
    
except Exception as e:
   print(e)


finally :
    print("this is finally")
# always runs , even if function returns 
# then why not write it like normal print stmt ?
# bcz if a function returns a value the control is transffered outside the function
# and normla pritn stmt won't work , but a finally block would work at any cost
