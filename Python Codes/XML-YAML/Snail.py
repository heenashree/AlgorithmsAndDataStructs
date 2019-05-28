def snail(array):
    k = 0
    list1 = []
    for i in array:
        print("I ki valie", i)
        j = 0
        while j < len(i):
            print("j", j)
            if not array:
                list1.append(i[])

            try:
                list1.append(i[j])
            except IndexError:
                pass
            try:
                i.remove(i[j])
            except IndexError:
                pass

            print("List1", list1)
            print("array", i)




array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
#expected = [1,2,3,6,9,8,7,4,5]
snail(array)


array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
#expected = [1,2,3,4,5,6,7,8,9]
snail(array)