import random as r
import RPS_ART as RPS
import RPS_PLAYERS as PLAYERS
import time

def score_updt(player1,player2):
    x = player1.rps + player2.rps # POSSIBLE VALUES OF x: [RR, RP, RS, PR, PP, PS, PS, SR, SP, SS]

    if x in ['RS','PR','SP']:
        player1.score += 1
        return f'{player1.player_name} WIN!'
    
    elif x in ['RP','PS','SR']:
        player2.score += 1
        return f'{player2.player_name} WIN!'
    
    else:
        return 'TIE'

print(RPS.welcome)

game = {'R':RPS.rock, 'S':RPS.scissor, 'P':RPS.paper}
name_user = input("Enter your Name: ")
user = PLAYERS.Player(name_user)
computer = PLAYERS.Player('Computer')
players = [user, computer]

def game_rps():

    # taking choice from the user for their move
    user.player_choice()

    # handling error in case the user gives wrong input
    while user.rps[:] not in game:
        print('No such move exists!')
        user.player_choice()
    print(user.player_name)
    print(game[user.rps])

    # randomizing move for the computer
    move_list = [move for move in game]
    computer.rps = r.choice(move_list)
    print(computer.player_name)
    print(game[computer.rps])

    # evaluating who won the current game
    print(score_updt(user,computer))

while True:
    game_rps()
    choice = input('Enter Y to continue game or Exit to exit the game: ').upper()
    if choice != 'Y':
        print(f"""{user.player_score()}\n{computer.player_score()}""")
        print(RPS.game_over)
        time.sleep(5)
        break