
"""Contains useful functions for a text based adventure game.

Leave one blank line.  The rest of this docstring should contain an
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.

This module contains fuctions: purchase_item, new_random_monster,
print_welcome, and print_shop_menu. Consult individual functions docstrings
for more information."""


#Adventure functions
#Ian Oberbillig
#09/29/24
import random

def purchase_item(itemPrice, startingMoney, quantity = 1):
    '''
    Returns the number of items purchased and the quantity of money remaining.

    Parameters:
        itemPrice(float): The price of the item.
        startingMoney(float): The amount of money owned by the player.
        quantity(int): The number of items the player wants to buy.

    Returns:
        (quantity_purchased, remainingMoney): A tuple whose contents are as follows:
            quantity_purchased(int): Number of items purchased.
            remainingMoney(float): The players remaining money.
    Example:
        >>> x = purchase_item(3, 22, 4)
        >>> print(x)
        (3, 10)
    '''
    totalPrice = quantity * itemPrice
    # Calculates how many items the player can afford
    canAfford = startingMoney // itemPrice
    # If the player can afford the quantity they want they purchase that quantity
    if canAfford >= quantity:
        quantity_purchased = quantity
        remainingMoney = startingMoney - itemPrice * quantity
    # If they can't afford what they want they purchase as much as they can
    else:
        quantity_purchased = canAfford
        remainingMoney = startingMoney - itemPrice * canAfford

    return (quantity_purchased, remainingMoney)

def new_random_monster():
    '''
    Generates a random monster.

    Paramters:
        None

    Returns:
        monster(dict): A dictionary with the following keys:
            name(str): the monster's name.
            description(str): A description of the monster.
            health(int): The monster's health.
            power(int): The monster's power.
            money(int): The monster's money.

    Example:
        >>> randomEncounter = new_random_monster()
        >>> print(randomEncounter['name']
        Blimp
        >>> print(randomEncounter['money']
        1223
    '''
    monster = {
        'name': '',
        'description' : '',
        'health' : '',
        'power' : '',
        'money' : ''
        }
    monsterLibrary = (
        'Chimp',
        'Simp',
        'Blimp'
        )
    #Assigns a name
    monster['name'] = monsterLibrary[random.randint(0,len(monsterLibrary) - 1)]
    #Assigns other stats based on name
    if monster['name'] == 'Chimp':
        monster['description'] = 'He\'s coming at you fast.'
        monster['health'] = random.randint(7,10)
        monster['power'] = random.randint(17, 23)
        monster['money'] = random.randint(0, 5)
    if monster['name'] == 'Simp':
        monster['description'] = 'He\'s crouched in the corner.'
        monster['health'] = random.randint(1,3)
        monster['power'] = random.randint(0, 3)
        monster['money'] = random.randint(100, 1000)
    if monster['name'] == 'Blimp':
        monster['description'] = 'He\'s just floating around.'
        monster['health'] = random.randint(150, 200)
        monster['power'] = random.randint(5, 8)
        monster['money'] = random.randint(1000, 20000)
        
    return monster

def print_welcome(name, width=20):
    '''
    Prints a welcome to "name", centered inside a whitespace of length "width".

    Paramaters:
        name(str): The players name.
        width(int): The desired amount of whitespace, default value of 20.

    Returns:
        None

    Example:
        >>> print_welcome('John', 22)
            Greetings John    
    '''
    #Creates the greeting for the given name
    new_string = f'Greetings {name}'
    print(f'{new_string:^{width}}')

def print_shop_menu(item1Name, item1Price, item2Name, item2Price):
    '''
    Prints a shop menu with two items.

    Paramaters:
        item1Name(str): The name of the first item.
        item1Price(float): The price of the first item.
        item2Name(str): The name of the second item.
        item2Price(float): The price of the second item.

    Returns:
        None

    Example:
        >>> print_shop_menu('Egg', 2.2, 'Milk', 32)
       /----------------------\\
       | Egg            $2.20 |
       | Milk          $32.00 |
       \\----------------------/ 
    '''
    #Shortens item names if they're too long
    if len(item1Name) > 12:
        item1Name = f'{item1Name[0:9]}...'
        
    if len(item2Name) > 12:
        item2Name = f'{item2Name[0:9]}...'
    #Lowers item price to 9999 if greater than 9999
    if item1Price > 9999:
        item1Price = 9999
    if item2Price > 9999:
        item2Price = 9999
    
    #puts a dollar sign on the prices and rounds to 2 decimal places
    item1Price = f'${item1Price:.2f}'
    item2Price = f'${item2Price:.2f}'

    #opening border
    print('/', end='')
    print('-' * 22, end='')
    print('\\')
    
    #body
    
    print('|', end = ' ')
    print(f'{item1Name:12}{item1Price:>8}', end = ' ')
    print('|')
    print('|', end = ' ')
    print(f'{item2Name:12}{item2Price:>8}', end = ' ')
    
    #closing border
    print('|')
    print('\\', end='')
    print('-' * 22, end='')
    print('/')
    

def game_over():
    '''
    Handles the death of a player.

    Paramaters:
        None

    Returns:
        (Bool, Bool): A tuple of booleans, which track whether the
            player wants to try again or quit the game entirely.
    '''

    user_input = ''
    input('You died \n')
    while not user_input in ['1', '2']:
        print(
             'What would you like to do? \n'
             '1) Play again \n'
             '2) Quit'
              )
        user_input = input('Select an option: ')
        if not user_input in ['1', '2']:
            input('Invalid input')
        elif user_input == '1':
            return (False, False)
        elif user_input == '2':
            return(True, False)
            

def fight_monster(player, monster):
    '''
    Initiates a fight between a player and a monster.

    Paramaters:
        player(dict): Player information
        monster(dict): Monster information
        

    Returns:
        None
    '''
    #Initializes an input
    user_input = ''
    leave = False
    #Main fight loop
    while user_input != '2' and not leave:
        input(f'You\'re in combat with a {monster["name"]}\n')
        input(
              f'Your hp: {player["current_hp"]}\n'
              f'Monster hp: {monster["health"]}\n'
              )
        
        print(
              'What do you want to do?\n\n'
              '\t 1) Attack\n'
              '\t 2) Run\n'
              )
        user_input = input('Choose 1 or 2: ')
        if not user_input in ['1', '2']:
            input('Invalid input')
            
        # Attack sequence
        elif user_input == '1':
            monster['health'] = monster['health'] - player['power']
            player['current_hp'] = player['current_hp'] - monster['power']
            
            #Checks if player died
            if player['current_hp'] <= 0:
                leave = True
            
            #Checks if monster died
            elif monster['health'] <= 0:
                print('You are victorious')
                player['gold'] += monster['money']
                user_input = '2'
        elif user_input == '2':
            print('Got away safely')


    
    
#Function Calls to demonstrate code functionality:
#Note for Ian: use 'control 3' to comment out highlighted code blocks


def test_functions():
    print('Sample run of each function 3 times, to demonstrate functionality:')
    print('')
        
    print('purchase_item(300, 4000)')
    print(purchase_item(300, 4000))
    print('')
    print('purchase_item(2000, 31)')
    print(purchase_item(2000, 31))
    print('')
    print('purchase_item(11, 422, 13)')
    print(purchase_item(11, 422, 13))

    print('')
    print('')


    print('new_random_monster()')
    print(new_random_monster())
    print('')
    print('new_random_monster()')
    print(new_random_monster())
    print('')
    print('new_random_monster()')
    print(new_random_monster())

    print('')
    print('')


    print('print_welcome("Felicity")')
    print_welcome('Felicity')
    print('')
    print('print_welcome("Ian", 30)')
    print_welcome('Ian', 30)
    print('')
    print('print_welcome("Alex", 100)')
    print_welcome('Alex', 100)

    print('')
    print('')

    print("print_shop_menu('Egg',2.2,'Milk',32)")
    print_shop_menu('Egg',2.2,'Milk',32)
    print('')
    print("print_shop_menu('Cursed Object',6.66, 'Pie',3.141592)")
    print_shop_menu('Cursed Object',6.66, 'Pie',3.141592)
    print('')
    print("print_shop_menu('Newt', 8.5, 'Mace of Extordinary Might', 100000000000)")
    print_shop_menu('Newt', 8.5, 'Mace of Extordinary Might', 100000000000)

    print('')
    print('')

    print("game_over()")
    
    game_over()

    print('')
    print('')


    player = {
    'name':'',
    'power':25,
    'max_hp':100,
    'current_hp':100,
    'gold':20
    }
    print("fight_monster(player, new_random_monster())")
    fight_monster(player, new_random_monster())

if __name__ == '__main__':
    test_functions()
    




