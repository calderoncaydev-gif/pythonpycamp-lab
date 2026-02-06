"""
15_comprehensions.py
--------------------
List, dict y set comprehensions.
"""

# List comprehension
numbers = [1, 2, 3, 4, 5]
squares = [n ** 2 for n in numbers]
evens = [n for n in numbers if n % 2 == 0]

print(squares)
print(evens)

# Dict comprehension
users = ["ana", "luis", "pedro"]
user_dict = {u: len(u) for u in users}

print(user_dict)

# Set comprehension
unique_lengths = {len(u) for u in users}
print(unique_lengths)
