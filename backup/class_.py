import functions_definitions as f
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
        
        f.table(f"{self.owner}'s round",items)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def legality(self):
        return self.age > 18

person = Person("Bilaal", 22)
print(person.name)

l = [person.name for i in people]

#print(l)

#12.47
