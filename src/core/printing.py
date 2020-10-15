def print_menu(APP_NAME):
    print(f'''
Welcome to {APP_NAME}!
  ____                                            
 |  _ \                            /\                  
 | |_) | _ __  ___  __      __    /  \    _ __   _ __  
 |  _ < | '__|/ _ \ \ \ /\ / /   / /\ \  | '_ \ | '_ \ 
 | |_) || |  |  __/  \ V  V /   / ____ \ | |_) || |_) |
 |____/ |_|   \___|   \_/\_/   /_/    \_\| .__/ | .__/ 
                                         | |    | |    
                                         |_|    |_| 

Please select an option by entering a number

\t[1] Display Names on your Table
\t[2] Display Drinks Menu
\t[3] Display Preferences
\t[4] Add People
\t[5] Add Drink
\t[6] Set a Preference
\t[7] Order a Round
\t[8] Close Application
''')

def table(title, data): #Prints out table of data
    width = get_width(title, data)
    banner = (f"     +{'=' * width}+")
    print(f"{banner}\n     |{title.upper()}{' ' * (width - len(title))}|     \n{banner}")

    for item in data:
        print(f"     |{item}{' ' * (width - len(item))}|"  )
    print(f"{banner}\n")

def get_width(title, data):
    longest = len(title)

    for item in data:
        if len(item) > longest:
            longest = len(item)
    return longest + 1

def long_table(title, data):
    width = get_width(title, data)
    banner = (f"     +{'=' * width}+")
    print(f"{banner}\n     |{title.upper()}{' ' * (width - len(title))}|\n{banner}")

    for key, value in data.items():
        print(f"     |{key}: {value}{' ' * (width - len(value) - len(key)-2)}|")
    print(f"{banner}\n")