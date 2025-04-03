# Using single or double quotes
str1 = 'Hello'
str2 = "World"

# Multi-line string using triple quotes
multi_line_str = """This is 
a multi-line 
string."""

print(str1, str2)
print(multi_line_str)

# Indexing (starts from 0)
first_char = str1[0]  # 'H'
last_char = str1[-1]  # 'o'

# Slicing
substring = str1[1:4]  # 'ell'

print("First Character:", first_char)
print("Last Character:", last_char)
print("Substring:", substring)

text = "  python programming  "

# Changing case
print(text.upper())  # "  PYTHON PROGRAMMING  "
print(text.lower())  # "  python programming  "
print(text.title())  # "  Python Programming  "

# Removing spaces
print(text.strip())  # Removes leading/trailing spaces

# Finding and replacing
print(text.find("programming"))  # Returns index of "programming"
print(text.replace("python", "Java"))  # Replaces "python" with "Java"

# Checking conditions
print(text.startswith("  python"))  # True
print(text.endswith("ing  "))  # True

# Splitting and joining
words = text.split()  # Splits into list ['python', 'programming']
joined_text = "-".join(words)  # Joins with "-"

print("Words List:", words)
print("Joined Text:", joined_text)

name = "Alice"
age = 25

# Using f-string (modern)
formatted_str = f"My name is {name} and I am {age} years old."

# Using format() method
formatted_str2 = "My name is {} and I am {} years old.".format(name, age)

print(formatted_str)
print(formatted_str2)
