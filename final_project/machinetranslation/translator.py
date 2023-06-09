'''a program to translate en-fr or fr-en'''

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    '''to french'''
    french_text = MyMemoryTranslator(source='en', target='fr').translate(english_text)
    return french_text

def french_to_english(french_text):
    ''' to english '''
    english_text = MyMemoryTranslator(source='french', target='english').translate(french_text)
    return english_text
