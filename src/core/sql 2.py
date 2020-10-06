import pymysql as sql
from core.class_ import Test_person, Test_drink
import core.functions as f
import csv

people = []
drinks = []
drink_cmd = 'SELECT * FROM drink'
people_cmd = 'SELECT * FROM people'

def insert_person():
    connection = sql.connect(host = "localhost", port = 33066, user = "root", passwd = "password", db = "brew_app")
    cursor = connection.cursor()

    args = (2, "James", "Smith", 25)
    cursor.execute("INSERT INTO person (ID, FirstName, SurName, Age) VALUES (%s, %s, %s, %s)", args)
    connection.commit()

    cursor.close()
    connection.close()

def insert_drink():
    connection = sql.connect(host = "localhost", port = 33066, user = "root", passwd = "password", db = "brew_app")
    cursor = connection.cursor()

    args = (2, "Sprite", 0)
    cursor.execute("INSERT INTO drink (ID, DrinkName, Age) VALUES (%s, %s, %s)", args)
    connection.commit()
    

    cursor.close()
    connection.close()

def add_to_database():
    connection = sql.connect(host = "localhost", port = 33066, user = "root", passwd = "password", db = "brew_app", autocommit = True)
    cursor = connection.cursor()
    people = []
    file_path = f'./data/people.csv'
    
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        
        for line in csv_reader:
            people.append(Test_person(line[1],line[2],line[3]))

        for person in people:
            args = [person.firstname, person.surname, person.age]
            
            cursor.execute("INSERT INTO people (first_name, surname, age) VALUES (%s, %s, %s)", args)

    cursor.close()
    connection.close()

def get_from_table(command, class_name, data, check):
    connection = sql.connect(host = "localhost", port = 33066, user = "root", passwd = "password", db = "brew_app")
    cursor = connection.cursor()

    cursor.execute(command)
    
    while True:
        row = cursor.fetchone()
        if row == None:
            break
        if check == 'people':
            data.append(class_name(row[1], row[2], row[3]))
            names = [f'{i.firstname} {i.surname}' for i in data]

        elif check == 'drink':
            data.append(class_name(row[1], row[2]))
            names = [i.name for i in data]
    
    print(names)
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    #get_from_table(people_cmd, Test_person, people, 'people')
    add_to_database()