#Python | Difference between iterable and iterator
#Iterable is an object, which one can iterate over. It generates an Iterator when passed to iter() method. Iterator is an object, which is used to iterate over an iterable object using __next__() method. Iterators have __next__() method, which returns the next item of the object.

#Note that every iterator is also an iterable, but not every iterable is an iterator. For example, a list is iterable but a list is not an iterator. An iterator can be created from an iterable by using the function iter(). To make this possible, the class of an object needs either a method __iter__, which returns an iterator, or a __getitem__ method with sequential indexes starting with 0.

