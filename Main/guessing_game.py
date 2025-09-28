import random


highest_num = 100
lowest_num = 1

while True:
    guesses = 0
    start = input("Welcome to the guessing game! Press s to start: ")

    if start != "s":
        start = input("Invalid input! Try again: ")

    answer = random.randint(lowest_num, highest_num)

    guess = int(input(f"Try to guess the generated number from {lowest_num} -- {highest_num}: "))
    while True:
        if guess > highest_num or guess < lowest_num:
             guess = int(input(f"Number out of range! Please select a number between {lowest_num} and {highest_num}: "))

        elif guess > answer:
            guess = int(input("Too high! Try again: "))
            guesses+=1
        elif guess < answer:
            guess = int(input("Too low: Try again: "))
            guesses += 1
        else:
            print("-----------------------------------")
            print(f"CORRECT! The answer was {answer}")
            print(f"Number of guesses: {guesses}")
            break
    start = input("Do you want to play again?(Y/N): ")
    if start.upper() != "Y":
        print("Thanks for playing!")
        break





