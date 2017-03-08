""" Lists """

print 'Lists'

list_of_scientists = [
    'Marie Curie',
    'Ada Lovelace',
    'Margaret Hamilton'
]

print list_of_scientists # All elements
print list_of_scientists[0] # Marie Curie
print list_of_scientists[1:] # Ada Lovelance and Margaret Hamilton
print list_of_scientists[:2] # Marie Curie and Ada Lovelace

""" Appending an element """
print 'Appending an element'

list_of_scientists.append('Dorothy Vaughan')
print list_of_scientists

list_of_scientists += ['Katherine Johnson']
print list_of_scientists

""" Removing an element """
list_of_scientists.remove('Marie Curie')
print 'Removing an element'
print list_of_scientists

""" Sorted """
list_of_scientists_sorted = sorted(list_of_scientists)
print "Sorted"
print list_of_scientists_sorted


""" MIN AND MAX """
totals = [1, 2, 25, 30, 7, 6, -5]
print min(totals)
print max(totals)

