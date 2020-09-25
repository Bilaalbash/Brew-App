import functions_definitions as f

people =[]

people = f.load_txt("people.txt", people)

print(f'person name {people}')