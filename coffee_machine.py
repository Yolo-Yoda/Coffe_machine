# 1 week
"""print('Starting to make a coffee'
      '\nGrinding coffee beans'
      '\nBoiling water'
      '\nMixing boiled water with crushed coffee beans'
      '\nPouring coffee into the cup'
      '\nPouring some milk into the cup'
      '\nCoffee is ready!')"""
# 2 week
'''print('Write how many cups of coffee you will need:')
a = int(input())
print('For', a, 'cups of coffee you will need:')
print(a * 200, 'ml of water')
print(a * 50, 'ml of milk')
print(a * 15, 'g of coffee beans')'''
# 3 week
'''list_cups = list()
print('Write how many ml of water the coffee machine has:')
a_1 = int(input())
a_1 = a_1 // 200
list_cups.append(a_1)
print('Write how many ml of milk the coffee machine has:')
a_2 = int(input())
a_2 = a_2 // 50
list_cups.append(a_2)
print('Write how many grams of coffee beans the coffee machine has:')
a_3 = int(input())
a_3 = a_3 // 15
list_cups.append(a_3)
print('Write how many cups of coffee you will need:')
a_4 = int(input())
list_cups.sort()
if a_4 < list_cups[0]:
    print('Yes, I can make that amount of coffee (and even', list_cups[0] - a_4, 'more than that)')
elif a_4 == list_cups[0]:
    print('Yes, I can make that amount of coffee')
else:
    print('No, I can make only', list_cups[0], 'cups of coffee')'''
# 4 week
'''def ostatok_coffeemachine(water, milk, coffee_beans, free_cups, money):
    print('The coffee machine has:')
    print(water, 'of water')
    print(milk, 'of milk')
    print(coffee_beans, 'of coffee beans')
    print(free_cups, 'of disposable cups')
    print(money, 'of money')
def action():
    print('\nWrite action (buy, fill, take):')
    action = input()
    if action == 'buy':
        buy()
    elif action == 'fill':
        fill(water, milk, coffee_beans, free_cups, money)
    elif action == 'take':
        take(water, milk, coffee_beans, free_cups, money)
def buy():
    print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
    a = int(input())
    if a == 1:
        espresso(water, milk, coffee_beans, free_cups, money)
    elif a == 2:
        latte(water, milk, coffee_beans, free_cups, money)
    else:
        cappuccino(water, milk, coffee_beans, free_cups, money)
def espresso(water, milk, coffee_beans, free_cups, money):
    water = water - 250
    coffee_beans = coffee_beans - 16
    money = money + 4
    free_cups = free_cups - 1
    print('')
    return ostatok_coffeemachine(water, milk, coffee_beans, free_cups, money)
def latte(water, milk, coffee_beans, free_cups, money):
    water = water - 350
    milk = milk - 75
    coffee_beans = coffee_beans - 20
    money = money + 7
    free_cups = free_cups - 1
    print('')
    return ostatok_coffeemachine(water, milk, coffee_beans, free_cups, money)
def cappuccino(water, milk, coffee_beans, free_cups, money):
    water = water - 200
    milk = milk - 100
    coffee_beans = coffee_beans - 12
    money = money + 6
    free_cups = free_cups - 1
    print('')
    return ostatok_coffeemachine(water, milk, coffee_beans, free_cups, money)

def fill(water, milk, coffee_beans, free_cups, money):
    print('Write how many ml of water do you want to add:')
    water_add = int(input())
    water = water + water_add
    print('Write how many ml of milk do you want to add')
    milk_add = int(input())
    milk = milk + milk_add
    print('Write how many grams of coffee beans do you want to add:')
    coffee_beans_add = int(input())
    coffee_beans = coffee_beans + coffee_beans_add
    print('Write how many disposable cups of coffee do you want to add:')
    free_cups_add = int(input())
    free_cups = free_cups + free_cups_add
    print('')
    return ostatok_coffeemachine(water, milk, coffee_beans, free_cups, money)

def take(water, milk, coffee_beans, free_cups, money):
    print('I gave you $', money, sep='')
    money = 0
    print('')
    return ostatok_coffeemachine(water, milk, coffee_beans, free_cups, money)

water = 400
milk = 540
coffee_beans = 120
free_cups = 9
money = 550

ostatok_coffeemachine(water, milk, coffee_beans, free_cups, money)
action()'''
# 5 week
# water 0, milk 1, beans 2, cups 3, money 4
"""coffeemachine_list = [400, 540, 120, 9, 550]
def ostatok_coffeemachine(coffeemachine_list):
    print('The coffee machine has:')
    print(coffeemachine_list[0], 'of water')
    print(coffeemachine_list[1], 'of milk')
    print(coffeemachine_list[2], 'of coffee beans')
    print(coffeemachine_list[3], 'of disposable cups')
    print('$',coffeemachine_list[4], ' of money', sep='')
def action():
    print('\nWrite action (buy, fill, take, remaining, exit):')
    action = input()
    while action != 'exit':
        if action == 'buy':
            print('')
            buy()
            action = action_1()
        elif action == 'fill':
            print('')
            fill(coffeemachine_list)
            action = action_1()
        elif action == 'take':
            print('')
            take(coffeemachine_list)
            action = action_1()
        elif action == 'remaining':
            print('')
            ostatok_coffeemachine(coffeemachine_list)
            action = action_1()
        else:
            break
def action_1():
    print('\nWrite action (buy, fill, take, remaining, exit):')
    action = input()
    return action
def take(coffeemachine_list):
    print('I gave you $', coffeemachine_list[4], sep='')
    coffeemachine_list[4] = 0
    return coffeemachine_list
def fill(coffeemachine_list):
    print('Write how many ml of water do you want to add:')
    water_add = int(input())
    coffeemachine_list[0] = coffeemachine_list[0] + water_add
    print('Write how many ml of milk do you want to add:')
    milk_add = int(input())
    coffeemachine_list[1] = coffeemachine_list[1] + milk_add
    print('Write how many grams of coffee beans do you want to add:')
    coffee_beans_add = int(input())
    coffeemachine_list[2] = coffeemachine_list[2] + coffee_beans_add
    print('Write how many disposable cups of coffee do you want to add:')
    free_cups_add = int(input())
    coffeemachine_list[3] = coffeemachine_list[3] + free_cups_add
    return coffeemachine_list
def buy():
    print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
    a = input()
    if a == '1':
        espresso(coffeemachine_list)
    elif a == '2':
        latte(coffeemachine_list)
    elif a == '3':
        cappuccino(coffeemachine_list)
    else:
        return coffeemachine_list
def espresso(coffeemachine_list):
    if coffeemachine_list[0] < 250:
        print('Sorry, not enough water!')
        return coffeemachine_list
    elif coffeemachine_list[2] < 16:
        print('Sorry, not enough coffee beans!')
        return coffeemachine_list
    elif coffeemachine_list[3] < 1:
        print('Sorry, not enough disposable cups!')
        return coffeemachine_list
    else:
        print('I have enough resources, making you a coffee!')
        coffeemachine_list[0] = coffeemachine_list[0] - 250
        coffeemachine_list[2] = coffeemachine_list[2] - 16
        coffeemachine_list[4] = coffeemachine_list[4] + 4
        coffeemachine_list[3] = coffeemachine_list[3] - 1
        return coffeemachine_list
def latte(coffeemachine_list):
    if coffeemachine_list[0] < 350:
        print('Sorry, not enough water!')
        return coffeemachine_list
    elif coffeemachine_list[1] < 75:
        print('Sorry, not enough milk!')
        return coffeemachine_list
    elif coffeemachine_list[2] < 20:
        print('Sorry, not enough coffee beans!')
        return coffeemachine_list
    elif coffeemachine_list[3] < 1:
        print('Sorry, not enough disposable cups!')
        return coffeemachine_list
    else:
        print('I have enough resources, making you a coffee!')
        coffeemachine_list[0] = coffeemachine_list[0] - 350
        coffeemachine_list[1] = coffeemachine_list[1] - 75
        coffeemachine_list[2] = coffeemachine_list[2] - 20
        coffeemachine_list[4] = coffeemachine_list[4] + 7
        coffeemachine_list[3] = coffeemachine_list[3] - 1
        return coffeemachine_list
def cappuccino(coffeemachine_list):
    if coffeemachine_list[0] < 200:
        print('Sorry, not enough water!')
        return coffeemachine_list
    elif coffeemachine_list[1] < 100:
        print('Sorry, not enough milk!')
        return coffeemachine_list
    elif coffeemachine_list[2] < 12:
        print('Sorry, not enough coffee beans!')
        return coffeemachine_list
    elif coffeemachine_list[3] < 1:
        print('Sorry, not enough disposable cups!')
        return coffeemachine_list
    else:
        print('I have enough resources, making you a coffee!')
        coffeemachine_list[0] = coffeemachine_list[0] - 200
        coffeemachine_list[1] = coffeemachine_list[1] - 100
        coffeemachine_list[2] = coffeemachine_list[2] - 12
        coffeemachine_list[4] = coffeemachine_list[4] + 6
        coffeemachine_list[3] = coffeemachine_list[3] - 1
        return coffeemachine_list
action()
"""


# 6 week

class coffee_machine:
    water = 400
    milk = 540
    coffee_beans = 120
    disposable_cups = 9
    money = 550
    action = None

    def action_input(self):
        print('Write action (buy, fill, take, remaining, exit):')
        self.action = str(input())

    def remaining(self):
        print('The coffee machine has:')
        print(self.water, 'of water')
        print(self.milk, 'of milk')
        print(self.coffee_beans, 'of coffee beans')
        print(self.disposable_cups, 'of disposable cups')
        print('$', self.money, ' of money', sep='')
        return self.action

    def buy(self):
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        z_1 = input()
        if z_1 == '1':
            self.espresso()
        elif z_1 == '2':
            self.latte()
        elif z_1 == '3':
            self.cappuccino()
        else:
            print('')
            return self.action

    def espresso(self):
        if self.water < 250:
            print('Sorry, not enough water!')
            print('')
            return self.action
        elif self.coffee_beans < 16:
            print('Sorry, not enough coffee beans!')
            print('')
            return self.action
        elif self.disposable_cups < 1:
            print('Sorry, not enough disposable cups!')
            print('')
            return self.action
        else:
            print('I have enough resources, making you a coffee!')
            print('')
            self.water -= 250
            self.coffee_beans -= 16
            self.money += 4
            self.disposable_cups -= 1
            return self.action

    def latte(self):
        if self.water < 350:
            print('Sorry, not enough water!')
            print('')
            return self.action
        elif self.milk < 75:
            print('Sorry, not enough milk!')
            print('')
            return self.action
        elif self.coffee_beans < 20:
            print('Sorry, not enough coffee beans!')
            print('')
            return self.action
        elif self.disposable_cups < 1:
            print('Sorry, not enough disposable cups!')
            print('')
            return self.action
        else:
            print('I have enough resources, making you a coffee!')
            print('')
            self.water -= 350
            self.milk -= 75
            self.coffee_beans = self.coffee_beans - 20
            self.money += 7
            self.disposable_cups -= 1
            return self.action

    def cappuccino(self):
        if self.water < 200:
            print('Sorry, not enough water!')
            print('')
            return self.action
        elif self.milk < 100:
            print('Sorry, not enough milk!')
            print('')
            return self.action
        elif self.coffee_beans < 12:
            print('Sorry, not enough coffee beans!')
            print('')
            return self.action
        elif self.disposable_cups < 1:
            print('Sorry, not enough disposable cups!')
            print('')
            return self.action
        else:
            print('I have enough resources, making you a coffee!')
            print('')
            self.water -= 200
            self.milk -= 100
            self.coffee_beans -= 12
            self.money += 6
            self.disposable_cups -= 1
            return self.action

    def fill(self):
        print('Write how many ml of water do you want to add:')
        water_add = int(input())
        self.water += water_add
        print('Write how many ml of milk do you want to add:')
        milk_add = int(input())
        self.milk += milk_add
        print('Write how many grams of coffee beans do you want to add:')
        coffee_beans_add = int(input())
        self.coffee_beans += coffee_beans_add
        print('Write how many disposable cups of coffee do you want to add:')
        free_cups_add = int(input())
        self.disposable_cups += free_cups_add
        print('')
        return self.action

    def take(self):
        print('I gave you $', self.money, sep='')
        self.money = 0
        print('')
        return self.action

    def action(self):
        self.action_input()
        while self.action != 'exit':
            if self.action == 'buy':
                print('')
                self.buy()
                self.action_input()
            elif self.action == 'fill':
                print('')
                self.fill()
                self.action_input()
            elif self.action == 'take':
                print('')
                self.take()
                self.action_input()
            elif self.action == 'remaining':
                print('')
                self.remaining()
                print('')
                self.action_input()
            else:
                break


a = coffee_machine()
a.action()
