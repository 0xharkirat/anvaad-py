import re

character_map = {
    'a': 'ੳ',
    'A': 'ਅ',
    'e': 'ੲ',
    's': 'ਸ',
    'h': 'ਹ',
    'k': 'ਕ',
    'K': 'ਖ',
    'g': 'ਗ',
    'G': 'ਘ',
    '|': 'ਙ',
    'c': 'ਚ',
    'C': 'ਛ',
    'j': 'ਜ',
    'J': 'ਝ',
    '\\': 'ਞ',
    't': 'ਟ',
    'T': 'ਠ',
    'f': 'ਡ',
    'F': 'ਢ',
    'x': 'ਣ',
    'q': 'ਤ',
    'Q': 'ਥ',
    'd': 'ਦ',
    'D': 'ਧ',
    'n': 'ਨ',
    'p': 'ਪ',
    'P': 'ਫ',
    'b': 'ਬ',
    'B': 'ਭ',
    'm': 'ਮ',
    'X': 'ਯ',
    'r': 'ਰ',
    'l': 'ਲ',
    'v': 'ਵ',
    'V': 'ੜ',
}

matraFixes = [
    ['[ਉ, ਊ]', 'ੳ'],
    ['[ਆ, ਆਂ, ਐ, ਔ]', 'ਅ'],
    ['[ਈ, ਏ]', 'ੲ'],
]

def customSort(firstEl, secondEl):
    if not firstEl:
        return -1
    if not secondEl:
        return 1
    firstIndex = sortedValues.index(firstEl[0])
    secondIndex = sortedValues.index(secondEl[0])
    if firstIndex == secondIndex:
        return customSort(firstEl[1:], secondEl[1:])
    return firstIndex - secondIndex

def getKeyByValue(dictionary, value):
    return next((key for key, val in dictionary.items() if val == value), None)

def alphabetize(sentenceArray, type='english'):
    global sortedValues
    if type == 'unicode':
        sortedValues = list(character_map.values())
    elif type == 'english':
        sortedValues = list(character_map.keys())

    sentenceObj = {}
    for sentence in sentenceArray:
        newSentence = sentence
        for pattern, replacement in matraFixes:
            newSentence = re.sub(pattern, replacement, newSentence)
        arr = [char for char in newSentence if char in sortedValues[1:]]
        sentenceObj[sentence] = ''.join(arr)

    sortedResult = sorted(sentenceObj.values(), key=lambda x: (x[0], customSort(x, x)))

    return [getKeyByValue(sentenceObj, value) for value in sortedResult]

# Test the alphabetize function
unicode_sentences = [
    "ਕੇਤੀਆ ਸੁਰਤੀ ਸੇਵਕ ਕੇਤੇ ਨਾਨਕ ਅੰਤੁ ਨ ਅੰਤੁ ॥੩੫॥",
    "ਤੁਧੁ ਵਿਣੁ ਸਿਧੀ ਕਿਨੈ ਨ ਪਾਈਆ ॥",
    "ਬਿਨੁ ਸਤਿਗੁਰ ਕਿਨੈ ਨ ਪਾਇਓ ਕਰਿ ਵੇਖਹੁ ਮਨਿ ਵੀਚਾਰਿ ॥",
    "ਅੰਤੁ ਨ ਸਿਫਤੀ ਕਹਣਿ ਨ ਅੰਤੁ ॥",
    "ਹਉ ਹਉ ਕਰਤੀ ਸਭ ਮੁਈ ਸੰਪਉ ਕਿਸੈ ਨ ਨਾਲਿ ॥",
]
english_sentences = [
    "kyqIAw surqI syvk kyqy nwnk AMqu n AMqu ]35]",
    "quDu ivxu isDI iknY n pweIAw ]",
    "ibnu siqgur iknY n pwieE kir vyKhu min vIcwir ]",
    "AMqu n isPqI khix n AMqu ]",
    "hau hau krqI sB mueI sMpau iksY n nwil ]",
]
