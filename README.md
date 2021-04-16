# Image_TextExtractor_and_Translator
Extracts english text from image and Translates it into destination language

This python code is created to extract text from an image and translate the text to desired language.
**Packages Used : **
OpenCV
PyTesserect
goslate 
Google Translate

In the code, goslate is used for translation of the text to required language. 

Py Tesseract is used to extract text from an image.

**Example:**

The image used as input is below

![thriller](https://user-images.githubusercontent.com/82672285/115062367-e6c21a80-9f07-11eb-9488-a0ee5e28c3fd.png)

**Output In French:**

MICHAEL JACKSON

Paroles de thriller

Il est proche de minuit et quelque chose de malade

Dans le noir

Sous le clair de lune, vous voyez un spectacle qui arrête presque
Votre cœur

Vous essayez de crier, mais la terreur prend le son avant
Tu l'as fait

Vous commencez à geler comme horreur vous cherche bien entre vous


**Languages and Language codes**
Out[33]: 
{'af': 'afrikaans',
 'am': 'amharic',
 'ar': 'arabic',
 'az': 'azerbaijani',
 'be': 'belarusian',
 'bg': 'bulgarian',
 'bn': 'bengali',
 'bs': 'bosnian',
 'ca': 'catalan',
 'ceb': 'cebuano',
 'co': 'corsican',
 'cs': 'czech',
 'cy': 'welsh',
 'da': 'danish',
 'de': 'german',
 'el': 'greek',
 'en': 'english',
 'eo': 'esperanto',
 'es': 'spanish',
 'et': 'estonian',
 'eu': 'basque',
 'fa': 'persian',
 'fi': 'finnish',
 'fr': 'french',
 'fy': 'frisian',
 'ga': 'irish',
 'gd': 'scots gaelic',
 'gl': 'galician',
 'gu': 'gujarati',
 'ha': 'hausa',
 'haw': 'hawaiian',
 'he': 'hebrew',
 'hi': 'hindi',
 'hmn': 'hmong',
 'hr': 'croatian',
 'ht': 'haitian creole',
 'hu': 'hungarian',
 'hy': 'armenian',
 'id': 'indonesian',
 'ig': 'igbo',
 'is': 'icelandic',
 'it': 'italian',
 'iw': 'hebrew',
 'ja': 'japanese',
 'jw': 'javanese',
 'ka': 'georgian',
 'kk': 'kazakh',
 'km': 'khmer',
 'kn': 'kannada',
 'ko': 'korean',
 'ku': 'kurdish (kurmanji)',
 'ky': 'kyrgyz',
 'la': 'latin',
 'lb': 'luxembourgish',
 'lo': 'lao',
 'lt': 'lithuanian',
 'lv': 'latvian',
 'mg': 'malagasy',
 'mi': 'maori',
 'mk': 'macedonian',
 'ml': 'malayalam',
 'mn': 'mongolian',
 'mr': 'marathi',
 'ms': 'malay',
 'mt': 'maltese',
 'my': 'myanmar (burmese)',
 'ne': 'nepali',
 'nl': 'dutch',
 'no': 'norwegian',
 'ny': 'chichewa',
 'or': 'odia',
 'pa': 'punjabi',
 'pl': 'polish',
 'ps': 'pashto',
 'pt': 'portuguese',
 'ro': 'romanian',
 'ru': 'russian',
 'sd': 'sindhi',
 'si': 'sinhala',
 'sk': 'slovak',
 'sl': 'slovenian',
 'sm': 'samoan',
 'sn': 'shona',
 'so': 'somali',
 'sq': 'albanian',
 'sr': 'serbian',
 'st': 'sesotho',
 'su': 'sundanese',
 'sv': 'swedish',
 'sw': 'swahili',
 'ta': 'tamil',
 'te': 'telugu',
 'tg': 'tajik',
 'th': 'thai',
 'tl': 'filipino',
 'tr': 'turkish',
 'ug': 'uyghur',
 'uk': 'ukrainian',
 'ur': 'urdu',
 'uz': 'uzbek',
 'vi': 'vietnamese',
 'xh': 'xhosa',
 'yi': 'yiddish',
 'yo': 'yoruba',
 'zh-cn': 'chinese (simplified)',
 'zh-tw': 'chinese (traditional)',
 'zu': 'zulu'}

**Note**:There have been problems reported while using Google Translate. Often, users get "attributeerror 'nonetype' object has no attribute 'group'" error using Google Translate.
