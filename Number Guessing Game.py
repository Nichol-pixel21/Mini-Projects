import random
lowest_num = 1
highest_num = 200

answer = random.randint(lowest_num, highest_num)
guesses = 0 
is_running = True


print("WELCOME DEAR USER, GUESS YOUR NUMBER SWEETIE!")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running :
    guess = input("Enter your guess pls.")

    if guess.isdigit(): 
        guess = int(guess)
        guesses += 1 

    if guess < lowest_num or guess > highest_num : 
        print("your dumb")

    elif guess < answer : 
        print("Too low")
    elif guess > answer :
        print("Too high")
    else : 
        print("Correct")
        
else :
        print("Bruh, don't you know the difference between a number and a string, you donkey !")