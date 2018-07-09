import speech_recognition as sr

r = sr.Recognizer()

hello = sr.AudioFile('hello.wav')
with hello as source:
  r.adjust_for_ambient_noise(source)
  audio = r.record(source)
  
r.recognize_google(audio)
