"""tests = [
    ['last', 'lest', 'list', 'lost', 'lust'],
    ['beryl', 'jigsawed', 'oospheres', 'troweller', 'volcanizes'],
    ['blackcaps', 'blackguard', 'blacks', 'blague', 'blancmange',
     'blander', 'blastular', 'blawort', 'blender', 'blimbing',
     'blinder', 'blistered', 'blocks', 'blonde', 'blonder',
     'blotchier', 'blowlamp', 'blue', 'bluejays', 'blunder'],
]

solutions = [
    [['last', 'lest', 'list', 'lost', 'lust']],
    [],
    [['blander', 'blender', 'blinder', 'blonder', 'blunder']]
]

"""
# Exclude 'y' from vowels since it can't make up its mind if it's a vowel
tests = [
    ['last', 'lest', 'list', 'lost', 'lust'],
    ['beryl', 'jigsawed', 'oospheres', 'troweller', 'volcanizes'],
    ['blackcaps', 'blackguard', 'blacks', 'blague', 'blancmange',
     'blander', 'blastular', 'blawort', 'blender', 'blimbing',
     'blinder', 'blistered', 'blocks', 'blonde', 'blonder',
     'blotchier', 'blowlamp', 'blue', 'bluejays', 'blunder'],
]
vowels = 'aeiou'

def find_solutions(words):
    """Searches for solutions to the game returning a list of all solutions."""
    from collections import Counter
    import re
    regex = r"([bcdfghjklmnpqrstvwxz]*[aeiou]+[bcdfghjklmnpqrstvwxz]*)"
    #if re.search(regex, phoneNumber):
    #    match = re.search(regex, phoneNumber)


    solutions = []
    mdict={}
    rev_multidict = {}

    for i in words:
        for sublist in i:
            mdict[sublist] = len(sublist)
        for key, value in mdict.items():
            rev_multidict.setdefault(value, set()).add(key)

    for key,value in rev_multidict.items():
        i = rev_multidict[key]






    #return solutions

find_solutions(tests)
