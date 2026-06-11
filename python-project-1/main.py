import random

'''
1 = snake
-1 = water
0 = gun
'''

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice (s/w/g): ")
youDict = { "s": 1, "w": -1, "g": 0}

you = youDict[youstr]

#by now we have 2 number(variables), which is you and computer

reverseDict = {1: "snake",-1: "water",0: "gun"}

if you not in reverseDict:
    print("Invalid input")

else:
    print(f"You chose {reverseDict[you]}")
    print(f"Computer chose {reverseDict[computer]}")

    if(computer == you):
        print("Its a draw")

    else:
        if(computer == -1 and you == 1):  
            print("You Win!")

        elif(computer == -1 and you == 0):  
            print("You Lose!")

        elif(computer == 1 and you == -1):  
            print("You Lose!")

        elif(computer == 1 and you == 0):  
            print("You Win!")

        elif(computer == 0 and you == -1):   
            print("You Win!")

        elif(computer == 0 and you == 1):  
            print("You Lose!")

        else:
            print("Something went wrong")