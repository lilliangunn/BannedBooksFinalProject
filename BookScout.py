"""
INST326 (0105) Final Project: BookScout
Professor Gabriel Cruz

By: Kenneth Yeaher and Lillian Gunn
"""
"""GUI to find information about any book from the Goodreads dataset based in its title or author name"""

#pip3 install customtkinter

import tkinter
import pandas as pd
import customtkinter
from customtkinter import StringVar

class BookScoutGUI:
    """Create GUI and find information based on a type of search term.
    Methods: search_books(): Search for books in the dataset based on user input.
            clear_results(): Delete the items in the results textbox.
            clear_input(): Delete the items in the search entry.
    """
    def __init__(self):
        """
        Design and return GUI named BookScout"""
        
        self.window = customtkinter.CTk()
        self.window.geometry("400x460")
        self.window.title('BookScout')
                
        #appearance of GUI        
        customtkinter.set_appearance_mode("light")   # Modes: system (default), light, dark
        customtkinter.set_default_color_theme('dark-blue')  # Themes: blue (default), dark-blue, green
        
        #create a frame for search options
        search_frame = customtkinter.CTkFrame(master=self.window)
        search_frame.pack(pady=10)
        #input label
        input_label = customtkinter.CTkLabel(search_frame, text='Search by:') #removed self.window, width=70
        input_label.pack()
        #dropdown menu
        self.input_var = customtkinter.StringVar(value="Choose title or author")
        input_dropdown = customtkinter.CTkOptionMenu(search_frame, values=['title', 'author'], variable=self.input_var) #removed self.window
        input_dropdown.pack()
    
        #Create a frame for search term
        search_term = customtkinter.CTkFrame(self.window)
        search_term.pack(pady=10)
        #entry box label
        input_label = customtkinter.CTkLabel(search_term, text='Enter a search term:') #removed self.window
        input_label.pack()
        #create entry box
        self.input_box = customtkinter.CTkEntry(search_term, width=200, placeholder_text='Type here') #removed self.window, width=20
        self.input_box.pack()
        #Search button for entry box
        search_button = customtkinter.CTkButton(search_term, text='Search', command=self.search_books, hover_color='green', width=15) #removed self.window, bg = 'light green' 
        search_button.pack(side=customtkinter.LEFT, padx=10, pady=5)
        #Clear entry box
        clear_search_button = customtkinter.CTkButton(search_term, text = 'Clear Search Box', command=self.clear_input, hover_color='red', width=15)
        clear_search_button.pack(side=customtkinter.LEFT, padx=5, pady=5)
        
        #Create a frame for search results
        results_frame = customtkinter.CTkFrame(self.window)
        results_frame.pack(pady=5, fill=customtkinter.BOTH, expand=True)
        #label for search results texbox
        result_label = customtkinter.CTkLabel(results_frame, text='Search results:') #removed self.window
        result_label.pack()
        #create scrollable textbox
        self.result_box = customtkinter.CTkTextbox(results_frame, activate_scrollbars=True, wrap='none', scrollbar_button_hover_color = 'blue') #removed self.window
        self.result_box.pack(fill=customtkinter.BOTH, expand=True)
        #clear results textbox button
        clear_results_button = customtkinter.CTkButton(results_frame, text='Clear Results', command=self.clear_results, hover_color='red') #removed bg='red'
        clear_results_button.pack(fill=customtkinter.BOTH, expand=False)

        # Load and preprocess data
        try:
            self.data = pd.read_csv('goodreads_books.csv')
            # Remove duplicates and handle missing values
            self.data = self.data.drop_duplicates().fillna('')
        except Exception as e:
            raise Exception("Error reading file: ", e)

        self.window.mainloop()

    #Method: search for books
    def search_books(self):
        """
        Search for books in the dataset based on user input.

        Returns:
            A list of tuples with book titles and authors that match the search query.
        """
        search_column = self.input_var.get()
        user_input = self.input_box.get()
        

        #check if a search option has been selected
        if search_column == 'Choose title or author':
            self.result_box.delete("0.0", customtkinter.END)
            self.result_box.insert(customtkinter.END, "STOP! You must first choose to search for a title or an author in the option menu.")
            return[]
        
        #check that user input is present
        if not user_input.strip():
            self.result_box.delete("0.0", customtkinter.END)
            self.result_box.insert(customtkinter.END, "STOP! You must pick a search option and then enter a search term.")
            return[]

        # Search for book in dataset
        result = self.data[self.data[search_column].str.contains(user_input, na=False, case=False)]

        # Display results to user
        self.result_box.delete("0.0", customtkinter.END)
        #insert count of total number of results at the top
        self.result_box.insert(customtkinter.END, f"Total results: {len(result)}\n\n")
        #what to return
        for index, row in result.iterrows():
            self.result_box.insert(customtkinter.END, f"{row['title']} by {row['author']}\n        Date Published: {row['date_published']}\n        Publisher: {row['publisher']}\n        Series: {row['series']}\n        Total number of ratings: {row['rating_count']}\n        Average Rating: {row['average_rating']}\n        Five Star Ratings: {row['five_star_ratings']}\n        One Star Ratings: {row['one_star_ratings']}\n        Awards: {row['awards']}\n        Genre and votes: {row['genre_and_votes']}\n        Goodreads Link: {row['link']}  \n\n")
        #return
        return [(row['title'], row['author'], row['average_rating']) for _, row in result.iterrows()]

    #new clear_results method for textbox
    def clear_results(self):
        """
        Delete the items in the results textbox.
        """
        self.result_box.delete("0.0", customtkinter.END)
    
    #clear input method for entry box
    def clear_input(self):
        """
        Delete the items in the search entry.
        """
        self.input_box.delete(0, customtkinter.END)
    

if __name__ == '__main__':
    app = BookScoutGUI()
