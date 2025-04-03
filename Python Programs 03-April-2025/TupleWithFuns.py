'''Explanation of Tuple Operations:
Indexing: Accessing elements using [] notation.

Slicing: Extracting a portion using [start:end].

index(value): Returns the index of the first occurrence of a value.

count(value): Counts occurrences of a value.

Concatenation (+): Merges two tuples.

Repetition (*): Repeats elements.

len(tuple): Returns the total number of elements.'''

my_tuple = (10, 20, 30, 40, 50, 20)
# Accessing elements
first_element = my_tuple[0]  # Accessing first element
last_element = my_tuple[-1]  # Accessing last element
sliced_tuple = my_tuple[1:4]  # Slicing from index 1 to 3

# Finding elements
index_30 = my_tuple.index(30)  # Returns index of first occurrence of 30
count_20 = my_tuple.count(20)  # Counts occurrences of 20

# Concatenation and repetition
new_tuple = my_tuple + (60, 70)  # Concatenating tuples
repeated_tuple = my_tuple * 2  # Repeating elements

# Tuple length
tuple_length = len(my_tuple)

# Displaying results
print("Original Tuple:", my_tuple)
print("First Element:", first_element)
print("Last Element:", last_element)
print("Sliced Tuple:", sliced_tuple)
print("Index of 30:", index_30)
print("Count of 20:", count_20)
print("Concatenated Tuple:", new_tuple)
print("Repeated Tuple:", repeated_tuple)
print("Tuple Length:", tuple_length)