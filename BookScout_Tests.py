import unittest
import pandas as pd
from tkinter import END

class TestBookScoutGUI(unittest.TestCase):
    def setUp(self):
        # Mock data to simulate the CSV file
        self.data = pd.DataFrame({
            'title': ['Joe', 'The Aeronaut\'s Windlass', 'Blood Memory'],
            'author': ['Larry Brown', 'Jim Butcher', 'Greg Iles'],
        })

        self.app = BookScoutGUI()
        self.app.data = self.data  # Replace actual data with mock data

    def test_search_books(self):
        # Test search by title
        self.app.input_var.set('title')
        self.app.input_box.insert(0, 'Joe')
        result = self.app.search_books()
        self.assertEqual(result, [('Joe', 'Larry Brown')])

        # Test search by author
        self.app.input_var.set('author')
        self.app.input_box.delete(0, END)
        self.app.input_box.insert(0, 'Jim Butcher')
        result = self.app.search_books()
        self.assertEqual(result, [('The Aeronaut\'s Windlass', 'Jim Butcher')])

        # Test search with no results
        self.app.input_box.delete(0, END)
        self.app.input_box.insert(0, 'Nonexistent')
        result = self.app.search_books()
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
