book_names = ["Solaris", "Dune", "Ice", "Kindred"]
book_years = [1961, 1965, 1967, 1979]
book_author = ['Elvis', 'Cristi', 'Vlad', 'Marius']

# Your code here
books = {}
for k in range(len(book_names)):
    books[book_names[k]] = book_years[k]

print(books)

books2 = {}

books2.update(zip(book_names, (zip(book_years, book_author))))


print(books2)
