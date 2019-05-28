

def largeAndSmall(x):
    return (max(x), min (x))
if __name__ == "__main__":
    listofNumbers = [1,2,3,4,5,5,6,7,2,8,9]
    mini, maxi = largeAndSmall(listofNumbers)
    print("dub", mini, maxi)