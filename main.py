import pyttsx3
import tkinter
from tkinter import *
top = tkinter.Tk()
top.title("Speech To Text Converter")
top.geometry("300x194")
top.resizable(width=False, height=False)
def helloCallBack():
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)

    if not E1.get("1.0", "end-1c"):
        engine.say("Please Enter Somthing")
        # play the speech
        engine.runAndWait()
    else:
        text = E1.get("1.0", "end-1c")

        engine.say(text)
        # play the speech
        engine.runAndWait()
E1 = Text(top, bd =0 , width=100 , height=10 , bg="#dfe6e9")
E1.pack()
B = tkinter.Button(top, bd=1 , text ="Speak", command = helloCallBack , width = 100 , bg="#6c5ce7" ,activebackground="#dfe6e9" , fg="white",font="bold")
B.pack()
top.mainloop()