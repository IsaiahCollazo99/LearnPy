character_name = "JOHN"
character_age = 35
isMale = False

# print("There once was a man named " + character_name + ", ")
# print("he was " + str(character_age) + " years old. ")
# print("He really liked the name " + character_name + ", ")
# print("but didn't like being " + str(character_age) + ".")

print(character_name.lower()) # To Lower Case
print(character_name.upper()) # To Upper Case
print(character_name.isupper()) # Is completely upper case
print(character_name.islower()) # Is completely lower case

print(len(character_name)) # length
print(character_name[0]) # Indexing into str
print(character_name.index("J")) # Getting index of a character in str
print(character_name.index("OH")) # Getting index where the inputted phrase starts

print(character_name.replace("HN", "NNY")) # Replace words/letters (first arg) with others (second arg)

# if(isMale):
#     print("Hey dude")
# else:
#     print("Hello *insert indetity*")