from src.core.saving import save_csv
from src.core.functions import enumerate_data, number_selection
from src.core.printing import table
from src.core.class_ import Round

def order_round(drink, people, people_class, drink_class):
    temp_drink = []
    temp_name = []
    drink_active = True
    global orders
    orders = []

    if drink_active == True:
        enumerate_data(people, temp_name)
        table("Whos Round is it?", temp_name)
        owner_input = number_selection("Whos Round is it: ")
        owner = people[owner_input-1]
        round = Round(owner)
        
        enumerate_data(drink, temp_drink)
        table("   Menu", temp_drink)
        print("Enter number that is next to the drink you want")

        for index, name in enumerate(people):
            option = input(f"\nDoes {name} want a drink (y/n): ")
            
            if option.lower() == "y" or option.lower() == "yes":
                select = number_selection(f"{name}'s Order: ")
                bev = drink[select-1]
                if people_class[index].age < drink_class[select-1].age:
                    print(f'{people_class[index].firstname} is too young to buy a {drink_class[select-1].name}\n')
                else:
                    round.add_order(name, bev)
                    orders.append(f"{round.name}, {round.drink}")
                    save_csv('./src/data/round.csv', round.owner, orders)
            elif option.lower() == "n" or option.lower() == "no":
                pass

            else:
                print("That is not a valid input.\n")
        print("")
        round.print_order()
    else:
        print("Sorry we're not taking orders right now")