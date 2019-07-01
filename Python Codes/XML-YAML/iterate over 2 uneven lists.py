import os, itertools
dir_=[]
runID= 'abc'
oracleSID = 'NTTPOC3'
directory = '../A/B/'
for l in os.listdir(directory):
    if (os.path.isdir(directory + l)):
        dir_.append('B/' + l)
        print(dir_)
    print("dir", dir)
hosts = ['h1', 'h2', 'h3']
for x, y in zip(dir_, itertools.cycle(hosts)):
    extra_vars = 'runId=' + str(runID) + ' ' + 'profile=' + x + ' ' + 'host=' + y + ' ' + 'oracleSid=' + str(
        oracleSID)
    print("Extra vars for runCDG--> ", extra_vars)
    print("\n***Invoking ansible script to run***\n")