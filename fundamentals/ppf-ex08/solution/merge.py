book_names = ["Solaris", "Dune", "Ice", "Kindred"]
book_years = [1961, 1965, 1967, 1979]

# Your code here
books = {}
for i in range(len(book_names)):
    books[book_names[i]] = book_years[i]

print(books)

