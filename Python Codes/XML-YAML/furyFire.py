import re


def fire_and_fury(tweet):
    result = []
    if tweet.count('FIRE') == 0 and tweet.count('FURY') == 0 or any((x) not in 'FURYIE' for x in tweet):
        return "Fake tweet."
    tweet = re.findall('FIRE|FURY', tweet)

    i = 0
    while (i < len(tweet)):
        if tweet[i] == 'FIRE':
            count = 0
            while i < len(tweet) and tweet[i] == 'FIRE':
                count += 1
                i += 1
            i -= 1
            result.append('You' + ' and you' * (count - 1) + ' are fired!')

        if tweet[i] == 'FURY':
            count = 0
            while i < len(tweet) and tweet[i] == 'FURY':
                count += 1
                i += 1
            i -= 1
            result.append('I am' + ' really' * (count - 1) + ' furious.')
        i += 1
    return ' '.join(result)