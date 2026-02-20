library_catalog = [
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "genre": "Fiction",
        "rating": 4.8,
        "year": 1960
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "genre": "Romance",
        "rating": 4.7,
        "year": 1949
    },
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "genre": "Classic",
        "rating": 4.5,
        "year": 1925
    },
    {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "genre": "Classic",
        "rating": 4.2,
        "year": 1951
    },
    {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "genre": "Romance",
        "rating": 4.6,
        "year": 1813
    },
    {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "genre": "Classic",
        "rating": 4.7,
        "year": 1937
    },
    {
        "title": "Sapiens: A Brief History of Humankind",
        "author": "Yuval Noah Harari",
        "genre": "Fiction",
        "rating": 4.6,
        "year": 2011
    },
    {
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "genre": "Fiction",
        "rating": 4.3,
        "year": 1988
    },
    {
        "title": "The Da Vinci Code",
        "author": "Dan Brown",
        "genre": "Classic",
        "rating": 4.4,
        "year": 2003
    },
    {
        "title": "The Road",
        "author": "Cormac McCarthy",
        "genre": "Romance",
        "rating": 4.1,
        "year": 2006
    }
]
import statistics

highest_rating_per_genre = {}
for mydict in library_catalog:
    genre = mydict.get('genre')
    rating = mydict.get('rating')

    if genre not in highest_rating_per_genre or (rating > highest_rating_per_genre[genre]):
        highest_rating_per_genre[genre] = rating

avg_rating = statistics.mean(highest_rating_per_genre.values())

print(highest_rating_per_genre)
print(avg_rating)

print(sorted(highest_rating_per_genre))