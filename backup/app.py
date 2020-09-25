import sys
import functions_definitions as f
import class_ as a
import csv
args = sys.argv
APP_NAME = "Brew App"
people = []
beverages = []
favourite = {}

def start():
    while True:
        f.print_menu(APP_NAME)
        people = f.load_txt("people.txt")
        beverages = f.load_txt("drink.txt")
        user_input = f.number_selection("Please Choose an Option\n")
    
        if user_input == 1: # View Peoples List
            f.table("names", people)
            f.wait()
        elif user_input == 2: # View Drinks List
            f.table("drinks", beverages)
            f.wait()
        elif user_input == 3: # View Favourites List
            f.long_table("favourite drinks list", favourite)
            f.wait()
        elif user_input == 4: # Add a person
            f.add(people, "Person")
            f.save_items("people.txt", people, "People")
            f.wait()
        elif user_input == 5: # Add a Drink
            f.add(beverages, "Drink")
            f.save_items("drink.txt", beverages, "Drinks")
            f.wait()
        elif user_input == 6: # Set a Favoruite Drink
            f.assign_favourite("Favourite Drinks List", favourite, people, beverages)
            f.wait()
        elif user_input == 7: #Rounds
            f.order_round(beverages, people)
            f.wait()
        elif user_input == 8: # Close Application
            f.save_items("people.txt", people, "People")
            f.save_items("drink.txt", beverages, "Drinks")
            print(f"\nThank you for using {APP_NAME}")
            exit()
        else:
            print("ERROR!, Please check if the input is valid\n")
            f.wait()

if __name__ == "__main__":
    start()