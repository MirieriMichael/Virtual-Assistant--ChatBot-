import json
import speech_to_txt
import text_to_speech
import datetime
#Load predefined questions and answers from a JSON file
with open("responses.json", "r") as file:
    predefined_responses = json.load(file)

def action(data):
    user_data = data.lower().strip()  # Normalize user input by lowering case and stripping spaces
    if user_data == "what is the time":
        current_time = datetime.datetime.now().strftime("%H:%M")
        response = f"It's currently {current_time}."
        text_to_speech.text_speech(response)
        return response
    # Check if the user input matches a predefined response
    if user_data in predefined_responses:
        response = predefined_responses[user_data]
        text_to_speech.text_speech(response)
        return response
    else:
        text_to_speech.text_speech("Sorry, I don't know how to respond to that.")
        return "Sorry, I don't know how to respond to that."
