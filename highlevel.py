from tkinter import *
import requests
import tkinter as tk
from tkinter import ttk
import json
from tkinter import messagebox
root = tk.Tk()
root.title("Weather App")
root.geometry('500x400')

# Function to fetch weather data for a given city
def get_weather(city):
    api_key = '38b93b43883601be779c852e641e98b0'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    res = requests.get(url)

    # Check if request was successful
    if res.status_code == 200:
        # Parse JSON respoanse
        data = res.json()
        print(data)
        return data
    else:
        return none

def fetch_weather(city):
    #city = entry.get().strip()
    data = get_weather(city)
    if data:
        weather_description = data['weather'][0]['description'].capitalize()
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        weather_info = f"Weather: {weather_description}\nTemperature: {temperature}°C\nHumidity: {humidity}%"


        return weather_info
    else:
        return None


def fetch_weather_entry():
    city = entry.get().strip()
    if city:
        weather_info = fetch_weather(city)
        if weather_info:
            weather_display.config(state='normal')
            weather_display.delete(1.0, END)
            weather_display.insert(END, weather_info)
            weather_display.config(state='disabled')
        else:
            messagebox.showerror("Error", "Failed to fetch weather data. Please try again.")
    else:
        messagebox.showwarning("Warning", "Please enter a city name.")

def calculate_statistics(city):
    data = get_weather(city)
    if data:
        temperatures = []
        humidities = []

        for _ in range(5):
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            temperatures.append(temperature)
            humidities.append(humidity)

        avg_temp = sum(temperatures) / len(temperatures)
        max_humidity = max(humidities)

        statistics_info = f"Average Temperature: {avg_temp:.2f}°C\nMax Humidity: {max_humidity}%"
        return statistics_info
    else:
        return None

def display_statistics_entry():
        city = entry.get().strip()
        if city:
            statistics_info = calculate_statistics(city)
            if statistics_info:
                messagebox.showinfo("Statistics", statistics_info)
            else:
                messagebox.showwarning("Warning", "failed to calculate statistics.")
        else:
            messagebox.showwarning("Warning", "Please enter a city name.")


def save_data():
    city = entry.get().strip()
    if city:
        data = get_weather(city)
        if data:
            file = open("weather.json", "w")
            json.dump(data, file)
            messagebox.showinfo("Success", "Data saved.")
        else:
            messagebox.showwarning("Warning", "failed to save data.")
    else:
        messagebox.showwarning("Warning", "Please enter a city name.")

def load_data():
    city = entry.get().strip()
    if city:
        filename = f"{city}weather.json"
        try:
              file = open("weather.json", "r")
              data = json.load(file)
              temp = data['main']['temp']
              humidity = data['main']['humidity']
              pressure = data['main']['pressure']
              weather_info = f"Temp: {temp}\nhumidity: {humidity}\npressure: {pressure}"
              weather_display.config(state='normal')
              weather_display.delete(1.0, END)
              weather_display.insert(END, weather_info)
              weather_display.config(state='disabled')
              messagebox.showinfo("Success", "Data loaded.")
        except FileNotFoundError:
              messagebox.showwarning("Warning", "failed to load data.")
    else:
         messagebox.showwarning("Warning", "Please enter a city name.")

label = tk.Label(root, text="enter city:")
label.pack(pady=10)
entry = tk.Entry(root, width=30)
entry.pack(pady=10)
# Fetch Button
fetch_button = ttk.Button(root, text="Fetch Weather",command=fetch_weather)
fetch_button.pack()

statistics_button = tk.Button(root,text='display statistics',command=display_statistics_entry())
statistics_button.pack()
save_button = tk.Button(root, text='save data',command= save_data)
save_button.pack()
load_button = tk.Button(root, text='load data',command=load_data)
load_button.pack()
weather_display = tk.Text(root, height = '50',width = '30',state='disabled')
weather_display.pack()
root.mainloop()

