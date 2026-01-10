
"""Adventure Game
In this adventure game, the player takes on the role of an explorer searching for a legendary
treasure hidden in an ancient land. The player must navigate through various challenges,
make strategic decisions, and overcome obstacles to complete their quest successfully. Thegame consists of multiple decision-based scenarios where each choice leads to a different
outcome. Some choices will move the player closer to the treasure, while others might result
in failure or setbacks. The player will navigate different locations—such as a dense forest and
a mysterious cave—while making strategic choices that determine their success.
1. The game starts by introducing the player's quest and asking for their name.
2. The player is given an initial choice of exploring different paths (a dark forest or a
mysterious cave).
3. Each choice will trigger a new event, leading to more decisions.
4. The player must think critically and choose wisely to advance toward the treasure.
5. The game ends in one of the following three ways:
o Winning: Finding the treasure
o Losing: Making a poor decision that ends the adventure
o Restarting: Choosing to replay the game after an unsuccessful attempt
The objective is to find the treasure by making the right choices and overcoming obstacles,
successfully navigating the adventure. If the player makes poor decisions, they may lose
their way or fail the quest.
"""

# Task 1: Set up the project
print("Welcome to the Adventure Game!. Setup done successfully.")

# Task 2: Create a function to start the game
# Define the function start_game() to display the game introduction
# Ask the player for their name and store it in a variable
# Provide the player with an initial choice (explore a forest or enter a cave)
# restrict the name to be valid (non-empty) and just alpha. if invalid ask again.
def start_game():
    print("\n\nYou are an explorer on a quest to find a legendary treasure hidden in an ancient land.")
    while True:
        player_name = input("\n\nWhat is your name, adventurer? ")
        if player_name and player_name.isalpha():
            break
        print("Invalid name. Please enter a valid name (letters only).")
    print(f"\n\nWelcome, {player_name}! Your journey begins now.")
    print("\n\nYou have two paths ahead of you:")
    print("\n1. Explore the Dark Forest")
    print("\n2. Enter the Mysterious Cave")
    choice = input("\nWhich path will you choose? (Enter 1 or 2): ")
    return choice

# Task 3: Create the forest path
# Define the function forest_path() that describes the forest scenario
# Provide the player with choices (follow a river or climb a tree)
# Use an if-else structure to handle player choices
# limit the user input to 1 or 2 just. in case of invalid input the player should retry to input again.
# add more paths to make the game more interesting.

def forest_path():
    print("\nYou enter the dark forest. The trees are tall and the path ahead is unclear.")
    print("You see a river nearby and a tall tree with a strange marking.")
    while True:
        choice = input("\nDo you follow the river (1) or climb the tree (2)? ")
        if choice == "1":
            print("\nYou follow the river and find a hidden bridge.")
            return "bridge"
        elif choice == "2":
            print("\nYou climb the tree and discover a secret passage.")
            return "passage"
    
# Task 4: Create the cave path
# Define the function cave_path() that describes the cave scenario
# Provide the player with choices (light a torch or proceed in the dark)
# Use conditionals to determine the outcome
# limit the user input to 1 or 2 just. in case of invalid input the player should retry to input again.

def cave_path():
    print("\nYou enter the mysterious cave. It's dark and eerie.")
    print("\nYou can either light a torch or proceed in the dark.")
    while True:
        choice = input("\nDo you light a torch (1) or proceed in the dark (2)? ")
        if choice == "1":
            print("\nWith the torch lit, you see a treasure chest ahead!")
            return "treasure"
        elif choice == "2":
            print("\nYou stumble in the dark and fall into a pit.")
            return "pit"
    
    
# Task 5: Run the adventure game
# Call start_game() to begin the adventure
# Ensure the program runs in a loop until the player completes their journey
# Provide an option to restart the game after completion
while True:
    player_choice = start_game()
    if player_choice == "1":
        outcome = forest_path()
        if outcome == "bridge":
            # make this choice as a lose also
            # print a lose message            
            print("\nYou cross the bridge and fall into a pit. You lose!")
        elif outcome == "passage":
            print("\nThe secret passage leads you to a dead end. You lose!")
        else:
            print("You are lost in the forest. Game over!")
    elif player_choice == "2":
        outcome = cave_path()
        if outcome == "treasure":
            print("You found the treasure chest! You win!")
            break
        elif outcome == "pit":
            print("You fell into a pit. You lose!")
        else:
            print("You are lost in the cave. Game over!")
    else:
        print("Invalid choice. Please choose a valid path.")
    
    restart = input("Do you want to play again? (y/n): ")
    if restart.lower() != "y":
        print("Thank you for playing the Adventure Game! Goodbye!")
        break
