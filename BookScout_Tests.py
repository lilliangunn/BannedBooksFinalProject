# Load sample data for testing
data = pd.DataFrame({
   'title': [
       'The Catcher in the Rye',
       'To Kill a Mockingbird',
       'The Great Gatsby',
       'Pride and Prejudice',
       'The Lord of the Rings',
       'Harry Potter and the Philosopher\'s Stone'
   ],
   'author': [
       'J.D. Salinger',
       'Harper Lee',
       'F. Scott Fitzgerald',
       'Jane Austen',
       'J.R.R. Tolkien',
       'J.K. Rowling'
   ],
   'publisher': [
       'Little, Brown and Company',
       'J. B. Lippincott & Co.',
       'Charles Scribner\'s Sons',
       'T. Egerton, Whitehall',
       'Allen & Unwin',
       'Bloomsbury Publishing'
   ]
})


# Test 1: Search for book that exists in dataset (by title)
search_result = search_books('The Great Gatsby', data, 'title')
assert len(search_result) == 1
assert search_result[0] == 'The Great Gatsby'

# Test 2: Search for book that does not exist in dataset (by title)
search_result = search_books('The Hobbit', data, 'title')
assert len(search_result) == 0

# Test 3: Search for book with partial match (by title)
search_result = search_books('Harry Potter', data, 'title')
assert len(search_result) == 1
assert search_result[0] == 'Harry Potter and the Philosopher\'s Stone'

# Test 4: Search for book with case-insensitive match (by title)
search_result = search_books('the catcher in the rye', data, 'title')
assert len(search_result) == 1
assert search_result[0] == 'The Catcher in the Rye'

# Test 5: Search for book by author
search_result = search_books('jane austen', data, 'author')
assert len(search_result) == 1
assert search_result[0] == 'Pride and Prejudice'

# Test 6: Search for book by publisher
search_result = search_books('Bloomsbury', data, 'publisher')
assert len(search_result) == 1
assert search_result[0] == 'Bloomsbury Publishing'

# Test 7: Search for book with missing data
data.loc[0, 'title'] = None
search_result = search_books('Catcher', data, 'title')
assert len(search_result) == 1
assert search_result[0] == 'The Catcher in the Rye'

