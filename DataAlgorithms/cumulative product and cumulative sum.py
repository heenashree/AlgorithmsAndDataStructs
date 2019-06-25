#>>> cumulative_sum([1, 2, 3, 4])
#[1, 3, 6, 10]
#>>> cumulative_sum([4, 3, 2, 1])
#[4, 7, 9, 10]

def cumulative_sum(arr):
    i = 0
    k = []
    try:
        k.append(arr[0])
        for i in range(len(arr)):
            i = arr[i] + arr[i+1]
            k.append(i)

    except IndexError as e:
        pass
    print(k)

cumulative_sum([1, 3, 6, 10])

#same goes for multiplcation