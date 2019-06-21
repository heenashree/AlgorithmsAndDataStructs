
# finally block always runs, even after encountering return
#Because finally statements are guaranteed to be executed (well, presuming no power outage or anything outside of Python's control). This means that before the function can return, it must run the finally block, which returns a different value.

#The Python docs state:

#When a return, break or continue statement is executed in the try suite of a try...finally statement, the finally clause is also executed ‘on the way out.’ A continue statement is illegal in the finally clause. (The reason is a problem with the current implementation — this restriction may be lifted in the future).
#This means that when you try to return, the finally block is called, returning it's value, rather than the one that you would have had.
def f():
    try:
        print "a"
        return
    except:
        print "b"
    else:
        print "c"
    finally:
        print "d"

f()