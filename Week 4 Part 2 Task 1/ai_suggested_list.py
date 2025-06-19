
from operator import itemgetter

# Function to sort list of dictionaries by a specific key
def sort_list_of_dicts(lst, key):
    return sorted(lst, key=itemgetter(key))

# Sample list of dictionaries
data = [
    {'name': 'Chard', 'age': 23},
    {'name': 'Omolo', 'age': 53},
    {'name': 'Odhiambo', 'age': 28},
    {'name': 'Peter', 'age': 12},
    {'name': 'Florence', 'age': 34}
]

# Sort by 'age'
sorted_by_age = sort_list_of_dicts(data, 'age')

# Sort by 'name'
sorted_by_name = sort_list_of_dicts(data, 'name')

# Display results
print("Original list:")
print(data)

print("\nSorted by 'age':")
print(sorted_by_age)

print("\nSorted by 'name':")
print(sorted_by_name)