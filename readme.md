# anvaad-py :: ਅਨੁਵਾਦ-ਪੀਵਾਏ 

This is python version of [anvaad-js](https://github.com/KhalisFoundation/anvaad-js) 

Hosted on Pypi - [anvaad-py](https://pypi.org/project/anvaad-py/)

## Installation

```bash
# pip
pip install anvaad-py //for windows
pip3 install anvaad-py //for mac
```

## API Documentation

## Usage

```python
from anvaad_py import unicode

result = unicode('ਆਇ ਮਿਲੁ ਗੁਰਸਿਖ ਆਇ ਮਿਲੁ ਤੂ ਮੇਰੇ ਗੁਰੂ ਕੇ ਪਿਆਰੇ ॥', True)

print(result)

// => 'Awie imlu gurisK Awie imlu qU myry gurU ky ipAwry ]'
```

### Table of Contents

-   [ascii](#ascii)
-   [firstLetters](#firstletters)
-   [mainLetters](#mainletters)
-   [unicode](#unicode)

## ascii

Returns a comma-separated string of ascii codes for a
string of Gurmukhi characters

**Parameters**

-   `string` The string of letters

**Examples**

```python
from anvaad_py import ascii

result = ascii('AmgAmqmgkp')

print(result)
// => ',065,109,103,065,109,113,109,103,107,112,'
```

`string` Returns a single string of comma-separated ascii codes


## firstLetters

Retrieve the first letter of each word from a string

**Parameters**

-   `words` **[string](https://developer.mozilla.org/docs/Web/python/Reference/Global_Objects/String)** The string from which to get first letters
-   `eng` **[boolean](https://developer.mozilla.org/docs/Web/python/Reference/Global_Objects/Boolean)** Whether the string is English (optional, default `false`)
-   `simplify` **[boolean](https://developer.mozilla.org/docs/Web/python/Reference/Global_Objects/Boolean)** Whether to simplify embedded vowels and other characters (eg. E to a, ^ to K)

**Examples**

```python
from anvaad_py import firstLetters

result = firstLetters('Awie imlu gurisK Awie imlu qU myry gurU ky ipAwry ]')

print(result)
// => 'AmgAmqmgkp'
```

`string` Returns a single string of characters


## mainLetters

Removes vowel symbols from a Gurmukhi string

**Parameters**

-   `words` **[string](https://developer.mozilla.org/docs/Web/python/Reference/Global_Objects/String)** The string from which to get main letters
-   `simplify` **[boolean](https://developer.mozilla.org/docs/Web/python/Reference/Global_Objects/Boolean)** Whether to simplify embedded vowels/nasal sounds (eg. E to a, ^ to K)
-   `simplifyConsonants` **[boolean](https://developer.mozilla.org/docs/Web/python/Reference/Global_Objects/Boolean)** Whether to simplify half characters to full characters (eg. R to r)

**Examples**

```python
from anvaad_py import mainLetters

result = mainLetters('Awie imlu gurisK Awie imlu qU myry gurU ky ipAwry ]')

print(result)
// => 'Ae ml grsK Ae ml q mr gr k pAr'
```

`string` Returns a single string of characters



## unicode

Convert Gurmukhi script to Unicode and back again.

**Parameters**

-   `text` **[string](https://developer.mozilla.org/docs/Web/python/Reference/Global_Objects/String)** Gurbani Akhar or Unicode script to be converted
-   `reverse` **[boolean](https://developer.mozilla.org/docs/Web/python/Reference/Global_Objects/Boolean)** Whether to convert ASCII to unicode (false by default)
-   `simplify` **[boolean](https://developer.mozilla.org/docs/Web/python/Reference/Global_Objects/Boolean)** Whether to simplify extended characters to single code points (eg. sæ to ਸ਼ (u0A36), ਸ਼ (u0A38u0A3C) to S) (false by default)


**Examples**

```python
from anvaad_py import unicode

gurmukhiResult = unicode('Awie imlu gurisK Awie imlu qU myry gurU ky ipAwry ]')

print(f"gurmukhi results: {gurmukhiResult}")
// => 'gurmukhi results: ਆਇ ਮਿਲੁ ਗੁਰਸਿਖ ਆਇ ਮਿਲੁ ਤੂ ਮੇਰੇ ਗੁਰੂ ਕੇ ਪਿਆਰੇ ॥'
```

Returns **[string](https://developer.mozilla.org/docs/Web/python/Reference/Global_Objects/String)** Returns unicode text

```python
from anvaad_py import unicode

unicodeResult = unicode('ਆਇ ਮਿਲੁ ਗੁਰਸਿਖ ਆਇ ਮਿਲੁ ਤੂ ਮੇਰੇ ਗੁਰੂ ਕੇ ਪਿਆਰੇ ॥', True)

print(f"unicode results: {unicodeResult}")
 * // => 'unicode results: Awie imlu gurisK Awie imlu qU myry gurU ky ipAwry ]'
```

`string` Returns gurbani akhar ascii text


a [0xharkirat](https://github.com/0xharkirat/) (Harkirat Singh) production.
