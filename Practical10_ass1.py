import pandas as pd

try:
    df = pd.read_csv('books.csv')

    print("a) Complete Report of Books:")
    print(df.to_string(index=False))

    author_name = input("\nEnter Author Name to search: ")
    author_books = df[df['author'].str.lower() == author_name.lower()]
    print(f"\nb) Books by {author_name}:")
    print(author_books if not author_books.empty else "No books found for this author.")

    pub_house = input("\nEnter Publishing House to search: ")
    pub_books = df[df['publishing_house'].str.lower() == pub_house.lower()]
    print(f"\nc) Books by {pub_house}:")
    print(pub_books if not pub_books.empty else "No books found for this publisher.")

    cheapest_title = df.loc[df['price'].idxmin(), 'title']
    costliest_title = df.loc[df['price'].idxmax(), 'title']
    print(f"\nd) Cheapest Book: {cheapest_title}")
    print(f"   Costliest Book: {costliest_title}")

    print("\ne) Books sorted by Publication Year:")
    sorted_df = df.sort_values(by='publication_year')
    print(sorted_df.to_string(index=False))

except FileNotFoundError:
    print("Error: 'books.csv' file not found.")
  
