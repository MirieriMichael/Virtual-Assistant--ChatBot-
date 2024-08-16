import pyttsx3
def text_speech(text):
    engine=pyttsx3.init()
    rate=engine.getProperty('rate')
    engine.setProperty('rate','rate-70')
    engine.say(text)
    engine.runAndWait()
text_speech('Hello Chase the bag')