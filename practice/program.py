secret = "ahmed"
attempts = 0

while attempts < 3:
    guess = input("Enter your secret: ")
    attempts += 1

    if guess == secret and attempts <= 3:
        print("You won!")
        break
    elif guess != secret and attempts < 3:
        print("Try again")
    elif guess != secret or attempts == 3:
        print("You failed!")
