'''
Find position of an element in a sorted array of infinite numbers
Suppose you have a sorted array of infinite numbers, how would you search an element in the array?

Source: Amazon Interview Experience.
Since array is sorted, the first thing clicks into mind is binary search, but the problem here is that we don’t know size of array.
If the array is infinite, that means we don’t have proper bounds to apply binary search. So in order to find position of key, first we find bounds and then apply binary search algorithm.

Let low be pointing to 1st element and high pointing to 2nd element of array, Now compare key with high index element,
->if it is greater than high index element then copy high index in low index and double the high index.
->if it is smaller, then apply binary search on high and low indices found.
'''

'''
def elementAt(x, Listy, i=0, j=0):
    #Returns the index of element at i index
    #Listy is sorted
    print("j", j)

    try:
        low = Listy[i]
        print("low", low)
        high = Listy[j]
        print("hight", high)
        print("x", x)
        if x == high:
            print("ok", j)
            return j
        elif x > high:
            j = j+1
            low = high
            high = Listy[j+1]
            print("now high", high)
            elementAt(x, Listy,i, j)
        else:
            #low is the high index over ehere and you can aplpy binary search.
            print(BinarySearch(Listy,x, i,j))


    except IndexError:
        return -1

def BinarySearch(Listy,x, i,j):

    while j <= i:

        mid = len[Listy]//2
        if Listy[mid] == x:
            return mid
        elif Listy[mid]<x:
            i = mid+1
        else:
            j = mid -1
    return -1

if __name__=="__main__":
    x = 1
    Listy=[10,11,12,13,14] #List is sorted
    k = elementAt(x, Listy, i=0, j=0)
    print(k)

'''