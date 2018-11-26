#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import requests
import time
from snipsTools import SnipsConfigParser
from hermes_python.hermes import Hermes
from hermes_python.ontology import *
import io
import os

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

    def askCommand_callback(self, hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")

		# initialization
        commandeTv = None
		
		# use this way : dummyValue = intent_message.slots.[SLOT_NAME].first().value
        commandeTv = intent_message.slots.TvCommand.first().value

        if commandeTv is None:
            telecommande_msg = "Je ne comprend pas ce que vous me demandez"

        # FREEREMOTECODE = self.config.get("secret").get("freeremotecode")

        if commandeTv == 'power':
			# self.powerTv() ???
			os.system('irsend SEND_ONCE tv KEY_POWER')
			
        elif commandeTv == 'television' :
            # self.television(FREEREMOTECODE)
			# self.powerTv()
			os.system('irsend SEND_ONCE tv KEY_POWER')
			
    # def powerFreebox(self, FREEREMOTECODE):
	def powerTv(self):
	# def powerTv(self, KEY_POWER): ???
        time.sleep(1)
        # requests.get(REMOTE_ADDR+FREEREMOTECODE+'&key=power')
		os.system('irsend SEND_ONCE tv KEY_POWER')
		# os.system('irsend SEND_ONCE tv' + KEY_POWER)

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
