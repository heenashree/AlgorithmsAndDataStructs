
def test(list1, k):
    list2=[]
    for i in list1:
        for j in list1:
            if i+j == k:
                list2.append((i,j))
    print(list2)
    print (set(list2))



if __name__ == "__main__":
    listofNumbers = [1,2,3,4,5,5,6,7,2,8,9]
    k = 10
    duplicate = test(listofNumbers, k)

    print("dub", duplicate)