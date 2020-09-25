import sys
import csv
import core.functions as f
import core.class_ as a
f.clear()

args = sys.argv
APP_NAME = "Brew App"
favourite = {}

def start():

    while True:
        f.print_menu(APP_NAME)
        people_names = [person.name for person in people]
        drink_names = [drink.name for drink in beverages]
        user_input = f.number_selection("Please Choose an Option\n")
    
        if user_input == 1: # View Peoples List
            f.table("names", people_names)
            f.wait()
        elif user_input == 2: # View Drinks List
            f.table("drinks", drink_names)
            f.wait()
        elif user_input == 3: # View Favourites List
            f.long_table("favourite drinks list", favourite)
            f.wait()
        elif user_input == 4: # Add a person
            f.add_name(people_names, "Person", people, a.Person)
            f.wait()
        elif user_input == 5: # Add a Drink
            f.add_drink(drink_names, "Drink", beverages, a.Drink)
            f.wait()
        elif user_input == 6: # Set a Favoruite Drink
            f.assign_favourite("Favourite Drinks List", favourite, people_names, drink_names)
            f.wait()
        elif user_input == 7: #Rounds
            f.order_round(drink_names, people_names, people, beverages)
            f.wait()
        elif user_input == 8: # Close Application
            f.save_items("people.txt", people_names, "People")
            f.save_items("drink.txt", drink_names, "Drinks")
            print(f"\nThank you for using {APP_NAME}")
            exit()
        else:
            print("ERROR!, Please check if the input is valid\n")
            f.wait()

if __name__ == "__main__":
    f.clear()
    people = f.load_people("../data/people.csv")
    beverages = f.load_drinks("../data/drink.csv")
    start()