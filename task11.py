import requests
from tkinter import *
from tkinter import ttk
# Function to fetch weather data for a given city
def get_weather(city, api_key):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    res = requests.get(url)
    return res.json()


# Main function
def main():
    api_key = '38b93b43883601be779c852e641e98b0'

    # While loop to allow user to fetch weather data for different locations
    while True:
        city = input("Enter City (type 'exit' to quit): ")
        if city.lower() == 'exit':#z8ar 
            print("Exiting...")
            break

        # Fetch weather data for the given city
        data = get_weather(city, api_key)

        # Extract weather information from the API response
        if 'main' in data:
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            pressure = data['main']['pressure']
        else:
            print("City not found. Please try again.")
            continue

        if 'wind' in data:
            wind_speed = data['wind']['speed']
            wind_direction = data['wind'].get('deg', 'N/A')#key hye deg 
        else:
            wind_speed = "N/A"
            wind_direction = "N/A"

        if 'weather' in data and len(data['weather']) > 0:
            description = data['weather'][0]['description']
        else:
            description = "N/A"#intial

        # Print weather information
        print('\nWeather Information for', city)
        print('Temperature:', temp, '°C')
        print('Humidity:', humidity, '%')
        print('Pressure:', pressure, 'hPa')
        print('Wind Speed:', wind_speed, 'm/s')
        print('Wind Direction:', wind_direction)
        print('Description:', description)


# Entry point of the program
if __name__ == "__main__":
    root = Tk()
    root.geometry('500x500') #size la interface kila
    root.title('weather app')#title ela
    label=Label(root,text='enter city')#variable
    label.pack()
    entry =Entry(root)#text used for multiple user
    entry.pack()
    button=Button(root,text='submit')#button
    button.pack()

    download = PhotoImage (file= "C:\\Users\\Laptops pro\\Desktop\\New folder\\download.png")#esm sora width and height  label
    image_label = Tk.Label(root, image=download)
    image_label.pack()
    #weather_icon_path = 'C:\\Users\\Laptops pro\\Desktop\\download.png'
    #weather_image = Image.open(weather_icon_path)
    #image = tk.PhotoImage(file="C:\Users\Laptops pro\Desktop")
    #label = ttk.Label(image=image)
    #label.pack()
    root.mainloop()
   # main()
''' check1  = Checkbutton(root, text='male')
    check1.pack()
    check2  = Checkbutton(root, text='male')
    check2.pack()
    radio1 = Radiobutton(root,text='male')
    radio1.pack()
    radio2 = Radiobutton(root, text='female')
    radio2.pack()'''
#entery text button
#button
#root geometry hded length and width