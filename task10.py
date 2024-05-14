# import subprocess
import requests
# subprocess.run(['python', '-m', 'pip', 'install', 'requests'])

#city = input("Enter City:")

#api_key = '38b93b43883601be779c852e641e98b0'
def get_weather(city, api_key):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'''
    res = requests.get(url)
    return res.json()

# Main function
def main():
    api_key = '38b93b43883601be779c852e641e98b0'

    # While loop to allow user to fetch weather data for different locations
    while True:
        city = input("Enter City (type 'exit' to quit): ")
        if city.lower() == 'exit':
            print("Exiting...")
            break

        # Fetch weather data for the given city
data = get_weather(city, api_key)
if 'main' in data:
    humidity = data['main']['humidity']
pressure = data['main']['pressure']
temp = data['main']['temp']
else:
print("City not found. Please try again.")
continue

if 'wind'in data :
wind = data['wind']['speed']
wind_direction = data['wind'].get('deg', 'N/A')
        else:
             wind_speed = "N/A"
             wind_direction = "N/A"
if 'weather' in data and len(data['weather']) > 0:
    description = data['weather'][0]['description']
    else:
        description = "N/A"
# Print weather information
print('\nWeather Information for', city)
print('Temperature:',temp,'°C')
print('Humidity:', humidity, '%')
print('Pressure:', pressure, 'hPa')
print('Wind Speed:', wind_speed, 'm/s')
print('Wind Direction:', wind_direction)
print('Description:', description)

