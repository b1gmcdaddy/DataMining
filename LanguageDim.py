import pandas as pd

# language mappingz
language_mapping = {
    'en': 'English', 'es': 'Spanish', 'ko': 'Korean', 'ja': 'Japanese', 'de': 'German',
    'fr': 'French', 'tr': 'Turkish', 'pt': 'Portuguese', 'da': 'Danish', 'ca': 'Catalan',
    'sv': 'Swedish', 'no': 'Norwegian', 'th': 'Thai', 'it': 'Italian', 'zh': 'Chinese',
    'ar': 'Arabic', 'ru': 'Russian', 'is': 'Icelandic', 'tl': 'Tagalog', 'he': 'Hebrew',
    'pl': 'Polish', 'nl': 'Dutch', 'hi': 'Hindi', 'fi': 'Finnish', 'lb': 'Luxembourgish',
    'cy': 'Welsh', 'gl': 'Galician', 'uk': 'Ukrainian', 'hu': 'Hungarian', 'cs': 'Czech',
    'la': 'Latin', 'ro': 'Romanian', 'cn': 'Chinese', 'bg': 'Bulgarian', 'el': 'Greek',
    'vi': 'Vietnamese', 'ta': 'Tamil', 'sr': 'Serbian', 'hr': 'Croatian', 'fa': 'Farsi',
    'zu': 'Zulu', 'xx': 'Unknown', 'bn': 'Bengali', 'id': 'Indonesian', 'ms': 'Malay',
    'sk': 'Slovak', 'ur': 'Urdu', 'te': 'Telugu', 'sh': 'Serbo-Croatian', 'af': 'Afrikaans',
    'kn': 'Kannada', 'si': 'Sinhala', 'bs': 'Bosnian', 'ga': 'Irish', 'et': 'Estonian',
    'ab': 'Abkhazian', 'am': 'Amharic', 'ka': 'Georgian', 'nb': 'Norwegian Bokmål',
    'sq': 'Albanian', 'az': 'Azerbaijani', 'ku': 'Kurdish', 'ml': 'Malayalam',
    'lt': 'Lithuanian', 'mo': 'Moldavian', 'eu': 'Basque', 'mr': 'Marathi',
    'sl': 'Slovenian', 'lv': 'Latvian', 'ne': 'Nepali', 'as': 'Assamese', 'mn': 'Mongolian',
    'be': 'Belarusian', 'se': 'Northern Sami', 'gu': 'Gujarati', 'mk': 'Macedonian',
    'pa': 'Punjabi', 'mt': 'Maltese', 'jv': 'Javanese', 'or': 'Oriya', 'st': 'Southern Sotho',
    'sw': 'Swahili', 'so': 'Somali'
}

data = pd.read_csv(r'C:\Users\JOLO\Desktop\newcleaned.csv')

unique_languages = data['original_language'].unique()

language_dimension = pd.DataFrame({'original_language': unique_languages})
language_dimension['language_id'] = range(3000, 3000 + len(language_dimension))
language_dimension['original_languageName'] = language_dimension['original_language'].map(language_mapping)
language_dimension['spoken_languages'] = data['spoken_languages'].str.replace(',', '-').str.replace(' ', '')

language_dimension = language_dimension[['language_id', 'original_language', 'original_languageName', 'spoken_languages']]
language_dimension.to_csv(r'C:\Users\JOLO\Desktop\Dim_Language.txt', sep=',', index=False)
