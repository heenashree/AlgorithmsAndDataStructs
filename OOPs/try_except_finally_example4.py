#Because finally statements are guaranteed to be executed.
# This means that before the function can return, it must run the finally block, which returns a different value.

#The Python docs state:

#When a return, break or continue statement is executed in the try suite of a try...finally statement,
# the finally clause is also executed ‘on the way out.’
# A continue statement is illegal in the finally clause.
# (The reason is a problem with the current implementation — this restriction may be lifted in the future).

#This means that when you try to return, the finally block is called,
# returning it's value, rather than the one that you would have had.
#The execution order is:

#try block all completes normally -> finally block -> function ends
##try block run and get into exception A -> finally block -> function ends
#try block make a return value and call return -> finally block -> popup return value -> function ends


#So, any return in the finally block will end the steps in advance.


def demo1():
    try:
        raise RuntimeError,"To Force Issue"
    except:
        return 1
    else:
        return 2
    finally:

        return 3


def demo2():
    try:
        try:
            raise RuntimeError,"To Force Issue"
        except:
            return 1
        else:
            return 2
        finally:
            return 3
    except:
        print 4
    else:
        print 5
    finally:
        print 6


def demo3():
    try:
        x = 2/0
    except:
        print("exception")
        exit()
    finally:
        print("final statement")

print demo1()

print demo2()
demo3()

