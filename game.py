# game.py
# Ian Oberbillig
# 12/07/24

import gamefunctions


#Main game loop

quit_status = False

while not quit_status:

    #Initialize player stats

    player = {
        'name':'',
        'power':25,
        'max_hp':100,
        'current_hp':5,
        'gold':20
        }

    input('Welcome to a text based adventure (hit enter to continue)')

    player['name'] = input('What is your name: ')
    print('')
    gamefunctions.print_welcome(player['name'])
    input()

    #Adventure loop
    
    adventure_status = True
    
    while adventure_status:

        #Game over
        if player['current_hp'] <= 0:
            answer = gamefunctions.game_over()
            quit_status = answer[0]
            adventure_status = answer[1]

        else:
        
            input(f'Current HP: {player["current_hp"]}, Current Gold: {player["gold"]}')
            print(
                'What would you like to do? \n'
                '1) Fight Monster \n'
                '2) Sleep (Restore HP for 5 Gold) \n'
                '3) Quit \n'
            )
            user_input = input('Select an option: ')

            if not user_input in ['1', '2', '3']:
                input('Invalid input')
                
            elif user_input == '1':
                monster = gamefunctions.new_random_monster()
                input(f'You go searching until you find a {monster["name"]}')
                input(monster['description'])
                gamefunctions.fight_monster(player, monster)
                
            elif user_input == '2':
                input('You buy a room at an Inn for 5 gold')
                player['gold'] -= 5
                player['current_hp'] = player['max_hp']
                input('You feel refreshed')
            elif user_input == '3':
                adventure_status = False
                quit_status = True


        
    

        
    


    




