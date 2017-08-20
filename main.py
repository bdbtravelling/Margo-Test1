""" Main program loop """

import init
import speech_processor

""" Initial Setup """
margoinitstatus = init.margo_initialisation()
print ("Margo initialised: " + margoinitstatus)

""" Choose operating mode """
operatingmode = init.choose_mode()

""" Enter Program State Machine """
while True:
    if operatingmode == "1":
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
        break

print ("Programme ending")