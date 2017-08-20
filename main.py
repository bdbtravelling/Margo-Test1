""" Main program loop """

import init
import speech_processor

""" Initial Setup """
margoinitstatus = init.margo_initialisation()
print ("Margo initialised: " + margoinitstatus)

""" Choose operating mode """
""" operatingmode = init.choose_mode() """

""" Variable setup"""
conversation = False

""" Enter Program State Machine """
while True:
    if conversation:
        receivedspeech = speech_processor.check_for_speech()
        if "shopping" in receivedspeech:
            speech_processor.speak_response("Ok, let's talk about shopping")
        elif "reminder" in receivedspeech:
            speech_processor.speak_response("Ok, let's check your reminders")
        elif "company" in receivedspeech:
            speech_processor.speak_response("Ok, I've got some ideas about that")
        else:
            speech_processor.speak_response("Sorry, I'm not sure what you mean")
            conversation = False
    else:
        wakestatus = speech_processor.check_for_wake_signal()
    if wakestatus:
        """ Margo Wake - start dialogue"""
        speech_processor.margo_greeting()
        conversation = True
        wakestatus = False

"""    if operatingmode == "1":
        inputspeech = raw_input("Enter speech to process: ")
        if inputspeech == "Exit":
            break
        interpret = speech_processor.process_speech(inputspeech)
        print ("Speech Interpretted: " + interpret)
    elif operatingmode == "2":
        inputspeech = raw_input("Enter text to speak: ")
        if inputspeech == "Exit":
            break
        speech_processor.speak_response(inputspeech)
    else:
        break"""

print ("Program ending")