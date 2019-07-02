import itertools
listy_start = [1,2,3]
listy_end = [4,5]

for (start, end) in itertools.izip_longest(listy_start, listy_end):
    print start, end

"""Output
1 4
2 5
3 None
"""