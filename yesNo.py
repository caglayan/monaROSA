import os                             # NOTE: this requires PyAudio because it uses the Microphone class
import speech_recognition as sr
import re


os.system("afplay /System/Library/Sounds/Ping.aiff")
r = sr.Recognizer()
with sr.Microphone() as source:                # use the default microphone as the audio source
    r.adjust_for_ambient_noise(source)         # listen for 1 second to calibrate the energy threshold for ambient noise levels
    audio = r.listen(source)                   # now when we listen, the energy threshold is already set to a good value, and we can reliably catch speech right away


try:
    print("You said " + r.recognize(audio))    # recognize speech using Google Speech Recognition
    os.system("afplay /System/Library/Sounds/Submarine.aiff")
    responseObj = re.search('yes', r.recognize(audio), re.M|re.I)
    if responseObj:
    	os.system("python mic.py")
    else:
    	os.system("say ok")
except LookupError:                            # speech is unintelligible
    print("Could not understand audio")
    os.system("say Could not understand audio")
    os.system("say Can i try again?")
    os.system("python yesNo.py")
