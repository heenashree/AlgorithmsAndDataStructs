def getMissingNo(A):
    n = len(A)
    total = (n + 1) * (n + 2) / 2
    print("Total,", total)
    sum_of_A = sum(A)
    print("Sum of A", sum_of_A)
    print("Substract", total-sum_of_A)
    return total - sum_of_A


# Driver program to test above function
A = [1, 2, 4, 5, 6]
miss = getMissingNo(A)
print(miss)
# This code is contributed by Pratik Chhajer