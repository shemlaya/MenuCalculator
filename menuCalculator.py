import csv
import time


class Menu:
    def __init__(self) -> object:
        self.items = {}
        with open('menu.csv') as menu:
            csv_reader = csv.reader(menu, delimiter=',')
            for row in csv_reader:
                self.items[row[0]] = row[1]

    def printMenu(self):
        index = 1
        for item in self.items.keys():
            print(str(index) + '. ' + item + ': $' + str(self.items[item]))
            index += 1

    def exists(self, name):
        if name in self.items.keys():
            return True
        else:
            return False

    def getPrice(self, name):
        return self.items[name]


class Order:

    def __init__(self):
        self.itemsList = {}
        self.menu = Menu()
        self.menu.printMenu()

    def add(self, name):
        if not self.menu.exists(name):
            print('We don\'t have that in our menu, try another item')
        else:
            if name in self.itemsList.keys():
                self.itemsList[name][1] += 1
            else:
                price = float(self.menu.getPrice(name))
                self.itemsList[name] = [price, 1]
            print(name + ' It is. Anything else? (or type "Bill")')

    def bill(self):
        total = 0
        index = 1
        print('\n*** Your bill ***\n')
        for item in self.itemsList.items():
            subSum = item[1][0] * item[1][1]
            total += subSum
            print(str(index) + '. ' + str(item[1][1]) + ' X ' + item[0] + ' = ' + str(subSum))
            index += 1
        print('\nTotal = ' + str(total))


if __name__ == '__main__':
    print('Welcome to our restaurant! This is our menu:')
    order = Order()
    time.sleep(0.5)
    print('\nWhat would you like to order?')

    while True:
        name = input()
        if name.lower() != "bill":
            order.add(name)
        else:
            order.bill()
            break