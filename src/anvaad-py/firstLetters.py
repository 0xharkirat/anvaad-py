import re



simplifications = [
    ['E', 'a'],
    ['ਓ', 'ੳ'],
    ['L', 'l'],
    ['ਲ਼', 'ਲ'],
    ['S', 's'],
    ['ਸ਼', 'ਸ'],
    ['z', 'j'],
    ['ਜ਼', 'ਜ'],
    ['Z', 'g'],
    ['ਗ਼', 'ਗ'],
    ['\\^', 'K'],
    ['ਖ਼', 'ਖ'],
    ['ƒ', 'n'],
    ['ਨੂੰ', 'ਨ'],
    ['&', 'P'],
    ['ਫ਼', 'ਫ'],
]

def first_letters(words='', eng=False, simplify=False):
    if words == '' or not isinstance(words, str):
        return words
    
    new_words = words
    
    if simplify:
        for e in simplifications:
            new_words = re.sub(e[0], e[1], new_words)
    
    new_words = re.sub(r'\]', '', new_words)
    new_words = re.sub(r'\[', '', new_words)
    new_words = re.sub(r'॥', '', new_words)
    new_words = re.sub(r'।', '', new_words)
    new_words = re.sub(r'rhwau dUjw', '', new_words)
    new_words = re.sub(r'rhwau', '', new_words)
    new_words = re.sub(r'[0-9]', '', new_words)
    new_words = re.sub(r'[;,.]', '', new_words)
    
    def first_letter(word):
        if word:
            if word[0] == 'i' and not eng:
                return word[1]
            return word[0]
        return ''
    
    letters = ''.join(first_letter(word) for word in new_words.split(' '))
    
    if not eng:
        letters = letters.replace('|', '')
    
    return letters
