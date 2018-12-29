"""What are Sets?"""

# Sets are lists with no duplicate entries. For example, if we were to print out a set:
# >>> a = set(["Jake", "Jake", "John", "Eric"])
# >>> print a
# It would print out:
#     set(['Jake', 'John', 'Eric']).
# You can also write a set like:
# >>> a = {1, 1, 5, 2, 3}


"""Methods:"""

# There are various methods that work with sets:
# In [4]: a.
#     a.add                          a.issubset
#     a.clear                        a.issuperset
#     a.copy                         a.pop
#     a.difference                   a.remove
#     a.difference_update            a.symmetric_difference
#     a.discard                      a.symmetric_difference_update
#     a.intersection                 a.union
#     a.intersection_update          a.update
#     a.isdisjoint

#To find out which members attended both events, you may use the "intersection" method:
>>> a = {1, 2, 3, 5}
>>> b = {3, 5, 6, 7}
>>> print(a.intersection(b))
{3}

#To find out which members attended only one of the events, use the "symetric_difference" method:
>>> a = {"Jake", "John", "Eric"}
>>> b = {"John", "Jill"}
>>> print(a.symmetric_difference(b))
{'Jake', 'Jill', 'Eric'}
#This just takes out the word that is common in both sets

#To find out which members attended only one event and not the other, use the "Difference" method:
>>> a = set(["Jake", "John", "Eric"])
>>> b = set(["John", "Jill"])
>>> print(a.difference(b))
>>> print(b.difference(a))
{'Jake', 'Eric'}
{'Jill'}

#To recieve a list of all the participants, use the "union" method:
>>> a = set(["Jake", "John", "Eric"])
>>> b = set(["John", "Jill"])
>>> print(a.union(b))
{'Jake', 'Jill', 'John', 'Eric'}














