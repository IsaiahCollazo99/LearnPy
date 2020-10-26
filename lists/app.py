friends = ["Kaho", "Evan", "Lia", "Lucy"]
numbers = [1, 2, 3, 4]

# friends.extend(numbers) # Add two lists together
friends.append("Jeff") # Adds a new item to end of list
friends.append("Evan") # Adds a new item to end of list
friends.insert(3, "Imran") # Adds element to specified idx, other values pushed to right
# friends.remove("Evan") # Removes specified el from list

# friends.clear() # Resets list
# friends.pop() # Removes item from end of list

print(friends.index("Jeff")) # Gives idx of speicied value
print(friends.count("Evan")) # Gives number of times el appears in list
print(friends.reverse()) # Reverses order of the list

friends2 = friends.copy() # Creates a duplicate of a list

# friends.sort() # Sorts list

print(friends)
# print(friends[1:]) # Grabs all elements from the indicated int on
# print(friends[1:3]) # Grabs elements from first idx to second idx