import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

# Prompt for the number of players
while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2-4 players.")
    else:
        print("Invalid input, try again.")

# Initialize the maximum score and player scores
max_score = 50
player_scores = [0 for _ in range(players)]

# Game loop
while max(player_scores) < max_score:
    for player_idx in range(players):
        print("\nPlayer number", player_idx + 1, "'s turn has started!")
        print("Your total score is", player_scores[player_idx], "\n")
        
        current_score = 0
        
        # Player's turn loop
        while True:
            should_roll = input("Would you like to roll? (y to roll, any other key to hold): ")
            if should_roll.lower() != "y":
                break

            value = roll()
            print("You rolled a:", value)

            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("Your current score for this turn is:", current_score)

        player_scores[player_idx] += current_score
        print("Your total score is", player_scores[player_idx])
        
        # Check if the player has won
        if player_scores[player_idx] >= max_score:
            break

# Determine the winner
max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("\nPlayer number", winning_idx + 1, "is the winner with a score of:", max_score)
