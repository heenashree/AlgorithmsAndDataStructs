
def dupNumber(x):
    list2=[]
    for i in range(len(x)):
        k = i + 1
        for j in range(k, len(x)):
            if x[i] == x[j] and x[i] not in list2:
                list2.append(x[i])
    return list2


if __name__ == "__main__":
    listofNumbers = [1,2,3,4,5,5,6,7,2,8,9]
    duplicate = dupNumber(listofNumbers)
    print("dub", duplicate)































