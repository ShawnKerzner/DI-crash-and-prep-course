# authors = {
#     "Great Gatsby": "F. Scott Fitzgerald",
#     "Slaughterhouse Five": "Kurt Vonnegut",
#     "Of Mice and Men": "John Steinbeck"
# }

# print(authors["Great Gatsby"])
# print(authors["Of Mice and Men"])

# user_info = dict(name = "John")
# # print(user_info)
# # print(user_info['name'])
# user_info["name"] = "Dan"
# user_info["email"] = "dan@gmail.com"
# print(user_info)


# user_info_1 = dict(name="Alice", age="30", city="New York")
# # user_info.clear()
# # print(user_info)

# user_info_2 = {
#     "name": "Bob",
#     "age": 25,
#     "city": "Los Angeles"
# }
# print(user_info)
# user_info.clear()
# print(user_info)

# user_info_1_copy = user_info_1.copy()
# print(user_info_1_copy)
# print(user_info_1 is user_info_1_copy)


# user_info_2_copy = user_info_2.copy()
# print(user_info_2_copy)
# print(user_info_2 is user_info_2_copy)

# users = ["Alice", "Bob", "Charlie"]
# user_status = {}.fromkeys(users, "inactive")
# print(user_status)

# users = ["Alice", "Bob", "Charlie"]
# user_status = dict().fromkeys(users, "inactive")
# print(user_status)

# user_info = dict(name="Alice", age="30", city="New York")
# print(user_info.get("name"))
# print(user_info.get("no_key"))

# user_info = {"name": "Bob", "age": 25, "city": "Los Angeles"}
# print(user_info.get('city'))
# print(user_info.get('email'))

# user_info = {"name": "Bob", "age": 25, "city": "Los Angeles"}
# # print(user_info.items())
# # print(user_info.keys())
# print(user_info.pop("age"))
# print(user_info)

# user_info = dict(name="Alice", age=30, city="New York")
# print(user_info)
# additional_info = {'country': 'USA', 'email': "alice@example.com"}
# user_info.update(additional_info)
# print(user_info)

# user_info = {'name': 'Bob', 'age': 25, "city": "Los Angeles"}
# additional_info = {'age': 26, "city": "San Francisco"}
# user_info.update(additional_info)
# print(user_info)

# Exercise

books = {
    '1984': 'George Orwell',
    'Brave New World': 'Aldous Huxley',
    'The Great Gatsby': 'F. Scott Fitzgerald'
}

# Print the author of "1984"
print(books['1984'])
# Change the author of the great gatsby to Francis Scott Fitzgerald
books['The Great Gatsby'] = 'Francis Scott Fitzgerald'
print(books['The Great Gatsby'])
# Add a new book Moby Dick by Herman Melville
new_book = {'Moby Dick': "Herman Melville"}
books.update(new_book)
print(books)
# Use get method to try to access the auhtor of to kill a mockingbird
print(books.get("To Kill a Mockingbird"))
# remove the book a brave new world
books.pop('Brave New World')
print(books)



