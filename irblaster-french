import os
import speech_recognition as sr

# lirc_file_conf = '~/lircd.conf'
# power_button_command = 'KEY_POWER'

###########################################################################################################
# create file ~/.lircrc
#
# begin
#   remote = myRemote
#   prog = myProg
#   button = KEY_POWER
#   config = myVariable
#   repeat = 0
# end
#############################################################################################################

ALLUMER_TV = "allumer tv"
ETEINDRE_TV = "éteindre tv"

def main():
    # Create speech recognizer object
    r = sr.Recognizer()

    # Create infinite loop
    while True:
        # Record sound
        with sr.Microphone() as source:
            print("Recording")
            audio = r.listen(source)

        try:
            # Try to recognize the audio
            command = r.recognize_google(audio, language='fr-FR')
            
            print("Detected speech:{0}".format(command))
            # Check the current command
            if ALLUMER_TV in command.lower():
                # Get tv device and turn it on
                os.system('irsend SEND_ONCE tv KEY_POWER')
                print("TV ON")
            if TURN_TV_OFF in command.lower():
                # Get tv device and turn it off
                os.system('irsend SEND_ONCE tv KEY_POWER')
                print("TV OFF")
        except LookupError:
            # In case of an exception
            print("Could not translate audio")

if __name__ == '__main__':
    main()
