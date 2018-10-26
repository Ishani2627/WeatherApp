import tkinter as tk
import pyowm
import json
import PIL
import config
import requests
import datetime, time
from PIL import ImageTk, Image

obj = tk.Tk()
obj.geometry("320x320")
obj.title("Weather Map")
obj.configure(bg = "white")

img = ImageTk.PhotoImage(Image.open('download.jpg'))
panel = tk.Label(obj, image = img, bg = 'white')
panel.place(x = 107, y = 3)

label0 = tk.Label(obj, text = "Weather App", width = 20, font = ("bold",20), fg = "black")
label0.place(x = 0, y = 90)

city_name = tk.StringVar()
label = tk.Label(obj, text = "City" , width = 10)
label.place(x = 40, y = 140)
entry = tk.Entry(obj, textvar = city_name)
city_name.set("Enter_city")
entry.place(x = 100, y = 140)

label1 = tk.Label(obj, text = "Temperature : ", width = 20, bg = 'white', font = ("bold",10), fg = 'blue')
label1.place(x = 62, y = 220)
label2 = tk.Label(obj, text = "Pressure : ", width = 20, bg = 'white', font = ("bold",10), fg = 'blue')
label2.place(x = 62, y = 240)
label3 = tk.Label(obj, text = "Description : ", width = 20, bg = 'white', font = ("bold",10), fg = 'blue')
label3.place(x = 62, y = 260)

label4 = tk.Label(obj, text = "   ", width = 10, bg = 'white', font = ("bold",10), fg = 'blue')
label4.place(x = 192, y = 220)
label5 = tk.Label(obj, text = "   ", width = 10, bg = 'white', font = ("bold",10), fg = 'blue')
label5.place(x = 192, y = 240)
label6 = tk.Label(obj, text = "   ", width = 10, bg = 'white', font = ("bold",10), fg = 'blue')
label6.place(x = 192, y = 260)


def get_data():
    api_key = "<enter your api key>"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    city_name = entry.get()
    complete_url = base_url+"appid="+api_key+"&q="+city_name
   
    response = requests.get(complete_url)
    x = response.json()

    if["cod"] != '404':
        y = x["main"]
        current_temp = y["temp"]
        current_pressure = y["pressure"]

        z = x["weather"]
        weather_desc = z[0]["description"]
    else:
        label4.configure(text = "error")
        label5.configure(text = "error")
        label6.configure(text = "error")

button = tk.Button(obj, text = "Show Weather", width = 10, bg = 'brown', fg = 'white', command = get_data)
button.place(x = 122, y =170)

obj.mainloop()