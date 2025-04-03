'''Explanation of Set Methods:
add(value): Adds a single element.

update(iterable): Adds multiple elements.

remove(value): Removes an element (raises an error if not found).

discard(value): Removes an element (no error if not found).

pop(): Removes and returns a random element.

union(set): Returns a new set with elements from both sets.

intersection(set): Returns a new set with common elements.

difference(set): Returns a new set with elements in the first set but not in the second.

symmetric_difference(set): Returns elements in either set but not in both.

in: Checks if an element is present in the set.'''

# Creating a set
my_set = {10, 20, 30, 40, 50}

# Adding elements
my_set.add(60)  # Adds 60 to the set
my_set.update([70, 80])  # Adds multiple elements

# Removing elements
my_set.remove(30)  # Removes 30 (raises an error if not found)
my_set.discard(100)  # Does nothing if 100 is not found
popped_element = my_set.pop()  # Removes and returns a random element

# Set operations
another_set = {40, 50, 60, 90}

union_set = my_set.union(another_set)  # Combines both sets
intersection_set = my_set.intersection(another_set)  # Common elements
difference_set = my_set.difference(another_set)  # Elements in my_set but not in another_set
symmetric_difference_set = my_set.symmetric_difference(another_set)  # Elements in either set but not both

# Checking membership
is_present = 50 in my_set  # Returns True if 50 is in the set

# Displaying results
print("Modified Set:", my_set)
print("Popped Element:", popped_element)
print("Union Set:", union_set)
print("Intersection Set:", intersection_set)
print("Difference Set:", difference_set)
print("Symmetric Difference Set:", symmetric_difference_set)
print("Is 50 Present:", is_present)
