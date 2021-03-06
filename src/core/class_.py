import src.core.functions as f
from src.core.printing import table


#Start a round of drinks in menu
people = ["Harry", "Ron", "Hermoine"]
drinks = ["Coke", "Water", "Sprite"]
person= []
order = {}

class Round:
    def __init__(self, owner_name):
        self.owner = owner_name
        self.orders = {} #name:drink
    
    def add_order(self, name, drink):
        self.name = name
        self.drink = drink
        self.orders[name] = drink

    def print_order(self):
        items = []
        for name, drink in self.orders.items():
            items.append(f"{name}: {drink}")
        
        table(f"{self.owner}'s round",items)

class Csv():
    def __init__(self, filename):
        self.list = []
        self.file = filename

    def load(self):
        loaded_file = open(self.file,'r')
        for line in loaded_file:
            self.list.append(line.strip())

    def print(self):
        print("Hello World")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def legality(self):
        return self.age > 18

class Drink:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Test_person:
    def __init__(self, first_name, surname, age):
        self.firstname = first_name
        self.surname = surname
        self.age = age
    
    def legality(self):
        return self.age > 18

class Test_drink:
    def __init__(self, name, age):
        self.name = name
        self.age = age