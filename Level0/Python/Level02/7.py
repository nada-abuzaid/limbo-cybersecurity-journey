# Create a number guessing game.
secret_num = 42
while True:
    guess = int(input("Guess the number (between 1 and 100): "))
    if guess == secret_num:
        print("Congratulations! You guessed the number.")
        break
    elif guess < secret_num:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")