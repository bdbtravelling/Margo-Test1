import nltk
import tts_amazonpolly
from datetime import datetime
import time

conversation = False

def process_speech(inputspeech):
    processedspeech = inputspeech + " - Speech Processed"
    tokens = nltk.word_tokenize(inputspeech)
    print (tokens)
    tagged = nltk.pos_tag(tokens)
    print (tagged[0:6])
    entities = nltk.chunk.ne_chunk(tagged)
    print (entities)
    return processedspeech

"""def interpret_input(inputspeech):
    wordtokens = nltk.word_tokenize(inputspeech)
    print (wordtokens)
    if "shopping" in wordtokens:
        print ("Enable shopping speech sequence")"""

def check_for_wake_signal():
    listentext = raw_input("Enter Wake Signal (Hi Margo, Margo): ")
    listentexttokens = nltk.word_tokenize(listentext)
    print (listentexttokens)
    if "Margo" in listentexttokens:
        return True
    else:
        return False

def check_for_speech():
    listentext = raw_input("Enter speech: ")
    listentexttokens = nltk.word_tokenize(listentext)
    print (listentexttokens)
    return listentexttokens

def margo_greeting():
    """thetime = str(datetime.now().time())"""
    hour = time.strftime("%H")
    print (hour)
    """print (thetime)"""
    speak_response("Hi!  How can I help?")
    return

def speak_response(inputspeech):
    tts_amazonpolly.convert_text_to_speach(inputspeech)
    return

