# for x in 'word':
#     print(x)

# fav_languages = "my favorite computer languages are:" \
#     " Python " \
#     "Javascript " \
#     "C++ " 
# print(fav_languages)

# fav_languages = '''my favorite computer languages are:
#     Python
#     JavaScript
#     C++'''
# print(fav_languages)

# my_str = "can't touch this"
# print(my_str[6])

# new_str = "hello "
# for c in "world":
#     new_str += c
# print(new_str)

# opinion = "thIs iS niCe"
# print(opinion.upper())
# print(opinion.lower())
# print(opinion.capitalize())
# print(opinion.title())

# instructor = "Juliana"
# print(instructor.find('J'))
# print(instructor.find('A'))
# print(instructor.find('n'))

# words = ['Python', 'is', 'great']
# sentence = ' '.join(words)
# print(sentence)

# numbers = ['1', '2', '3', '4']
# numbers_string = ', '.join(numbers)
# print(numbers_string)

# # Exercise 1
# text = "Python is Fun!"

# # convert to all uppercase
# # text = text.upper()
# # print(text)

# # make the first letter uppercase
# # text = text.capitalize()
# # print(text)

# # # Make the first letter of each word uppercase
# # text = text.title()
# # print(text)

# # Find the index of "F". What happens if you use lower case in the method
# # print(text.find('F'))
# # if 'f' was lower case it would print -1 as the index because .find() method is case sensitive

# # Find a substring
# if "Python" in text:
#     print("Found it!")
# else:
#     print("I don't think it's there chief")

# # Checks if iterable is an aphabetical letter
# serial_num = 'B456 523'
# print(serial_num.isalpha())
# print(serial_num[0].isalpha())

# # Checks if the iterable is a space
# serial_num = "1234 5678"
# print(serial_num.isspace())
# print(serial_num[0].isspace())
# print(serial_num[4].isspace())

# #Checks if the iterable is a lower case letter
# greeting = "Hello World"
# print(greeting.islower())
# print(greeting[0].islower())
# print(greeting[1].islower())
# greeting = greeting.lower()
# print(greeting.islower())

# #Checks if the string is a title(first letter in each word is capitalized)
# greeting = "Hello World"
# print(greeting.istitle())
# print(greeting.title().istitle())
# print("not Awesome Sauce".istitle())
# print("Awesome Sauce".istitle())


# Checks if a string ends with a certain set of characters
# print("string".endswith('g'))
# print("awesome".endswith('foo'))

# # Partitions a string - meaning it takes a string and turns it into a tuple with 3 parts. You can set how the split will be made
# word = "awesome"
# # print(word.partition('i')) # looks for the letter 'i' as the separator, since there is no i the first part in the tuple is the whole world
# email = "email@gmail.com"
# print(email.partition('@'))

# Exercise 2


sentence = input("Please type a short sentence: ")
non_alpha = []
whitespace = []
for iterable in sentence:
    if not iterable.isalpha():
        non_alpha.append(iterable)
print(f"There are {len(non_alpha)} non alphabetical iterables in the sentence")
if sentence.endswith('!'):
    print("Sentence ends with an exclamation mark!")
else:
    print("Sentence does not end with an exclamation mark.")
for iterable in sentence:
    if iterable.isspace():
        whitespace.append(iterable)
print(f"There are {len(whitespace)} spaces in the sentence.")