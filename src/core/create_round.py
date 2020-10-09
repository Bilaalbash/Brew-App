from src.core.saving import save_csv

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