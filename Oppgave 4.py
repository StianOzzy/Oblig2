# Lager en tom liste
empty_list = []


# Lager en liste som inneholder bøkene fra oppgave 3
tolkiens_books = ["Farmer Giles of Ham", "Lord of the Rings: The Fellowship of the Ring", "Lord of the Rings: The Return of the King",
                  "Lord of the Rings: The Two Towers","The Hobbit", "The Silmarillion", "The adventures of Tom Bombadil", "Tree and Leaf", "Unfinished Tales"]


# Sjekker hvert element i tolkens_books. Hvis de inneholder tittelen av Lord of the Rings bøkene, så legges de til den empty_list
for book in tolkiens_books:
    if book == "Lord of the Rings: The Fellowship of the Ring" or book == "Lord of the Rings: The Two Towers" or book == "Lord of the Rings: The Return of the King":
        empty_list.append(book)


# For hvert element i empty_list, skriv ut navnet på elementet
for book in empty_list:
    print(book)
