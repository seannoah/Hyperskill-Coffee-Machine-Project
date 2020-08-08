class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.cb = 120
        self.cups = 9
        self.money = 550
        self.active = True
        self.take_action()
    def assess_supplies(self, drink_choice):
        can_do = False
        water = self.water
        milk = self.milk
        cb = self.cb
        cups = self.cups
        missing_ingredient = []
        if drink_choice == 1:
            if (water >= 250) and (cb >= 16) and (cups >= 1):
                can_do = True
            else:
                if water < 250:
                    missing_ingredient = 'water'
                elif cb < 16:
                    missing_ingredient = 'coffee beans'
                elif cups < 1:
                    missing_ingredient = 'cups'
        elif drink_choice == 2:
            if (water >= 350) and (milk >= 75) and (cb >= 20) and (cups >= 1):
                can_do = True
            else:
                if water < 350:
                    missing_ingredient = 'water'
                elif milk < 75:
                    missing_ingredient = 'milk'
                elif cb < 20:
                    missing_ingredient = 'coffee beans'
                elif cups < 1:
                    missing_ingredient = 'cups'
        elif drink_choice == 3:
            if (water >= 200) and (milk >= 100) and (cb >= 12) and (cups >= 1):
                can_do = True
            else:
                if water < 200:
                    missing_ingredient = 'water'
                elif milk < 100:
                    missing_ingredient = 'milk'
                elif cb < 12:
                    missing_ingredient = 'coffee beans'
                elif cups < 1:
                    missing_ingredient = 'cups'
        return can_do, missing_ingredient
    def take_action(self):
        while self.active:
            took = input('Write action (buy, fill, take, remaining, exit): ')
            if took == 'buy':
                self.buy()
            elif took == 'fill':
                self.fill()
            elif took == 'take':
                self.take()
            elif took == 'remaining':
                self.remaining()
            elif took == 'exit':
                self.active = False
    def buy(self):
        drink_choice = input('What do you want to buy? 1 – espresso, 2 – latte, 3 – cappuccino, back')
        if drink_choice == 'back':
            return None
        else:
            drink_choice = int(drink_choice)
            can_do, missing_ingredient = self.assess_supplies(drink_choice)
            if can_do:
                print('I have enough resources, making you a coffee!')
                if drink_choice == 1:
                    self.water -= 250
                    self.cb -= 16
                    self.cups -= 1
                    self.money += 4
                elif drink_choice == 2:
                    self.water -= 350
                    self.milk -= 75
                    self.cb -= 20
                    self.cups -= 1
                    self.money += 7
                elif drink_choice == 3:
                    self.water -= 200
                    self.milk -= 100
                    self.cb -= 12
                    self.cups -= 1
                    self.money += 6
            else:
                print('Sorry, not enough ' + missing_ingredient)
    def fill(self):
        self.water += int(input('Write how many ml of water do you want to add: '))
        self.milk += int(input('Write how many ml of milk do you want to add: '))
        self.cb += int(input('Write how many grams of coffee beans do you want to add: '))
        self.cups += int(input('Write how many disposable cups of coffee do you want to add: '))
    def take(self):
        print('I gave you ' + str(self.money))
        self.money = 0
    def remaining(self):
        print('The coffee machine has:')
        print(str(self.water) + ' of water')
        print(str(self.milk) + ' of milk')
        print(str(self.cb) + ' of coffee beans')
        print(str(self.cups) + ' of disposable cups')
        print(str(self.money) + ' of money')

a_coffee_machine = CoffeeMachine()
