import sys
import csv
import src.core.functions as f
import src.core.class_ as a
from src.core.adding import add_name, add_drink, assign_favourite
from src.core.sql_ import get_from_table, save_to_database
from src.core.printing import print_menu, table, long_table
from src.core.saving import save_fave, load_csv
from src.core.create_round import order_round
import pymysql as sql_

# KHALID WOZ ERE
# NICE APP LIKE MATE 

f.clear()
PREFERNCES_FILE = "./src/data/preferences.csv"
args = sys.argv
APP_NAME = "Brew App"
drink = []
people = []

def start():

    while True:
        
        print_menu(APP_NAME)
        names = [person.firstname for person in people]
        drink_names = [drink.name for drink in beverages]
        user_input = f.number_selection("Please Choose an Option\n")
        preferences = load_csv("./src/data/preferences.csv")


        if user_input == 1: # View Peoples List
            table("Table 20", names)
            f.wait()
        elif user_input == 2: # View Drinks List
            table("Drinks Menu", drink_names)
            f.wait()
        elif user_input == 3: # View Favourites List
            long_table("    Preferences   ", preferences)
            f.wait()
        elif user_input == 4: # Add a person
            add_name(names, people)
            save_to_database(people, "people")
            f.wait()
        elif user_input == 5: # Add a Drink
            add_drink(drink_names, beverages)
            save_to_database(beverages, "drink")
            f.wait()
        elif user_input == 6: # Set a Favoruite Drink
            assign_favourite("Favourite Drinks List", preferences, names, drink_names)
            save_fave(PREFERNCES_FILE, preferences)
            f.wait()
        elif user_input == 7: #Rounds
            order_round(drink_names, names, people, beverages)
            f.wait()
        elif user_input == 8: # Close Application
            print(f"\nThank you for using {APP_NAME}")
            exit()
        else:
            print("ERROR!, Please check if the input is valid\n")
            f.wait()

if __name__ == "__main__":
    f.clear()
    people = get_from_table("people", a.Test_person, people, "people")
    beverages = get_from_table("drink", a.Test_drink, drink, "drink")
    start()