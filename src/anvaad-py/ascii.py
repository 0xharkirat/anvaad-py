import string

def pad_start(string, target_length, pad_char=' '):
    return pad_char * (target_length - len(string)) + string

def ascii(string=''):
    if string == '' or not isinstance(string, str):
        return string
    
    return ',' + ','.join(pad_start(str(ord(char)), 3, '0') for char in string) + ','

