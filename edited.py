import requests
import tkinter as tk
from tkinter import ttk, messagebox, END
import json

root = tk.Tk()
root.title("Weather App")
root.geometry('500x400')

# Function to fetch weather data for a given city
def get_weather(city):
    api_key = '38b93b43883601be779c852e641e98b0'  # Replace with your OpenWeatherMap API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    res = requests.get(url)

    # Check if request was successful
    if res.status_code == 200:
        # Parse JSON response
        data = res.json()
        return data
    else:
        return None

def fetch_weather_entry():
    city = entry.get().strip()
    if city:
        weather_info = get_weather(city)  # Corrected function call
        if weather_info:
            weather_display.config(state='normal')
            weather_display.delete(1.0, END)
            weather_display.insert(END, json.dumps(weather_info, indent=2))  # Display JSON data
            weather_display.config(state='disabled')
        else:
            messagebox.showerror("Error", "Failed to fetch weather data. Please try again.")
    else:
        messagebox.showwarning("Warning", "Please enter a city name.")

def display_statistics_entry():
    city = entry.get().strip()
    if city:
        statistics_info = calculate_statistics(city)
        if statistics_info:
            messagebox.showinfo("Statistics", statistics_info)
        else:
            messagebox.showwarning("Warning", "Failed to calculate statistics.")
    else:
        messagebox.showwarning("Warning", "Please enter a city name.")

def save_data():
    city = entry.get().strip()
    if city:
        data = get_weather(city)
        if data:
            with open(f"{city}_weather.json", "w") as file:
                json.dump(data, file, indent=2)
            messagebox.showinfo("Success", "Data saved.")
        else:
            messagebox.showwarning("Warning", "Failed to save data.")
    else:
        messagebox.showwarning("Warning", "Please enter a city name.")

def load_data():
    city = entry.get().strip()
    if city:
        try:
            with open(f"{city}_weather.json", "r") as file:
                data = json.load(file)
                weather_display.config(state='normal')
                weather_display.delete(1.0, END)
                weather_display.insert(END, json.dumps(data, indent=2))  # Display JSON data
                weather_display.config(state='disabled')
            messagebox.showinfo("Success", "Data loaded.")
        except FileNotFoundError:
            messagebox.showwarning("Warning", "Failed to load data.")
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

label = tk.Label(root, text="Enter city:")
label.pack(pady=10)
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

fetch_button = ttk.Button(root, text="Fetch Weather", command=fetch_weather_entry)
fetch_button.pack()

statistics_button = tk.Button(root, text='Display Statistics', command=display_statistics_entry)
statistics_button.pack()

save_button = tk.Button(root, text='Save Data', command=save_data)
save_button.pack()

load_button = tk.Button(root, text='Load Data', command=load_data)
load_button.pack()

weather_display = tk.Text(root, height='10', width='50')
weather_display.pack()

root.mainloop()
