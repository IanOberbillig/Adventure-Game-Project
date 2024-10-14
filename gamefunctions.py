#Adventure functions
#Ian Oberbillig
#09/29/24
import random

def purchase_item(itemPrice, startingMoney, quantity = 1):
    ''' Returns the number of items purchased and the quantity of money remaining '''
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
    '''Generates a random monster'''
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
        monster['description'] = 'He\'s coming at you fast'
        monster['health'] = random.randint(7,10)
        monster['power'] = random.randint(17, 23)
        monster['money'] = random.randint(0, 5)
    if monster['name'] == 'Simp':
        monster['description'] = 'He\'s crouched in the corner'
        monster['health'] = random.randint(0,3)
        monster['power'] = random.randint(0, 3)
        monster['money'] = random.randint(100, 1000)
    if monster['name'] == 'Blimp':
        monster['description'] = 'He\'s just floating around'
        monster['health'] = random.randint(150, 200)
        monster['power'] = random.randint(90, 100)
        monster['money'] = random.randint(1000, 20000)
        
    return monster

def print_welcome(name, width=20):
    '''Prints a welcome to "name", centered around a whitespace of length "width"'''
    #Creates the greeting for the given name
    new_string = f'Greetings {name}'
    print(f'{new_string:^{width}}')

def print_shop_menu(item1Name, item1Price, item2Name, item2Price):
    '''Prints a shop menu'''
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

#Function Calls to demonstrate code functionality:
#Note for Ian: use 'command 3' to comment out hilighted code blocks
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

print("print_shop_menu('Egg',2,'Milk',32)")
print_shop_menu('Egg',2,'Milk',32)
print('')
print("print_shop_menu('Cursed Object',6.66, 'Pie',3.141592)")
print_shop_menu('Cursed Object',6.66, 'Pie',3.141592)
print('')
print("print_shop_menu('Newt', 8.5, 'Mace of Extordinary Might', 100000000000)")
print_shop_menu('Newt', 8.5, 'Mace of Extordinary Might', 100000000000)







