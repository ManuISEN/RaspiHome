#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import requests
import time
from snipsTools import SnipsConfigParser
from hermes_python.hermes import Hermes
from hermes_python.ontology import *
import io
import os

CONFIG_INI = "config.ini"

# If this skill is supposed to run on the satellite,
# please get this mqtt connection info from <config.ini>
# Hint: MQTT server is always running on the master device
MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

# REMOTE_ADDR = 'http://hd1.freebox.fr/pub/remote_control?code='


class Telecommande(object):
    """Class used to wrap action code with mqtt connection
        Please change the name refering to your application
    """

    def __init__(self):
        # get the configuration if needed
        try:
            self.config = SnipsConfigParser.read_configuration_file(CONFIG_INI)
        except :
            self.config = None

        # start listening to MQTT
        self.start_blocking()

    #def playPause(self,FREEREMOTECODE):
    #    time.sleep(1)
    #    requests.get(REMOTE_ADDR+FREEREMOTECODE+'&key=play')


    def askCommand_callback(self, hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")

        commandeTv = None

        commandeTv = intent_message.slots.TvCommand.first().value

        if commandeTv is None:
            telecommande_msg = "Je ne comprend pas ce que vous me demandez"


        # FREEREMOTECODE = self.config.get("secret").get("freeremotecode")

        if commandeTv == 'power':
            # self.powerFreebox(FREEREMOTECODE)
			os.system('irsend SEND_ONCE tv KEY_POWER')
			
		""" NOT IMPLEMENTED YET
        elif commandeTv == 'pip':
            self.pip(FREEREMOTECODE)
        elif commandeTv == 'switchpip':
            self.switchPip(FREEREMOTECODE)
        elif commandeTv == 'stopip':
            self.stopPip(FREEREMOTECODE)
        elif commandeTv == 'direct':
            self.direct(FREEREMOTECODE)
        elif commandeTv == 'rewind':
            self.rewind(FREEREMOTECODE)
        elif commandeTv == 'forward':
            self.forward(FREEREMOTECODE)
        elif (commandeTv == 'play') or (commandeTv == 'pause'):
            self.playPause(FREEREMOTECODE)
        elif (commandeTv == 'mute') or (commandeTv =='unmute'):
            self.muteUnmute(FREEREMOTECODE)
        elif commandeTv == 'volDown':
            self.volDown(FREEREMOTECODE)
        elif commandeTv == 'volup':
            self.volUp(FREEREMOTECODE)
		"""
		
        elif commandeTv == 'television' :
            # self.television(FREEREMOTECODE)
			os.system('irsend SEND_ONCE tv KEY_POWER')
			
		""" NOT IMPLEMENTED YET
        elif commandeTv=='twitch':
            self.twitch(FREEREMOTECODE)
        elif commandeTv == 'sortprogrammetv' :
            self.exitProgTv(FREEREMOTECODE)
        elif commandeTv == 'programmetv':
            self.progTv(FREEREMOTECODE)
        else :
            self.channelChange(commandeTv,FREEREMOTECODE)
		"""

    """ NOT IMPLEMENTED YET
	def playPause(self,FREEREMOTECODE):
        time.sleep(1)
        requests.get(REMOTE_ADDR+FREEREMOTECODE+'&key=play')
	"""
	
    # def powerFreebox(self, FREEREMOTECODE):
	def powerTv(self):
	# def powerTv(self, KEY_POWER): ???
        time.sleep(1)
        # requests.get(REMOTE_ADDR+FREEREMOTECODE+'&key=power')
		os.system('irsend SEND_ONCE tv KEY_POWER')

	""" NOT IMPLEMENTED YET
    def switchPip(self,FREEREMOTECODE):
        time.sleep(1)
        requests.get(REMOTE_ADDR+FREEREMOTECODE+'&key=red')


    def stopPip(self,FREEREMOTECODE):
        time.sleep(1)
        requests.get(REMOTE_ADDR+FREEREMOTECODE+'&key=green')
        requests.get(REMOTE_ADDR+FREEREMOTECODE+'&key=ok')

    def pip(self,FREEREMOTECODE):
        time.sleep(1)
        requests.get(REMOTE_ADDR+FREEREMOTECODE+'&key=yellow')
        time.sleep(1)
        requests.get(REMOTE_ADDR+FREEREMOTECODE+'&key=yellow')
        time.sleep(1)
        requests.get(REMOTE_ADDR+FREEREMOTECODE+'&key=right')
        time.sleep(1)
        requests.get(REMOTE_ADDR+FREEREMOTECODE+'&key=ok')
        time.sleep(1)
        requests.get(REMOTE_ADDR+FREEREMOTECODE+'&key=red')

    def direct(self,FREEREMOTECODE):
        time.sleep(1)
        requests.get(REMOTE_ADDR+FREEREMOTECODE+'&key=green')
        requests.get(REMOTE_ADDR+FREEREMOTECODE+'&key=ok')

    def rewind(self,FREEREMOTECODE):
        time.sleep(1)
        requests.get(REMOTE_ADDR+FREEREMOTECODE+'&key=bwd&long=true')
        time.sleep(1)
        requests.get(REMOTE_ADDR+FREEREMOTECODE+'&key=bwd&long=true')
        time.sleep(1)
        requests.get(REMOTE_ADDR+FREEREMOTECODE+'&key=bwd&long=true')
        time.sleep(1)
        requests.get(REMOTE_ADDR+FREEREMOTECODE+'&key=bwd&long=true')
        time.sleep(1)

    def forward(self,FREEREMOTECODE):
        time.sleep(1)
        requests.get(REMOTE_ADDR+FREEREMOTECODE+'&key=fwd&long=true')
        time.sleep(1)
        requests.get(REMOTE_ADDR+FREEREMOTECODE+'&key=fwd&long=true')
        time.sleep(1)
        requests.get(REMOTE_ADDR+FREEREMOTECODE+'&key=fwd&long=true')
        time.sleep(1)

    def playPause(self,FREEREMOTECODE):
        time.sleep(1)
        requests.get(REMOTE_ADDR+FREEREMOTECODE+'&key=play')

    def muteUnmute(self,FREEREMOTECODE):
        time.sleep(1)
        requests.get(REMOTE_ADDR+FREEREMOTECODE+'&key=mute')

    def volDown(self,FREEREMOTECODE):
        time.sleep(1)
        requests.get(REMOTE_ADDR+FREEREMOTECODE+'&key=vol_dec&long=true')

    def volUp(self,FREEREMOTECODE):
        time.sleep(1)
        requests.get(REMOTE_ADDR+FREEREMOTECODE+'&key=vol_inc&long=true')

    def television(self,FREEREMOTECODE):
        time.sleep(1)
        requests.get(REMOTE_ADDR+FREEREMOTECODE+'&key=home')
        time.sleep(1)
        requests.get(REMOTE_ADDR+FREEREMOTECODE+'&key=home')
        time.sleep(1)
        requests.get(REMOTE_ADDR+FREEREMOTECODE+'&key=ok')

    def exitProgTv(self,FREEREMOTECODE):
        time.sleep(1)
        requests.get(REMOTE_ADDR+FREEREMOTECODE+'&key=red')

    def progTv(self,FREEREMOTECODE):
        time.sleep(1)
        requests.get(REMOTE_ADDR+FREEREMOTECODE+'&key=home')
        time.sleep(1)
        requests.get(REMOTE_ADDR+FREEREMOTECODE+'&key=home')
        time.sleep(2)
        requests.get(REMOTE_ADDR+FREEREMOTECODE+'&key=ok')
        time.sleep(6)
        requests.get(REMOTE_ADDR+FREEREMOTECODE+'&key=green')
        time.sleep(1)
        requests.get(REMOTE_ADDR+FREEREMOTECODE+'&key=down')
        time.sleep(1)
        requests.get(REMOTE_ADDR+FREEREMOTECODE+'&key=ok')
        time.sleep(1)
        requests.get(REMOTE_ADDR+FREEREMOTECODE+'&key=ok')
        time.sleep(1)

    def twitch(selft,FREEREMOTECODE):
        time.sleep(1)
        requests.get(REMOTE_ADDR+FREEREMOTECODE+'&key=home')
        time.sleep(1)
        requests.get(REMOTE_ADDR+FREEREMOTECODE+'&key=home')
        time.sleep(3)
        requests.get(REMOTE_ADDR+FREEREMOTECODE+'&key=left')
        requests.get(REMOTE_ADDR+FREEREMOTECODE+'&key=left')
        requests.get(REMOTE_ADDR+FREEREMOTECODE+'&key=up')
        requests.get(REMOTE_ADDR+FREEREMOTECODE+'&key=up')
        requests.get(REMOTE_ADDR+FREEREMOTECODE+'&key=ok')
        time.sleep(4)
        requests.get(REMOTE_ADDR+FREEREMOTECODE+'&key=down')
        requests.get(REMOTE_ADDR+FREEREMOTECODE+'&key=down')
        requests.get(REMOTE_ADDR+FREEREMOTECODE+'&key=down')
        requests.get(REMOTE_ADDR+FREEREMOTECODE+'&key=down')


    def channelChange(self,commandeTv,FREEREMOTECODE):
        time.sleep(1)
        for digit in commandeTv:
            requests.get(REMOTE_ADDR+FREEREMOTECODE+'&key='+digit)
	"""
	
    # --> Master callback function, triggered everytime an intent is recognized
    def telecommandeTv_callback(self,hermes, intent_message):
        coming_intent = intent_message.intent.intent_name

        if coming_intent == 'emmto:Televiseur':
            self.askCommand_callback(hermes, intent_message)
        # more callback and if condition goes here...

    # --> Register callback function and start MQTT
    def start_blocking(self):
        with Hermes(MQTT_ADDR) as h:
            h.subscribe_intents(self.telecommandeTv_callback).start()

if __name__ == "__main__":
    Telecommande()
