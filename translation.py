
import injector
from googletrans import Translator

translator = Translator()


def translate(wordto_translate):
    translated = []
    translated_word_Hebrew = translator.translate(wordto_translate,dest='iw',src='auto')
    translated_word_Englilsh = translator.translate(wordto_translate,dest='en',src='auto')
    translated_word_Russian= translator.translate(wordto_translate,dest='ru',src='auto')
    translated = [translated_word_Hebrew.text,translated_word_Russian.text,translated_word_Englilsh.text]
    return translated

def detect_language(word):
    detect = translator.detect(word)
    return detect
#list = translate(frontEnd.text_translate)
#print(list)
