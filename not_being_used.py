
def load_people(PEOPLE_FILE_PATH):
    people = []
    for name, age in load_csv(PEOPLE_FILE_PATH).items(): 
            people.append(a.Person(name, age))
    return people

def load_drinks(DRINK_FILE_PATH):
    drink = []
    for drinks, age in load_csv(DRINK_FILE_PATH).items(): 
            drink.append(a.Drink(drinks, age))
    return drink


