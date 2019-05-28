'''

def URLify(str, length):
    if length <= 13:
        return ('%20'.join(str.split()))

print(URLify("Mr   John Smith    ", 13))
'''

def URLfy(string):
    return string.strip().replace(' ', '%20')

print (URLfy('abab  abab aaaaaa '))
