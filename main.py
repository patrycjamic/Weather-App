import tkinter as tk, tkinter.messagebox
import requests
from datetime import date
import calendar

# The main application is class
class MainApplication(tk.Frame):
    # General setup
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        master.title('Weather App')
        master.iconbitmap('icon.ico')
        master.geometry('600x500')

        # Function call to bind Enter key and 'Generate' button
        master.bind('<Return>', self.callback)

        # Background
        self.bg_image = tk.PhotoImage(file='landscape.png')
        self.bg_label = tk.Label(master, image=self.bg_image).place(relwidth=1, relheight=1)

        # Frames
        self.frame = tk.Frame(master, bg='#A5DDE0', bd=5)
        self.frame.place(relx = 0.5, rely=0.21,relwidth=0.75, relheight=0.1, anchor='n')

        self.lower_frame = tk.Frame(master, bg='#A5DDE0', bd=7)
        self.lower_frame.place(relx=0.5, rely=0.35, relwidth=0.75, relheight=0.6, anchor='n')

        # Entries
        self.textbox = tk.Entry(self.frame, font=('Garamond', 15), borderwidth=2, relief=tk.FLAT)
        self.textbox.place(relwidth=0.65, relheight=1)

        # Buttons
        self.btn_submit = tk.Button(self.frame, text='Generate', font=('Garamond', 15), command=lambda: self.get_weather(self.textbox.get()))
        self.btn_submit.place(relx=0.7, relwidth=0.3, relheight=1)

        self.btn_help = tk.Button(master, text='Help', font=('Garamond', 12), command=self.get_help)
        self.btn_help.place(relx=0.98, rely=0.02, relwidth=0.12, relheight=0.05, anchor="ne")

        # Labels
        self.label_display = tk.Label(self.lower_frame, bg='white', font=('Garamond', 15))
        self.label_display.place(relwidth=1, relheight=1)

    # Function that display messagebox with instruction how to use Weather App
    def get_help(self):
        self.message_text = '''
        To search your city weather type your city
        into textbox and click 'Generate'.
        To be more specific you can add name of your
        city and country code after comma.
        For example: Paris, FR
        '''
        self.my_message = tkinter.messagebox.showinfo('Info', self.message_text)

    # Formatting response
    def format_response(self, weather):
        try:
            self.name = weather['name']
            self.desc = weather['weather'][0]['description']
            self.temp = weather['main']['temp']
            self.day = calendar.day_name[date.today().weekday()]
            self.final_str = f'City name: {self.name}\nConditions: {self.desc}\nTemperature: {self.temp} °C\n\n{self.day}'
        except:
            self.final_str = 'Invalid city name'
        return self.final_str

    # Data acquisition
    def get_weather(self, city):
        self.weather_key = '3c580ccd1e780ff38aaccb4144227e3f'
        self.url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.weather_key}&units=metric'
        self.response = requests.get(self.url)
        self.weather = self.response.json()
        self.label_display['text'] = f'{self.format_response(self.weather)}'

    # Function that bind Enter key and 'Generate' button
    def callback(self, event):
        self.get_weather(self.textbox.get())

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
