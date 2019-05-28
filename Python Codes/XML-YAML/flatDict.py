import collections

def flatten(d, parent_key='', sep='/'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    print (dict(items))
    return dict(items)


flatten({
    "name": {
        "first": "One",
        "last": "Drone"
    },
    "job": "scout",
    "recent": {},
    "additional": {
        "place": {
            "zone": "1",
            "cell": "2"
        }
    }
})
"""{
    "name/first": "One",
    "name/last": "Drone",
    "job": "scout",
    "recent": "",
    "additional/place/zone": "1",
    "additional/place/cell": "2"
})"""