
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