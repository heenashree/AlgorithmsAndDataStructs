import os
directory = '../A/B/'
for l in os.listdir(directory):
    if (os.path.isdir(directory + l)):
        print("Yep, it is directory")
