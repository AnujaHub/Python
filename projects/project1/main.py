'''
1 - Snake 
-1 - Water 
0 - Gun
'''

import random

# Mapping
dic = {"s": 1, "w": -1, "g": 0}
rev_dic = {1: "Snake", -1: "Water", 0: "Gun"}  # reverse mapping

# Computer's random choice
computer = random.choice(list(dic.keys()))
computer_val = dic[computer]

# User input
user = input("Enter choice (s/w/g): ").lower()
uchoice = dic[user]

print(f"\nYou chose: {rev_dic[uchoice]}")
print(f"Computer chose: {rev_dic[computer_val]}\n")

# Game logic
if uchoice == computer_val:
    print("It's a draw!")
elif (uchoice == 1 and computer_val == -1) or (uchoice == -1 and computer_val == 0) or (uchoice == 0 and computer_val == 1):
    print("You win!")
else:
    print("Computer wins!")
