import os
import speech_recognition as sr

lirc_file_conf = '~/lircd.conf'
power_button_command = 'KEY_POWER'

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

TURN_TV_ON = "turn tv on"
TURN_TV_OFF = "turn tv off"

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
            command = r.recognize(audio)
            print("Detected speech:{0}".format(command))
            # Check the current command
            if TURN_TV_ON in command.lower():
                # Get tv device and turn it on
                # tv = cec.Device(0) # to be changed in order to send IR ON command to the TV
                # tv.power_on()
                os.system('irsend SEND_ONCE {} {}'.format(lirc_file_conf, power_button_command))
                print("TV ON")
            elif TURN_TV_OFF in command.lower():
                # Get tv device and turn it off
                # tv = cec.Device(0) # to be changed in order to send IR OFF commande to the TV
                # tv.standby()
                os.system('irsend SEND_ONCE {} {}'.format(lirc_file_conf, power_button_command))
                print("TV OFF")
        except LookupError:
            # In case of an exception
            print("Could not translate audio")

if __name__ == '__main__':
    main()
