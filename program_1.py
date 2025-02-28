# Claire Francis, Feb 23, 2025, Week_6_program_1.py
# Program #1: Random Dice
# Write a "randDice" function (with no input) that randomly chooses two numbers between 1 and 6 (inclusive) and then adds them (this is to simulate the rolling of 2 dice).
# The dice sum will be the output of this function.
import random
sum = 0
def randDice():
    # Write your logic to generate 2 numbers between 1 and 6 here

    x = random.randint(1, 6)
    y = random.randint(1, 6)

    # Sum 2 numbers

    sum = x + y


    # return sum to calling function
    return sum

randDice()

#########
# Then write a mainline that calls the "randDice" function 100 times in a for loop.
# The mainline then prints the average of the 100 rolls, rounded to the nearest 0.01.
def main():
    total = 0

    for i in range(100):
        total += randDice()
    print("The average roll: ", round ( total / 100, 2))



if __name__ == '__main__':
    main()

