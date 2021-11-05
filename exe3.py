import random

low_end = int(input("Pick a start point for guessing the number"))
high_end = int(input("Pick an end point for guessing the number"))
guess = 0
try_amount = 0
chosen = random.randint(low_end, high_end)
while guess != chosen:
    guess = int(input("Please guess the number:"))
    if guess > chosen:
        print("Too high!Try again!")
        try_amount = try_amount + 1
    elif guess < chosen:
        print("Too low!Try again!")
        try_amount = try_amount + 1
    else:
        print("You guessed it!")
        try_amount = try_amount + 1
        print("It took", try_amount, "attempts!")
