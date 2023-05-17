import unittest
import pandas as pd
from customtkinter import END
from tkinter import END

class TestBookScoutGUI(unittest.TestCase):
    def setUp(self):
        # Mock data to simulate the CSV file
        self.data = pd.DataFrame({
            'title': ['Joe', 'The Aeronaut\'s Windlass', 'Blood Memory'],
            'author': ['Larry Brown', 'Jim Butcher', 'Greg Iles'],
            'date_published': ['1980', 'May 15th, 2020', 'June 2003']
            'publisher': ['Penguin', 'Robber Baron', 'Greenleaf']
            'series': ['(Chosen ones)', '(Boring books)', '(Cool Books)']
            'rating_count': ['111', '32', '5']
            'average_rating': ['3.4', '5', '2.3']
            'five_star_ratings': ['55', '3', '2']
            'one_star_ratings': ['30', '10', '0']
            'awards':['Trust 2009', 'Lifetime 2020',  'Teens 2004']
            'genre_and_votes': ['Children 11', 'Action 13, Romance 55', 'Action 6, Grief 44']
            'link':['abcd.com', 'efghi.com', 'jklmno.com']
        })

        self.app = BookScoutGUI()
        self.app.data = self.data  # Replace actual data with mock data

    def test_search_books(self):
        # Test search by title
        self.app.input_var.set('title')
        self.app.input_box.insert(0, 'Joe')
        result = self.app.search_books()
        self.assertEqual(result, [('Joe', 'Larry Brown', '1980', 'Penguin', '(Chosen ones)', '111', '3.4', '55', '30', 'Trust 2009', 'Children 11', 'abcd.com' )])

        # Test search by author
        self.app.input_var.set('author')
        self.app.input_box.delete(0, END)
        self.app.input_box.insert(0, 'Jim Butcher')
        result = self.app.search_books()
        self.assertEqual(result, [('The Aeronaut\'s Windlass', 'Jim Butcher', 'May 15th, 2020', 'Robber Baron', '(Boring books)', '32', '5', '3', '10', 'Lifetime 2020', 'Action 13, Romance 55', 'efghi.com')])

        # Test search with no results
        self.app.input_box.delete(0, END)
        self.app.input_box.insert(0, 'Nonexistent')
        result = self.app.search_books()
        self.assertEqual(result, [])
        
    def test_clear_results(self):
        self.app.input_var.set('title') #reset the search column
        self.app.input_box.insert(0, 'Joe')
        self.app.search_books()
        self.app.clear_results()
        self.assertEqual(self.app.result_box.get('1.0', END), '\n')
        
    def test_clear_input(self):
        self.app.input_box.insert(0, 'Joe')
        self.app.clear_input()
        self.assertEqual(self.app.input_box.get(), '')

if __name__ == '__main__':
    unittest.main()
