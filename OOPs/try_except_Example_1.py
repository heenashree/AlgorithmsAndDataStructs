try:
    print a
except:
    print "b"
else: #runs when exception is not called, if there is exception else will not run
    print "c"
finally:
    print "d"