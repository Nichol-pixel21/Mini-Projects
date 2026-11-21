import random 

options = ("rock","paper", "scissors")
player = None
computer = random.choice(options)
running =  True 

while running:

        player = None
        computer = random.choice(options)

        while player not in options : 
            player = input("Enter a choice : rock, paper, scissors ")

        print(f"Player: {player} and computer = {computer}")

        if player == computer : 
            print("It's a tie")

        elif player == "rock" and computer == "scissors" :
            print("Player wins!")

        elif player == "paper" and computer == "rock" :
            print("Player wins!")

        elif player == "scissors" and computer == "paper" :
            print("Player wins")

        else : 
            print("You lose")
        
        play_again = input("Would you like to play again ? (For yes : Y and for No : N ) :") 
        if not play_again == "Y" :
              running = False

print("Thanks for playing!")