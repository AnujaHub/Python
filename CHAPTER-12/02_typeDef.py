from typing import List,Tuple, Dict,Union


# type definitions
n : int = 5
# we are simpply letting compiler know data type 
# increases readability 

def sum(a: int , b:float) ->float:
    return a+b

print(sum(4,4.3))


# by importing from typing , 
# you can create well defined built in data types

# list of integers 
numbers: List[int] = [1,2,3,4,5]

# tuple of string & integers
person: Tuple[str,int] = ("sun" , 90)


