import core.functions as f
import unittest
from unittest.mock import Mock, patch
from core.class_ import Person, Drink

class Test_Methods(unittest.TestCase):
    @patch("functions_definitions.number_selection")
    def test_assign_favourites(self, mock_number_selection):
        #Arrange
        person = Mock(Person)
        drink = Mock(Drink)

        person.name = 'Bilaal'
        person.age = 22
        drink.name = 'Water'
        drink.age = 0

        person_name = [person.name]
        drink_name = [drink.name]
        combo = {}
        mock_number_selection.return_value = 1
        expected = {'Bilaal':'Water'}

        #Act
        actual = f.assign_favourite('Favourite', combo, person_name, drink_name)
        
        #Assert
        self.assertEqual(actual,expected)

    # def test_get_width(self):
    #     #Arrange
    #     title = 'People'
    #     people_list = ['Harry', 'Ron', 'Hermoine'] 
    #     expected = 9

    #     #Act
    #     actual = f.get_width(title, people_list)

    #     #Assert
    #     self.assertEqual(actual,expected)

    # def test_enumerate_data(self):
    #     #Arrange
    #     people_list = ['Harry', 'Ron', 'Hermoine']
    #     new_list = []

    #     expected = ['[1] Harry', '[2] Ron', '[3] Hermoine']

    #     #Act
    #     actual = f.enumerate_data(people_list, new_list)
    #     #Assert
    #     self.assertEqual(actual,expected)

    # @patch('builtins.input')
    # def test_number_selection(self, input_mock):
    #     #Arrange
    #     #Make message
    #     #Patch input

    #     #Act
        
    #     #Assert

if __name__ == '__main__':
    f.clear()
    unittest.main()         
    



# def add_list_element(my_list, element):
#     """Appends specified element to specified list,
# IF the element is a string that contains only characters, and can not be
# empty, have all the characters be spaces, contain any numbers or be already in the list. """
#     if not element or element.isspace():
#         print("You have not entered anything!")
#     elif any(num in element for num in "0123456789"):
#         print("No numbers can be included in the name.")
#     elif element.capitalize() not in my_list:
#         my_list.append(element.capitalize())
#         print(f"Your choice: {element.capitalize()} was successfully added!")
#     else:
#         print("Already on the list. Try a different option.")
#     return my_list

# def add_list_element_unit_test():
#     #Arrange
#     my_list = ["Harry", "Ron"]  
#     element = "Hermoine"
#     expected = ["Harry", "Ron", "Hermoine"]

#     #Act
#     actual = add_list_element(my_list, element)

#     #assert
#     assert expected == actual



# get_width_unit_test()
