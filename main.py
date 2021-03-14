#importing modules
import pyautogui
import PIL.Image
import PIL.ImageTk
import time
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import webbrowser as wb
import pygame
import random

#pyinstaller.exe --onefile -w --icon=clymate_logo.ico main.py

#setting up the window
window=tk.Tk()
window.title("Clymate")
window.iconbitmap('clymate_logo.ico')
window.geometry('1000x600')
window.resizable(False,False)
colour=['#00ff5a','#6ccde2','#ee6aa7','#ff0000','#99a7a3','#1fad8d','#66cdaa','#0080ff','#b6fcd5','#ffa500']#for random bg colours
list_index=random.randint(0,9)
window.configure(bg=colour[list_index])

#-------IMAGE-------
fp = open("Clymate.png","rb")
app_image = PIL.Image.open(fp)
app_photo = PIL.ImageTk.PhotoImage(app_image)
app_img_label=Label(image=app_photo)
app_img_label.place(x=450,y=3)

#speaker images
fso = open("speaker-on.png","rb")
speaker_on_image = PIL.Image.open(fso)
speaker_on_photo = PIL.ImageTk.PhotoImage(speaker_on_image)

fsoff = open("speaker-off.jpg","rb")
speaker_off_image = PIL.Image.open(fsoff)
speaker_off_photo = PIL.ImageTk.PhotoImage(speaker_off_image)



#-------FUNCTIONS-------

#online tools
def AQI():
    wb.open('https://waqi.info/')
    time.sleep(6)
    AQ1_locationCoords=pyautogui.locateCenterOnScreen("AQI_location symbol.PNG")
    pyautogui.click(AQ1_locationCoords)

def population():
    wb.open('https://www.worldometers.info/world-population/')
    time.sleep(6)

def sound_check():
    wb.open('https://youlean.co/online-loudness-meter/')
    time.sleep(6)

#information resources
def why_climate():
    wb.open('https://www.youtube.com/watch?v=EtW2rrLHs08')
    pyautogui.click(x=50, y=200)
    time.sleep(6)
    pyautogui.click(x=50, y=200)
    pyautogui.press('f')

def animal_extinct():
    wb.open('https://www.youtube.com/watch?v=nho73BtDQtE')
    pyautogui.click(x=50, y=200)
    time.sleep(6)
    pyautogui.click(x=50, y=200)
    pyautogui.press('f')

def whose_fault():
    wb.open('https://www.youtube.com/watch?v=ipVxxxqwBQw')
    pyautogui.click(x=50, y=200)
    time.sleep(6)
    pyautogui.click(x=50, y=200)
    pyautogui.press('f')

#bg music control
def play():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("Nature sounds.wav")
    pygame.mixer.music.play(2)
    pygame.mixer.music.set_volume(1.0)
    #print(pygame.mixer.music.get_busy())

def stop_play():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.stop()
    #print(pygame.mixer.music.get_busy())


#my og music
def my_inform():
    wb.open("https://youtu.be/KYU-F_90NaU")
    pyautogui.click(x=50, y=200)
    time.sleep(5)
    pyautogui.click(x=50, y=200)
    pyautogui.press('f')

#information popup
def AQI_popup():
    messagebox.showinfo("💡 AQI Check","This will take you to a website which will show you the Air Quality Index(AQI) in your nearby locations. Give location permissions.")

def population_popup():
    messagebox.showinfo("💡 World Population Meter","A real-time estimation of world population with births and death. Population control is necessary.")

def sound_popup():
    messagebox.showinfo("💡 Decibel Check","This website will use your device microphone to measure the decibel of sound you are subject to at the moment. Give microphone permissions.")

#-------BUTTONS-------

#quit button
button_quit=Button(window,text='Exit',bg='red',font=('Arial Bold',12),command=window.quit)
button_quit.place(x=500,y=500)

#online tools buttons
button_AQI=Button(window,text='AQI Check',bg='light blue',font=('Arial',12),command=lambda:AQI())
button_AQI.place(x=100,y=400)

button_population=Button(window,text='World Population Meter',bg='light blue',font=('Arial',12),command=lambda:population())
button_population.place(x=400,y=400)

button_soundcheck=Button(window,text='Decibel Check',bg='light blue',font=('Arial',12),command=lambda:sound_check())
button_soundcheck.place(x=800,y=400)

#information resource button
button_why_climate=Button(window,text='Why climate matters?',bg='orange',font=('Arial',12),command=lambda:why_climate())
button_why_climate.place(x=100,y=230)

button_animal_extinct=Button(window,text='Threat to animals?',bg='orange',font=('Arial',12),command=lambda:animal_extinct())
button_animal_extinct.place(x=450,y=230)

button_fault=Button(window,text='Who is to blame?',bg='orange',font=('Arial',12),command=lambda:whose_fault())
button_fault.place(x=800,y=230)

#music control button
button_bg_music_play=Button(window,image=speaker_on_photo,width=35,height=35,command=lambda:play())
button_bg_music_play.place(x=900,y=10)

button_bg_music_stop=Button(window,image=speaker_off_photo,width=35,height=35,command=lambda:stop_play())
button_bg_music_stop.place(x=950,y=10)

my_info=Button(window,text='Made my Sam ♪♫*•♪',bg='#ff6a6a',font=('Helvetica',8),command=lambda:my_inform())
my_info.place(x=850,y=500)

#info for tool buttons
message_AQI=Button(window,text='💡',bg='#ff6a6a',font=('Helvetica',12),command=lambda:AQI_popup())
message_AQI.place(x=213,y=400)

message_population=Button(window,text='💡',bg='#ff6a6a',font=('Helvetica',12),command=lambda:population_popup())
message_population.place(x=624,y=400)

message_sound=Button(window,text='💡',bg='#ff6a6a',font=('Helvetica',12),command=lambda:sound_popup())
message_sound.place(x=943,y=400)

#-------TEXT FIELDS-------

#intro text
Intro_text=Text(window,width=86,height=3)
Intro_text.place(x=100,y=130)
Intro_text.insert(tk.END,"Hey! Climate change is an important topic. The later we realize, the more we suffer. Below are a few resources that will help in understanding the problems caused by us humans and why we need to worry.")
Intro_text.configure(state='disabled')

#tools text
Tools=Text(window,width=86,height=3)
Tools.place(x=100,y=300)
Tools.insert(tk.END,"These are some great tools to help you. Click on '💡' for more information.")
Tools.configure(state='disabled')


window.mainloop()
#thank you:)