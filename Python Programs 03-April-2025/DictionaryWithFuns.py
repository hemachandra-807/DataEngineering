'''Dictionary Methods Explained:
Accessing Values:

dict[key] Retrieves the value for a key (raises an error if key not found).

dict.get(key, default) Retrieves the value for a key (returns default if key not found).

Modifying Dictionary:

dict[key] = value Adds or updates a key-value pair.

Removing Elements:

dict.pop(key) Removes a key and returns its value.

dict.popitem() Removes and returns the last key-value pair.

del dict[key] Deletes a key from the dictionary.

dict.clear() Removes all elements.

Iterating & Extracting Data:

dict.keys() Returns all keys.

dict.values() Returns all values.

dict.items() Returns key-value pairs.

Copying Dictionary:

dict.copy() Returns a shallow copy of the dictionary.'''

# Creating a dictionary
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Accessing values
name = my_dict["name"]  # Access value using key
age = my_dict.get("age")  # Another way to access value
# Adding & Updating values
my_dict["age"] = 26  # Update value
my_dict["country"] = "USA"  # Add new key-value pair

# Removing elements
removed_value = my_dict.pop("city")  # Removes 'city' and returns its value
last_item = my_dict.popitem()  # Removes and returns the last key-value pair
del my_dict["age"]  # Deletes a specific key

# Checking for a key
is_name_present = "name" in my_dict  # Returns True if key exists

# Iterating through dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Getting all keys and values
keys = my_dict.keys()  # Returns all keys
values = my_dict.values()  # Returns all values

# Copying a dictionary
copy_dict = my_dict.copy()

# Clearing all elements
my_dict.clear()

# Displaying results
print("Modified Dictionary:", my_dict)
print("Removed Value:", removed_value)
print("Last Removed Item:", last_item)
print("Is 'name' Present:", is_name_present)
print("Keys:", keys)
print("Values:", values)
print("Copied Dictionary:", copy_dict)