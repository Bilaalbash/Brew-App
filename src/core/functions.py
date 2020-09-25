import core.class_ as a
import csv
import os

def clear():
    os.system("clear")

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

def load_csv(filepath):
    try:
        with open(filepath, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            dict_ = {}
            for line in csv_reader:
                dict_[line[0]] = line[1]
    except FileNotFoundError as fnfe:
        print('Unable to open file: ' + str(fnfe))
        return
    except Exception as e:
        print('An error occurred: ' + str(e))
        return   
    finally:
        pass#csv_file.close()
    return dict_

def load_txt(filepath):
    temp_list = []
    try:
        txt_file = open(filepath,'r')
        for line in txt_file:
            temp_list.append(line.strip())

    except FileNotFoundError as fnfe:
        print('Unable to open file: ' + str(fnfe))
        return []
    except Exception as e:
        print('An error occurred: ' + str(e))
        return []    
    finally:
        txt_file.close()
    return temp_list

def save_items(filepath, items, name):
    try:
        items_file = open(filepath,'w')
        for item in items:
            items_file.write(item + '\n')
    except:
        print(f"Unable to open {filepath} for writing")
    finally:
        items_file.close()
        print(f"Saving...")

def wait():
    input("\nPress Enter to return to Menu\n")

def table(title, data): #Prints out table of data
    width = get_width(title, data)
    banner = (f"+{'=' * width}+")
    print(f"{banner}\n|{title.upper()}{' ' * (width - len(title))}|\n{banner}")

    for item in data:
        print(f"|{item}{' ' * (width - len(item))}|"  )
    print(f"{banner}\n")

def long_table(title, data):
    
    width = get_width(title, data)
    banner = (f"+{'=' * width}+")
    print(f"{banner}\n|{title.upper()}{' ' * (width - len(title))}|\n{banner}")

    for key, value in data.items():
        print(f"|{key}: {value}{' ' * (width - len(value) - len(key)-2)}|")
    print(f"{banner}\n")

def get_width(title, data):
    longest = len(title)

    for item in data:
        if len(item) > longest:
            longest = len(item)
    return longest + 1

def enumerate_data(list_1, list_2):
    for index, item in enumerate(list_1, start=1):
            list_2.append(f"[{index}] {item}")
    return list_2

def order_round(drink, people, people_class, drink_class):
    temp_drink = []
    temp_name = []
    drink_active = True
    global orders
    orders = []

    if drink_active == True:
        enumerate_data(people, temp_name)
        table("Whos Round is it?", temp_name)
        owner = input("Whos Round is it: ")
        round = a.Round(owner)
        
        enumerate_data(drink, temp_drink)
        table("   Menu", temp_drink)
        print("Enter number that is next to the drink you want\n")

        for index, name in enumerate(people):
            select = number_selection(f"{name}'s Order: ")
            bev = drink[select-1]
            if people_class[index].age < drink_class[select-1].age:
                print(f'{people_class[index].name} is too young to buy a {drink_class[select-1].name}\n')
            else:
                round.add_order(name, bev)
                orders.append(f"{round.name}, {round.drink}")
                save_csv('round.csv', round.owner, orders)
            
        round.print_order()
    else:
        print("Sorry we're not taking orders right now")

def save_csv(file_path, owner, data):

    with open(file_path, 'w') as csvfile:
        round_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL) # Writer
        round_writer.writerow([f"{owner}'s Round\n"])
        for names in data:
            round_writer.writerow([f"{names}"])

def print_menu(APP_NAME):
    print(f'''
Welcome to {APP_NAME}!

Please select an option by entering a number

\t[1] View People List
\t[2] View Drinks List
\t[3] View Favourite List
\t[4] Add People
\t[5] Add Drink
\t[6] Set a Favourite Drink
\t[7] Create Round
\t[8] Close Program
''')

def add_name(list_, data, object_list, Class):
    input_ = input(f"What is the name of the {data}?\n")
    age = int(input(f"How old are you: "))
    if input_ == "":
        print("\nERROR something is missing!")
        return

    if input_ not in list_:
        list_.append(input_)
        object_list.append(Class(input_, age))
        save_items("drink.txt", list_, "Drinks")
        print("Thank you! The information has been stored.")
    else:
        print("Name already exists! Please try another Name")
    
def add_drink(list_, data, object_list, Class):
    input_ = input(f"What is the name of the {data}?\n")
    if input_ == "":
        print("\nERROR something is missing!")
        return

    if input_ not in list_:
        list_.append(input_)
        object_list.append(Class(input_))
        save_items("drink.txt", list_, "Drinks")
        print("Thank you! The information has been stored.")
    else:
        print("Name already exists! Please try another Name")
    

def number_selection(message):
    try:
        input_ = int(input(message))
    except:
        print("ERROR! Invalid Input")
        return "ERROR"
    return input_

def assign_favourite(title, fav, data, data_2):
    temp = []
    temp_2 = []
    for index, item in enumerate(data, start=1):
        temp.append(f"[{index}] {item}")
    table("people", temp) 
    name = number_selection("\nSelect number next to the name\n")
    print(name)

    for index, value in enumerate(data_2, start = 1):
        temp_2.append(f"[{index}] {value}")
    table("drinks", temp_2)
    drink = number_selection("\n Select the number next to your favoruite drink: \n")
    
    fav[data[name-1]] = data_2[drink-1]
    print("\nFavourites Stored")
    
    return fav
