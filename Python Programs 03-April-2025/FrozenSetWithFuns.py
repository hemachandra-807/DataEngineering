# Creating a frozenset
my_frozenset = frozenset([10, 20, 30, 40, 50])

# Creating another frozenset
another_frozenset = frozenset([30, 40, 50, 60, 70])

# Set operations
union_set = my_frozenset | another_frozenset  # Union
intersection_set = my_frozenset & another_frozenset  # Intersection
difference_set = my_frozenset - another_frozenset  # Difference
symmetric_difference_set = my_frozenset ^ another_frozenset  # Symmetric Difference

# Membership checking
is_present = 30 in my_frozenset  # True if 30 is in frozenset

# Displaying results
print("FrozenSet:", my_frozenset)
print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference:", difference_set)
print("Symmetric Difference:", symmetric_difference_set)
print("Is 30 Present:", is_present)
