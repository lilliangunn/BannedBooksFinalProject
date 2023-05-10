# Import necessary libraries
import tkinter
import pandas as pd

# Define function to search for book
def search_book():
    # Read CSV file and preprocess data
    data = pd.read_csv('kindle_reviews.csv')
    # Remove duplicates and handle missing values
    data = data.drop_duplicates().fillna('')
  
    # Get user input from GUI
    user_input = input_box.get()
  
    # Search for book in dataset
    result = data[data['title'].str.contains(user_input, na=False)]
  
    # Display results to user
    result_box.delete(0, tkinter.END)
    for index, row in result.iterrows():
        result_box.insert(tkinter.END, row['title'])

# Create GUI
window = tkinter.Tk()
window.title('BookScout')
input_label = tkinter.Label(window, text='Enter a book title:')
input_label.pack()
input_box = tkinter.Entry(window)
input_box.pack()
search_button = tkinter.Button(window, text='Search', command=search_book)
search_button.pack()
result_label = tkinter.Label(window, text='Search results:')
result_label.pack()
result_box = tkinter.Listbox(window)
result_box.pack()

# Start GUI
window.mainloop()


