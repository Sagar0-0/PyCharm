import random


def generateRandom(start,end):
    return random.randint(start,end)


if __name__ == '__main__':
    player1name=input("Enter the name of Player 1: ")
    player2name=input("Enter the name of Player 2: ")
    ranje=[0,0]
    ranje[0]=int(input(f"Enter the starting range for your guessing game : "))
    ranje[1]=int(input(f"Enter the ending range for your guessing game : "))
    answer=generateRandom(ranje[0],ranje[1])
