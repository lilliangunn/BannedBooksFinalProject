import pandas as pd

# Load sample data for testing
data = pd.DataFrame({
    'title': [
        'The Catcher in the Rye',
        'To Kill a Mockingbird',
        'The Great Gatsby',
        'Pride and Prejudice',
        'The Lord of the Rings',
        'Harry Potter and the Philosopher\'s Stone'
    ]
})

# Test 1: Search for book that exists in dataset
search_result = search_book('The Great Gatsby', data)
assert len(search_result) == 1
assert search_result[0] == 'The Great Gatsby'

# Test 2: Search for book that does not exist in dataset
search_result = search_book('The Hobbit', data)
assert len(search_result) == 0

# Test 3: Search for book with partial match
search_result = search_book('Harry Potter', data)
assert len(search_result) == 1
assert search_result[0] == 'Harry Potter and the Philosopher\'s Stone'

# Test 4: Search for book with case-insensitive match
search_result = search_book('the catcher in the rye', data)
assert len(search_result) == 1
assert search_result[0] == 'The Catcher in the Rye'
