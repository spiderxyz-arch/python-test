
# a=700
# b=900
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b) 

print("Welcome to the Secret Word Challenge 💖")

secret = "smile"
chances = 3

while chances > 0:
    guess = input("Guess my secret word: ").lower()

    if guess == secret:
        print("Wow! You guessed it! You are amazing 😊")
        break
    elif guess[0] == secret[0]:
        print("Close hint: it starts with S 😉")
    else:
        print("Not even close 😜")

    chances -= 1
    print(f"Chances left: {chances}")

if chances == 0:
    print("Game over! I will tell you the secret…")
    print(f"The secret word was: {secret}")

print("Thanks for playing with me 😄")

 
 