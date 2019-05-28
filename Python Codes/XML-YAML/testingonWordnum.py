from num2words import num2words
from word2number import w2n
def test(z):
    try:
        return(w2n.word_to_num(z))
    except:
        for i in range(z):
            print(w2n.word_to_num(i))


test('onetwo')