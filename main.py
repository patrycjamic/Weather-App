import tkinter as tk
import requests
from tkinter import messagebox
from datetime import date
import calendar


# General Setup
root = tk.Tk()
root.title('Weather App')
root.iconbitmap('icon.ico')
root.geometry('600x500')

# Binding Enter Key to work as 'Generate' button
def callback(event):
    get_weather(textbox.get())

root.bind('<Return>', callback)

def get_help():
    message_text = '''
    To search your city weather type your city 
    into textbox and click 'Generate'. 
    To be more specific you can add name of your 
    city and country code after comma.
    For example: Paris, FR
    '''
    my_message = tk.messagebox.showinfo('Info', message_text)

# Assigning informations
def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        final_str = f'City name: {name}\nConditions: {desc}\nTemperature: {temp} °C'
    except:
        final_str = 'Invalid city name'
    return final_str

# Getting and displaying informations
def get_weather(city):
    weather_key= '3c580ccd1e780ff38aaccb4144227e3f'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_key}&units=metric'
    response = requests.get(url)
    weather = response.json()

    label_display['text'] = f'{format_response(weather)}\n\n{calendar.day_name[date.today().weekday()] }'

# Background
bg_image = tk.PhotoImage(file='landscape.png')
bg_label = tk.Label(root, image=bg_image).place(relwidth=1, relheight=1)

# Frames
frame = tk.Frame(root, bg='#A5DDE0', bd=5)
frame.place(relx = 0.5, rely=0.21,relwidth=0.75, relheight=0.1, anchor='n')

lower_frame = tk.Frame(root, bg='#A5DDE0', bd=7)
lower_frame.place(relx=0.5, rely=0.35, relwidth=0.75, relheight=0.6, anchor='n')

# Entries
textbox = tk.Entry(frame, font=('Garamond', 15), borderwidth=2, relief=tk.FLAT)
textbox.place(relwidth=0.65, relheight=1)

# Buttons
btn_submit = tk.Button(frame, text='Generate', font=('Garamond', 15), command=lambda: get_weather(textbox.get()))
btn_submit.place(relx=0.7, relwidth=0.3, relheight=1)

btn_help = tk.Button(root, text='Help', font=('Garamond', 12), command=get_help)
btn_help.place(relx=0.98, rely=0.02, relwidth=0.12, relheight=0.05, anchor="ne")

# Labels
label_display = tk.Label(lower_frame, bg='white', font=('Garamond', 15))
label_display.place(relwidth=1, relheight=1)

root.mainloop()
