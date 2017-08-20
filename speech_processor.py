import nltk
import tts_amazonpolly

conversation = False

def process_speech(inputspeech):
    processedspeech = inputspeech + " - Speech Processed"
    tokens = nltk.word_tokenize(inputspeech)
    print (tokens)
    if "shopping" in tokens:
        print ("Enable shopping speech sequence")
    tagged = nltk.pos_tag(tokens)
    print (tagged[0:6])
    entities = nltk.chunk.ne_chunk(tagged)
    print (entities)
    return processedspeech

def interpret_input(inputspeech):
    wordtokens = nltk.word_tokenize(inputspeech)
    print (wordtokens)

    if "shopping" in wordtokens:
        print ("Enable shopping speech sequence")

def speak_response(inputspeech):
    tts_amazonpolly.convert_text_to_speach(inputspeech)
    return

