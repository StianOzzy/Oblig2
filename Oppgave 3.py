tolkiens_books = ["The Hobbit", "Farmer Giles of Ham", "The Fellowship of the Ring", "The Two Towers", "The Return of the King", "The adventures of Tom Bombadil", "Tree and Leaf"]

# Henter ut bøker fra lista
book1and2 = tolkiens_books[:2]
book6and7 = tolkiens_books[-2:]

# Printer de to første, og 2 siste bøkene fra lista
print(f"De 2 første bøkene fra lista er: {book1and2}")
print(f"De 2 siste bøkene fra lista er: {book6and7}")

# Legger til flere bøker i lista
tolkiens_books.append("The Silmarillion")
tolkiens_books.append("Unfinished Tales")

# Endrer tittel på alle Lord of the Rings-bøkene
tolkiens_books[2] = "Lord of the Rings: The Fellowship of the Ring"
tolkiens_books[3] = "Lord of the Rings: The Two Towers"
tolkiens_books[4] = "Lord of the Rings: The Return of the King"

# Printer alle bøkene fra lista, sortert alfabetisk
print("\nAlle Tolkiens bøker, sortert alfabetisk:")
print(sorted(tolkiens_books))