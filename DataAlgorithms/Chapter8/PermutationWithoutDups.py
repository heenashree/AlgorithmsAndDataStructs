def getPerms2(string):
    result = []
    getPerms2Inner(" ", string, result)
    return result

def getPerms2Inner(prefix, remainder, result):

    if len(remainder) == 0:
        result.append(prefix)
    length = len(remainder)
    for i in range(length):
        before = remainder[:i]
        after = remainder[i+1:]
        c = remainder[i]
        getPerms2Inner(prefix + c, before + after, result)
print(set(getPerms2("sep")))
