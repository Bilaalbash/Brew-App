from src.core.class_ import Test_drink, Test_person
from src.core.functions import number_selection
from src.core.printing import table

def add_name(list_, object_list):
    firstname_input = input(f"First Name: ")
    surname_input = input(f"Surname: ")
    age_input = int(input(f"Age: "))

    if firstname_input == "" or surname_input == "" or age_input == "":
        print("\nERROR something is missing!")
        return

    if firstname_input not in list_:
        object_list.append(Test_person(firstname_input, surname_input, age_input))
    else:
        print("Name already exists! Please try another Name")
        
def add_drink(list_, object_list):
    alcohol_input = input(f"Is it an alcoholic or caffeinated drink (y/n): ")
    drink_input = input(f"Drink Name: ")
   
    if alcohol_input.lower() == 'y' or alcohol_input.lower() == 'yes':
        age = 18
    
    elif alcohol_input.lower() == 'n' or alcohol_input.lower() == 'no':
        age = 0
    else:
        print("\nInvalid Input")
        return

    if drink_input == "" or alcohol_input == "":
        print("\nERROR something is missing!")
        return

    if drink_input not in list_:
        object_list.append(Test_drink(drink_input, age))
    else:
        print("Name already exists! Please try another Name")

def assign_favourite(title, fav, data, data_2):
    temp = []
    temp_2 = []
    for index, item in enumerate(data, start=1):
        temp.append(f"[{index}] {item}")
    table("people", temp) 
    name = number_selection("\nSelect number next to your name: ")
    print(name)

    for index, value in enumerate(data_2, start = 1):
        temp_2.append(f"[{index}] {value}")
    table("drinks", temp_2)
    drink = number_selection("\n Select the number next to your preference: ")
    
    fav[data[name-1]] = data_2[drink-1]
    print("\nPreference Stored")
    
    return fav