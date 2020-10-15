import src.core.class_ as a

import csv
import os

def clear():
    os.system("clear")

def wait():
    input("\nPress Enter to return to Menu\n")

def enumerate_data(list_1, list_2):
    for index, item in enumerate(list_1, start=1):
            list_2.append(f"[{index}] {item}")
    return list_2


    
def number_selection(message):
    try:
        input_ = int(input(message))
    except:
        print("ERROR! Invalid Input")
        return "ERROR"
    return input_
