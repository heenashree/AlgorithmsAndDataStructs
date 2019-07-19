#Method 1
from collections import Counter

d = {'hello': 1, 'python': 5, 'world': 3}
c = Counter(d)
print(c.most_common())

##>> [('python', 5), ('world', 3), ('hello', 1)]

#Method 2 by key, by value, descending or ascending
print(sorted(d.items(), key=lambda x: x[1]))
print(sorted(d.items(), key=lambda x: x[0]))

print(sorted(d.items(), key=lambda x: x[1], reverse=True))

#Method 3
import collections
sorted_dict = collections.OrderedDict(d)

#Method 4

data = [
    {
        "name" : "kevin",
        "age":23
    },
    {
        "name": "cole",
        "age":30
    }
]
data.sort(key = lambda p:p['age'])
print(data)
