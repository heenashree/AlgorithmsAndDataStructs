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

print demo1()

print demo2()

