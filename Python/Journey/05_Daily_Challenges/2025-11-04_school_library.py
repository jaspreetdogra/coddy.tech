def find_book_descriptions(catalog, query):
    """
    Scholar's Library 📚
    Function to search for book descriptions in a library catalog 
    that match a given query (case-insensitive).
    
    Steps to solve:
    1️⃣ Convert the query string to lowercase for case-insensitive comparison.
    2️⃣ Initialize an empty list to store matching book descriptions.
    3️⃣ Iterate through each book in the catalog.
    4️⃣ For each book:
        - Extract the book ID and description.
        - Convert both to lowercase for comparison.
        - If the query appears in either the ID or description, add the description to the results list.
    5️⃣ After iterating through all books:
        - If there are matches, join them with newline characters and return.
        - Otherwise, return "No books found.".
    """

    # Step 1: Convert query to lowercase for case-insensitive search
    query = query.lower()

    # Step 2: Initialize list for storing matching book descriptions
    matching_descriptions = []

    # Step 3: Iterate through catalog
    for book in catalog:
        book_id, description = book[0], book[1]

        # Step 4: Case-insensitive comparison
        if query in book_id.lower() or query in description.lower():
            matching_descriptions.append(description)

    # Step 5: Return results
    if matching_descriptions:
        return "\n".join(matching_descriptions)
    else:
        return "No books found."
