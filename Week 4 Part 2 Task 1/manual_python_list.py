def sort_dictionary_by_key(dictionary_list, sorting_key):

    try:
        return sorted(dictionary_list, key=lambda d: d.get(sorting_key, None))
    
    except TypeError as e:
        print(f'Error string: {e}')
        return dictionary_list
    

# Corrected persons to be a list of dictionaries
persons = [
    {'name': 'Chard', 'age': 23},
    {'name': 'Omolo', 'age': 53},
    {'name': 'Odhiambo', 'age': 28},
    {'name': 'Peter', 'age': 12},
    {'name': 'Florence', 'age': 34}
]

sorted_persons = sort_dictionary_by_key(persons, 'age')
print(sorted_persons)
