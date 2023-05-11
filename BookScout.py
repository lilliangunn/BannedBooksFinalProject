"""
INST326 (0105) Final Project: BookScout
Professor Gabriel Cruz

By: Kenneth Yeaher and Lillian Gunn
"""

import tkinter
import pandas as pd

class BookScoutGUI:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title('BookScout')

        input_label = tkinter.Label(self.window, text='Search by:', width=50) #EDIT:added width=50 to default widen the GUI
        input_label.pack()
        self.input_var = tkinter.StringVar()
        input_dropdown = tkinter.OptionMenu(self.window, self.input_var, 'title', 'author')
        input_dropdown.pack()

        input_label = tkinter.Label(self.window, text='Enter search term:')
        input_label.pack()
        self.input_box = tkinter.Entry(self.window, width=20) #EDIT:width=20 to widen entry box a little
        self.input_box.pack()

        search_button = tkinter.Button(self.window, text='Search', command=self.search_books, bg = 'light green') #EDIT:colored search button green
        search_button.pack()

        result_label = tkinter.Label(self.window, text='Search results:')
        result_label.pack()
        self.result_box = tkinter.Listbox(self.window)
        self.result_box.pack(fill=tkinter.BOTH, expand=True) #EDIT: added expand to GUI

        #EDIT: added red clear_results button to bottom of GUI; new clear_results() method added also
        clear_results_button = tkinter.Button(self.window, text='Clear Results', command=self.clear_results, bg='red')
        clear_results_button.pack()



        # Load and preprocess data
        try:
            self.data = pd.read_csv('goodreads_books.csv')
            # Remove duplicates and handle missing values
            self.data = self.data.drop_duplicates().fillna('')
        except Exception as e:
            raise Exception("Error reading file: ", e)

        self.window.mainloop()

    def search_books(self):
        """
        Search for books in the dataset based on user input.

        Returns:
            A list of tuples with book titles and authors that match the search query.
        """
        search_column = self.input_var.get()
        user_input = self.input_box.get()

        # Search for book in dataset
        result = self.data[self.data[search_column].str.contains(user_input, na=False, case=False)]

        # Display results to user
        self.result_box.delete(0, tkinter.END)
        for index, row in result.iterrows():
            self.result_box.insert(tkinter.END, f"{row['title']} by {row['author']}")

        return [(row['title'], row['author']) for _, row in result.iterrows()]

    #EDIT: new clear_results method
    def clear_results(self):
        """
        Delete the items in the results box."""
        self.result_box.delete(0, tkinter.END)

if __name__ == '__main__':
    app = BookScoutGUI()
