sol1=[]
def min_unfairness(word_list,k):
    tadatu=[]
    arr = sorted(word_list)
    print(arr)
    import itertools
    tada = set(itertools.combinations(arr, k))
    for i in tada:
        tadatu.append((max(i)-min(i)))
        print(tadatu)
    return min(tadatu)


min_unfairness([1,1,-1],2)
