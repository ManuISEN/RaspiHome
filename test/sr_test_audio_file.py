#!/usr/bin/env python3

# pip install SpeechRecognition

# NOTE : this exemple requires the file 'hello.wav' as an audio source file

import speech_recognition as sr

# obtain audio from the audio file
r = sr.Recognizer()
hello = sr.AudioFile('hello.wav')

with hello as source:
  r.adjust_for_ambient_noise(source)
  print "Adjusting ambient noise..."
  audio = r.record(source)
  
# recognize audio using Speech Recognition
try:
  print("Google Speech Recognition thinks the voice in audio file said in English: -  " + r.recognize_google(audio, language = "en-US"))
  print("Google Speech Recognition thinks the voice in audio file said in French: -  " + r.recognize_google(audio, language = "fr-FR"))
except sr.UnknownValueError:
	print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
	print("Could not request results from Google Speech Recognition service; {0}".format(e))
 
