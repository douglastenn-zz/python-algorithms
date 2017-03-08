""" 
Tuples
strongly typed
"""

print 'Tuples'

tuple_of_scientists = (
    'Marie Curie',
    'Ada Lovelace',
    'Margaret Hamilton'
)

print tuple_of_scientists # All elements
print tuple_of_scientists[0] # Marie Curie
print tuple_of_scientists[1:] # Ada Lovelance and Margaret Hamilton
print tuple_of_scientists[:2] # Marie Curie and Ada Lovelace

""" Appending an element """

tuple_of_scientists += ('Dorothy Vaughan',)
print 'Appending an element'
print tuple_of_scientists

""" Concat tuple with list """

list_of_scientists = ['Katherine Johnson']

# Wrong way!
# tuple_of_scientists = tuple_of_scientists + list_of_scientists 

tuple_of_scientists = tuple_of_scientists + tuple(list_of_scientists) 
print tuple_of_scientists


