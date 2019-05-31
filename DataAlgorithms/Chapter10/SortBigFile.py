'''
filename= '20GBfile.txt'
with open(filename, 'r') as f:
    data = f.read()
    data = list((data.split( )))
    print(sorted(data))
'''
#External sort, chunk file, sort them and merge to big file