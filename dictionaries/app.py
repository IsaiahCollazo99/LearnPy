person = {
    'name': "Isaiah",
    'age': 21,
    'gender': "Male",
    'is_single': False
}

person2 = {
    'name': "Imran",
    'age': 27,
    'gender': "Male",
    'is_single': True
}

# Do the same thing
print(person['name'])
print(person.get('name'))

# Get has a default statement that returns if a key doesn't exist
print(person.get('wow', 'That key doesnt exist'))