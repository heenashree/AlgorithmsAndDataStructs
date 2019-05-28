def est_subsets(arr):
    count =0
    arr = set(arr)
    import itertools
    for i in range(1,len(arr)+1):
        x = set(itertools.combinations(arr, i))
        count = count + len(x)
    return count