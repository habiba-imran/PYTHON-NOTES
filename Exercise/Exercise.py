# Rock, Paper, Scissors
import random as r # 1 for draw, # 2 for comp, # 3 for user
options = [0, 1, 2]
compChoice = r.choice(options)
userChoice = int(input("Enter your choice, rock(0), paper(1), scissors(2): "))
#   R P S # USER 
# R 1 3 2
# P 2 1 3
# S 3 2 1
array = ['D', 'U', 'C'], ['C', 'D', 'U'], ['U', 'C', 'D']
result = array[compChoice][userChoice]
print("Your choice: ", userChoice)
print("Computer's choice", compChoice)
if(result == 'D'):
    print("DRAW")
elif(result == 'U'):
    print("YOU WIN")
elif(result == 'C'):
    print("OOPS, YOU LOST")


    
