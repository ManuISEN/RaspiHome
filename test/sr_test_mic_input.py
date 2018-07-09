#!/usr/bin/env python3

# pip install SpeechRecognition

# NOTE: this example requires PyAudio because it uses the Microphone class

# List all the microphones present on your system
# sr.Microphone.list_microphone_names

import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
mic = sr.Microphone()

# mic = sr.Microphone(device_index=X)
# X is the number of desired (hw:0,X) from result of sr.Microphone.list_microphone_names()
# use either mic = sr.Microphone() (default microphone) or mic = sr.Microphone(device_index=X)

with mic as source:
  r.adjust_for_ambient_noise(source)
  print ("Adjusting ambient noise...")
  print ("Say something!")
  audio = r.listen(source)
  
# recognize speech using Google Speech Recognition
try:
  print("Google Speech Recognition thinks you said in English: -  " + r.recognize_google(audio, language = "en-US"))
  print("Google Speech Recognition thinks you said in English: -  " + r.recognize_google(audio, language = "fr-FR"))
except sr.UnknowValueError:
  print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
  print("Could not request results from Google Speech Recognition service; {0}".format(e))

