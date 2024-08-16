from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import speech_to_txt as speech_to_txt
import action as action
# Function for the button action
def ask():
    ask_val = speech_to_txt.speech_txt()  # Get recognized speech from the microphone

    # If there was an error in speech recognition, insert the error message
    if "Error:" in ask_val:
        text.insert(END, ask_val + '\n')
        return
    
    # Process the recognized speech
    text.insert(END, 'User --> ' + ask_val + '\n')
    
    # Pass the recognized speech to the action handler
    bot_val = action.action(ask_val)
    
    # Handle bot response if any
    if bot_val is not None:
        text.insert(END, 'BOT <-- ' + str(bot_val) + '\n')
    
    # Check if shutdown command is issued
    if bot_val == 'Shutdown':
        root.destroy()


def send():
    print('Sent')
def delete():
    print('Deleted')

# Initialize the main window
root = Tk()
root.title('AI Assistant')
root.geometry('550x675')
root.resizable(False, False)
root.config(bg='#6F8FAF')

# Frame for holding content, centered horizontally
frame = LabelFrame(root, padx=10, pady=10, borderwidth=3, relief='raised', bg='#6F8FAF')
frame.grid(row=0, column=0, padx=20, pady=20, columnspan=2)  # Spanning 2 columns for better centering

# Text label for the title
title_label = Label(frame, text='AI Assistant', font=('Comic Sans MS', 18, 'bold'), bg='#6F8FAF', fg='white')
title_label.grid(row=0, column=0, pady=10)

# Image display
image = ImageTk.PhotoImage(Image.open('images/chatbot.jpg'))
image_label = Label(frame, image=image)
image_label.grid(row=1, column=0, pady=10)

# Scrollbar for Text widget
scrollbar = Scrollbar(root)
scrollbar.grid(row=2, column=1, sticky='ns')  # Grid placement alongside the Text widget

# Text widget for displaying conversation
text = Text(root, font=('Courier', 10, 'bold'), bg='#356696', fg='white', wrap=WORD, yscrollcommand=scrollbar.set)
text.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')  # Adjusted layout for more flexible sizing
scrollbar.config(command=text.yview)

# Entry widget for user input
entry = Entry(root, justify=CENTER, font=('Arial', 12))
entry.place(x=50, y=500, width=450, height=50)

# Button to submit user input
button1 = Button(root, text='Ask', bg='#356696', fg='white', padx=10, pady=16, borderwidth=3, relief=SOLID, command=ask)
button1.place(x=100, y=585, width=60, height=40)
button2= Button(root, text='Send', bg='#356696', fg='white', padx=10, pady=16, borderwidth=3, relief=SOLID, command=send)
button2.place(x=240, y=585, width=60, height=40)
button3= Button(root, text='Delete', bg='#356696', fg='white', padx=10, pady=16, borderwidth=3, relief=SOLID, command=delete)
button3.place(x=400, y=585, width=60, height=40)
# Adjust grid weights to improve layout flexibility
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(2, weight=1)

root.mainloop()
