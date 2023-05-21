import re

simplifications1 = [
    ['E', 'a'],
    ['L', 'l'],
    ['S', 's'],
    ['z', 'j'],
    ['Z', 'g'],
    ['\\^', 'K'],
    ['ƒ', 'n'],
    ['&', 'P'],
]

simplifications2 = [
    ['H', 'h'],
    ['R', 'r'],
    ['®', 'r'],
    ['Í', 'v'],
    ['œ', 'q'],
    ['ç', 'c'],
    ['†', 't'],
    ['˜', 'n'],
    ['´', 'X'],
    ['Î', 'X'],
    ['ì', 'X'],
    ['í', 'X'],
]

def mainLetters(words='', simplify=False, simplifyConsonants=False):
    if words == '' or not isinstance(words, str):
        return words

    newWords = words

    if simplify:
        for e in simplifications1:
            newWords = re.sub(e[0], e[1], newWords)

    if simplifyConsonants:
        for e in simplifications2:
            newWords = re.sub(e[0], e[1], newWords)
    else:
        newWords = re.sub('[HR]', '', newWords)

    newWords = re.sub('[^A-Za-z ]', '', newWords)
    newWords = re.sub('[uUiIyYwWoOMN]', '', newWords)
    newWords = re.sub('[ \s]+', ' ', newWords)
    newWords = newWords.strip()

    return newWords

