# game.py
# Ian Oberbillig
# 10/17/24

import gamefunctions

playerName = input('What is your name: ')

gamefunctions.print_welcome(playerName)


randomEncounter = gamefunctions.new_random_monster()

input((f'As you walk along the path you encounter a {randomEncounter['name']}'))
input(randomEncounter['description'])
input('You manage to escape and come across a small roadside shop.')
print('The shop\'s menu is as follows:')
gamefunctions.print_shop_menu('Egg',2.2,'Milk',18)
input('Pulling out your wallet you see you see that you have 20 dollars.')

playerWealth = 20

input('The shopkeeper gives you a scowl and barks "what do you want?"')

playersPurchase = input('(Type what you want to purchase, "Egg", "Milk", or "Nothing"): ')

purchaseAmount = 0
price = 0

if playersPurchase == 'Egg':
    purchaseAmount = int(input('How many do you want?: '))
    price = 2.2
    playerWealth = gamefunctions.purchase_item(price, playerWealth, purchaseAmount)
elif playersPurchase == 'Milk':
    purchaseAmount = int(input('How many do you want?: '))
    price = 18
    playerWealth = gamefunctions.purchase_item(price, playerWealth, purchaseAmount)
elif playersPurchase == 'Nothing':
    print('"Then get out of my shop", snarls the shopkeeper!')
else:
    print('Invalid input.')
    




