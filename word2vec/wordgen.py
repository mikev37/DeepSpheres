import random
import string
vowels = list('eeeeeeeeeeeeaaaaaaaaiiiiiiiooooooouuu')
consonants = list('tttttttttnnnnnnnssssssrrrrrrhhhhhhddddllllcccmmmffyywwggppbbvvkkxqjz')
#vowels = list('aeiou')

def gen_word(min, max):
    word = ''
    syllables = min + int(random.random() * (max - min))
    for i in range(0, syllables):
        word += gen_syllable()
    
    return word.capitalize()


def gen_syllable():
    ran = random.random()
    if ran < 0.333:
        return word_part('v') + word_part('c')
    if ran < 0.666:
        return word_part('c') + word_part('v')
    return word_part('c') + word_part('v') + word_part('c')


def word_part(type):
    if type is 'c':
        return random.sample(consonants,1)[0]#[ch for ch in list(string.lowercase) if ch not in vowels], 1)[0]
    if type is 'v':
        return random.sample(vowels, 1)[0]


'''
for i in range(0, 10):
    print gen_word(2,4)
'''