from tkinter import *
from Chatbot import Session

window = Tk()

window.wm_title("Simple Chatbot-NLP")

messages = Text(window)
messages.pack()

messages.insert(INSERT,'Agent:\n' + 'Welcome to the Chatbot-NLP\n\
    Here you can talk to us about\n\
    * Booking a Hotel\n\
    * Booking a Restaurent\n')
   


frame = Frame(window)  # , width=300, height=300)
input_field.bind("<Return>", Enter_pressed)
frame.pack()



window.mainloop()
