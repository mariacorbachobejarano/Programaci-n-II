##Dice simulator: Write a program that simulates the roll of two dice and calculates the sum of
##the values obtained.

import random

def roll_two_dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6) 
    return dice1, dice2

def main():
 
    die1, die2 = roll_two_dice()
    print(f"Sum total: ",die1+die2)
    
if __name__ == "__main__":
    main()