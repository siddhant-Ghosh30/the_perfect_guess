import random
n = random.randint(1, 100)
a = -1 # we're taking -1 so that the loop always runs by default
guesses = 0 # intializing No. of guesses the player took
while (a != n):
    guesses = guesses + 1
    a = int(input(" Guess the number:"))

    if(a>n):
        print("Lower number please")
    elif(a<n):
        print("Higher number please")

    elif(a==n):
        print(f"Lessgoo {a} is the right number")
        break

print(f"you took {guesses} guesses")


