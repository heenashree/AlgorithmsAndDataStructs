try:
    print "a"
    raise Exception() #Exception is raised using the raised keyword. This will call except
except:
    print "b"
else:
    print "c"
finally:
    print "d"