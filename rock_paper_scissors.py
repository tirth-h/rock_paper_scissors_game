import random

def get_choices():
    player_choice = input('enter a choice (pock,paper,scissors) : ')
    options = ['paper','rock','scissors']
    computer_choice = random.choice(options)
    choices = { "player" : player_choice, "computer" : computer_choice}
    return choices

def check_win(player,computer):
    print(f"you chose {player} and the computer chose {computer}") ### fstring
    if player == computer:
        return 'it\'s a tie'
    elif player == 'paper':
        if computer == 'scissors':
            return "player loses"
        else:
            return "player wins"
    elif player == 'rock':
        if computer == 'paper':
            return "player loses"
        else:
            return "player wins"
    elif player == 'scissors':
        if computer == 'rock':
            return "player loses"
        else:
            return "player wins"
        

choices = get_choices()
result = check_win(choices["player"], choices["computer"])

print(result)