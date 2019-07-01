def file_lengthy(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            if 'nttrbsvpa' in l:
                break
    return i - 1