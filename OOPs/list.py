def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(10)
#print "list1 = %s" % list1
list2 = extendList(123,[])
#print "list1 = %s" % list2
list3 = extendList('a')
#print "list1 = %s" % list3

print "list1 = %s" % list1
print "list2 = %s" % list2
print "list3 = %s" % list3