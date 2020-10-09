import src.core.functions as f
import unittest
from unittest.mock import Mock, patch
from src.core.class_ import Person, Drink

class Test_Methods(unittest.TestCase):

    @patch("core.functions.number_selection")
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

    @patch("builtins.input")
    def test_add_name(self, mock_input):
        #Arrange
        person = Person
        mock_input.side_effect = ['Nathan', '22']
        expected_name = 'Nathan'
        expected_age = 22

        people_list = []
        object_list = []

        #Act
        f.add_name(people_list, 'people', object_list, person)

        #Assert
        self.assertEqual(object_list[-1].name, expected_name)
        self.assertEqual(object_list[-1].age, expected_age)

    @patch('builtins.input')
    def test_number_selection(self, input_mock):
        #Arrange
        input_mock.return_value = "1"
        expected = 1

        #Act
        actual = f.number_selection('Test!')

        #Assert
        self.assertEqual(actual,expected)

    def test_get_width(self):
        #Arrange
        title = 'People'
        people_list = ['Harry', 'Ron', 'Hermoine'] 
        expected = 9

        #Act
        actual = f.get_width(title, people_list)

        #Assert
        self.assertEqual(actual,expected)

    def test_enumerate_data(self):
        #Arrange
        people_list = ['Harry', 'Ron', 'Hermoine']
        new_list = []

        expected = ['[1] Harry', '[2] Ron', '[3] Hermoine']

        #Act
        actual = f.enumerate_data(people_list, new_list)
        #Assert
        self.assertEqual(actual,expected)


if __name__ == '__main__':
    f.clear()
    unittest.main()         
    