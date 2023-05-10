import tkinter
import pandas as pd


# Define function to search for book
def search_books(user_input=None, data=None, search_column='title'):
   # Read CSV file and preprocess data if not provided
   if data is None:
       try:
           data = pd.read_csv('amazon_books.csv')
           # Remove duplicates and handle missing values
           data = data.drop_duplicates().fillna('')
       except Exception as e:
           print("Error reading file: ", e)
           return []

   # Get user input from GUI if not provided
   if user_input is None:
       user_input = input_box.get()

   # Search for book in dataset
   result = data[data[search_column].str.contains(user_input, na=False, case=False)]

   # Display results to user if called from GUI
   if user_input is not None and data is None:
       result_box.delete(0, tkinter.END)
       for index, row in result.iterrows():
           result_box.insert(tkinter.END, row[search_column])

   # Return the search results for testing
   return result[search_column].tolist()


# Create GUI
window = tkinter.Tk()
window.title('BookScout')
input_label = tkinter.Label(window, text='Search by:')
input_label.pack()
input_dropdown = tkinter.OptionMenu(window, tkinter.StringVar(), 'title', 'author', 'publisher')
input_dropdown.pack()
input_label = tkinter.Label(window, text='Enter search term:')
input_label.pack()
input_box = tkinter.Entry(window)
input_box.pack()
search_button = tkinter.Button(window, text='Search', command=search_books)
search_button.pack()
result_label = tkinter.Label(window, text='Search results:')
result_label.pack()
result_box = tkinter.Listbox(window)
result_box.pack()


# Start GUI
window.mainloop()


