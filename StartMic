import os                             # NOTE: this requires PyAudio because it uses the Microphone class
import speech_recognition as sr
import re

os.system("say hello")
os.system("say Now i have two function")
os.system("say I can connect facebook and read news")
os.system("say Say something about facebook and news")


r = sr.Recognizer()
os.system("afplay /System/Library/Sounds/Ping.aiff")
 
with sr.Microphone() as source:                # use the default microphone as the audio source
    r.adjust_for_ambient_noise(source)         # listen for 1 second to calibrate the energy threshold for ambient noise levels
    audio = r.listen(source)                   # now when we listen, the energy threshold is already set to a good value, and we can reliably catch speech right away


try:
    print("You said " + r.recognize(audio))    # recognize speech using Google Speech Recognition
    os.system("afplay /System/Library/Sounds/Submarine.aiff")
    responseObj_f= re.search('facebook', r.recognize(audio), re.M|re.I)
    responseObj_n = re.search('news', r.recognize(audio), re.M|re.I)
    if responseObj_f:
    	os.system("python helloWorld.py")
    elif responseObj_n:
    	os.system("python newsCheck.py")
    else:
    	os.system("say i only programmed for facebook so far")
    	os.system("say Can i try again?")
    	os.system("python yesNo.py")
except LookupError:                            # speech is unintelligible
    print("Could not understand audio")
    os.system("afplay /System/Library/Sounds/Submarine.aiff")
    os.system("say Could not understand audio")
    os.system("say Can i try again?")
    os.system("python yesNo.py")

