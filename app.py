import random

game_options = {
    'rock': 'paper',
    'paper': 'scissors',
    'scissors': 'rock'
}

score = {
    'wins': 0,
    'rounds': 0,
    'losses': 0,
    'ties': 0
}

while True:
    print('rock, paper, or scissors?')
    user_input = input("Enter your choice: ")

    if user_input == "":
        print('Game over!')
        break

    if user_input not in game_options:
        print('Invalid option. Please choose rock, paper, or scissors.')
        continue

    print('You chose:', user_input)

    opponent_choice = random.choice(list(game_options.keys()))
    print('Opponent chose:', opponent_choice)

    if user_input == opponent_choice:
        print('It\'s a tie!')
        score['ties'] += 1
    elif game_options[user_input] == opponent_choice:
        score['wins'] += 1
        print('You won!')
    else:
        score['losses'] += 1
        print('You lost!')

print('Wins:', score['wins'])
print('Rounds:', score['rounds'])
print('Losses:', score['losses'])
print('Ties:', score['ties'])
