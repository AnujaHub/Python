
n = int(input("Enter a number to find factorial: "))
def fact(n):
    for i in range(1,n+1):
      if(n==0 or n==1):
        return 1
      else:
        return n*fact(n-1)
print(fact(n))

fact(n)
