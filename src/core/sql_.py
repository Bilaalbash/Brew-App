import pymysql as sql
from src.core.class_ import Test_person, Test_drink
import src.core.functions as f
import csv

people = []
drinks = []

def add_to_database():
    connection = sql_.connect(host = "localhost", port = 33066, user = "root", passwd = "password", db = "brew_app", autocommit = True)
    cursor = connection.cursor()
    people = []
    file_path = f'./src/data/people.csv'
    
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        sql ="INSERT INTO people (first_name, surname, age) VALUES (%s, %s, %s)"
        
        for line in csv_reader:
            people.append(Test_person(line[0],line[1],line[2]))

        for person in people:
            args = [person.firstname, person.surname, person.age]
            cursor.execute(sql, args)

    cursor.close()
    connection.close()

def save_to_database(list_, command):
    connection = sql.connect(host = "localhost", port = 33066, user = "root", passwd = "password", db = "brew_app", autocommit = True)
    cursor = connection.cursor()

    if command == "people":
        sql_command = "INSERT INTO people (first_name, surname, age) VALUES (%s, %s, %s)"
        args = [list_[-1].firstname, list_[-1].surname, list_[-1].age]
    elif command == "drink":
        sql_command = "INSERT INTO drink (DrinkName, age) VALUES (%s, %s)"
        args = [list_[-1].name, list_[-1].age]

    cursor.execute(sql_command, args)

    cursor.close()
    connection.close()

def get_from_table(command, class_name, data, check):
    connection = sql.connect(host = "localhost", port = 33066, user = "root", passwd = "password", db = "brew_app")
    cursor = connection.cursor()

    cursor.execute(f"SELECT * FROM {command}")
    
    while True:
        row = cursor.fetchone()
        if row == None:
            break
        if check == 'people':
            data.append(class_name(row[0], row[1], row[2]))
            names = [f'{i.firstname} {i.surname}' for i in data]

        elif check == 'drink':
            data.append(class_name(row[0], row[1]))
            names = [i.name for i in data]
    
    connection.commit()
    cursor.close()
    connection.close()
    return data



if __name__ == "__main__":
    #get_from_table(people_cmd, Test_person, people, 'people')
    pass