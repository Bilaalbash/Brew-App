import class_ as a
import csv

def load_txt(filepath):
    temp_list = []
    try:
        txt_file = open(filepath,'r')
        for line in txt_file:
            temp_list.append(line.strip())
        
        return temp_list

    except FileNotFoundError as fnfe:
        print('Unable to open file: ' + str(fnfe))
        return []
    except Exception as e:
        print('An error occurred: ' + str(e))
        return []    
    finally:
        txt_file.close()

def save_items(filepath, items, name):
    try:
        items_file = open(filepath,'w')
        for item in items:
            items_file.write(item + '\n')
    except:
        print(f"Unable to open {filepath} for writing")
    finally:
        items_file.close()
        print(f"Successfully saved {name}")

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

def order_round(drink, people):
    temp_drink = []
    temp_name = []
    drink_active = True
    global orders

    orders = []

    if drink_active == True:
        for index, item in enumerate(people, start=1):
            temp_name.append(f"[{index}] {item}")
        table("Whos Round is it?", temp_name)
        owner = input("Whos Round is it: ")
        round = a.Round(owner)
        
        for index, item in enumerate(drink, start=1):
            temp_drink.append(f"[{index}] {item}")
        table("   Menu", temp_drink)
        print("Enter number that is next to the drink you want\n")

        for name in people:
            select = number_selection(f"{name}'s Order: ")
            bev = drink[select-1]
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
        for index, names in enumerate(data):
            round_writer.writerow([f"{orders[index]}"])
        # except:
        #     print("Unable to Write Round")

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

def add(list_, data):
    input_ = input(f"What is the name of the {data}?\n")
    if input_ == "":
        print("\nERROR missing Name or Drink!")
        return

    if input_ not in list_:
        list_.append(input_)
    else:
        print("Name already exists! Please try another Name")
    
    print("Thank you! The information has been stored.")

def number_selection(message):
    try:
        input_ = int(input(message))
    except:
        print("ERROR! Invalid Input")
    return input_

def assign_favourite(title, fav, data, data_2):
    temp = []
    temp_2 = []
    for index, item in enumerate(data, start=1):
        temp.append(f"[{index}] {item}")
    table("people", temp) 
    name = number_selection("\nSelect number next to the name\n")

    for index, value in enumerate(data_2, start = 1):
        temp_2.append(f"[{index}] {value}")
    table("drinks", temp_2)
    drink = number_selection("\n Select the number next to your favoruite drink: \n")
    
    fav[data[name-1]] = data_2[drink-1]