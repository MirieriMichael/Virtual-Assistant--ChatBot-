import speech_recognition as sr

def speech_txt():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = r.listen(source, timeout=5)  # Adjust timeout as needed
            voice_data = r.recognize_google(audio)
            return voice_data
        except sr.UnknownValueError:
            return "Error: Could not understand the audio."
        except sr.RequestError:
            return "Error: Speech service is down."
        except Exception as e:
            return f"Error: {str(e)}"
