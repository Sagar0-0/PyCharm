import random

arr = ["Stone", "Paper", "Scissor"]

games = 10
wins = 0
loses = 0
ties = 0
while games > 0:
    myInput = int(input("Enter 1 for Stone\nEnter 2 for Paper\nEnter 3 for Scissor\n"))
    rand = random.choice(arr)
    if myInput == 1:
        if rand == "Paper":
            loses += 1
        elif rand == "Stone":
            ties += 1
        else:
            wins += 1
    elif myInput == 2:
        if rand == "Paper":
            ties += 1
        elif rand == "Stone":
            wins += 1
        else:
            loses += 1
    elif myInput == 3:
        if rand == "Paper":
            wins += 1
        elif rand == "Stone":
            loses += 1
        else:
            ties += 1
    else:
        print("Invalid input")
        continue
    print(f"Wins={wins}", f"Loses={loses}", f"Ties={ties}")
    games -= 1
print(f"Total matches Win={wins}\nTotal matches Lose={loses}\nTotal matches Tie={ties}")
