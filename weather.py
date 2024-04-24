from tkinter import *
import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap as ttk

def get_weather(city):
    API_key = "9f9cfecce8ad26f8338f4a8ff51df914"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    res = requests.get(url)
    if res.status_code == 404:
        messagebox.showerror("Error","City not found")
        return None
    weather = res.json()
    icon_id = weather['weather'][0]['icon']
    temperature = weather['main']['temp'] - 273.15
    description = weather['weather'][0]['description']
    city = weather['name']
    country = weather['sys']['country']

    icon_url = f"https://openweathermap.org/img/wn/{icon_id}10d@2x.png" 
    return (icon_url, temperature, description,city, country)

def search():
    city = city_entry.get()
    result = get_weather(city)
    if result is None:
        return
    icon_url, temperature, description, city, country = result
    location_label.configure(text=f"{city},{country}")

    image = Image.open(requests.get(icon_url, stream = True).raw)
    icon = ImageTk.PhotoImage(image)
    icon_label.configure (image=icon)
    icon_label.image = icon

    temperature.configure(text=f"Temperature: {temperature:.2f}°C")
    weather_desc.configure(text=f"Description: {description}")


root = ttk.Window(themename ="morph")
root.title("Mohan's Weather App")
root.geometry("400x400")

city_entry = ttk.Entry(root, font="Helvtica, 19")
city_entry.pack(pady=10)

search_button = ttk.Button(root, text="search", command=search, bootstyle= "warning")
search_button.pack(pady=10)

location_label = tk.Label(root, font="Helvetica, 25")
location_label.pack(pady=20)

icon_label = tk.Label(root)
icon_label.pack()

temperature_label = tk.Label(root, font="Helvetica, 20")
temperature_label.pack()

weather_desc = tk.Label(root, font="Helvetica, 20")
weather_desc.pack()

root.mainloop()