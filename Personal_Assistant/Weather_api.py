import requests
from Speech_recon import takeCommand
from Voice_engine import speak
import json
from datetime import datetime
# Not used in Main_Body.py 
# Can use if you wish to use this instead of Wolframalpha in search_run.py
def time_from_utc_with_timezone(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()

def weatherinpit(broken_speech):
        api_key = "PUT API KEY HERE FOR OPENWEATHERMAP"
        city_name = broken_speech[0][0]
        print(city_name)
        weather_url = "http://api.openweathermap.org/data/2.5/weather?q=" + city_name + '&appid='+api_key
        response = requests.get(weather_url)
        weather_data = response.json()

        if weather_data['cod'] == 200:
            kelvin = 273.15
            temp = int(weather_data['main']['temp'] - kelvin)
            feels_like_temp = int(weather_data['main']['feels_like'] - kelvin)
            pressure = weather_data['main']['pressure']
            humidity = weather_data['main']['humidity']
            wind_speed = weather_data['wind']['speed'] * 3.6
            sunrise = weather_data['sys']['sunrise'] #  need to convert because value in large unreadable number
            sunset = weather_data['sys']['sunset'] #  need to convert because value in large unreadable number
            timezone = weather_data['timezone']
            cloudy = weather_data['clouds']['all']
            description = weather_data['weather'][0]['description']
            sunrise_time = time_from_utc_with_timezone(sunrise + timezone)
            sunset_time = time_from_utc_with_timezone(sunset + timezone)

            print(f"Weather Information for {city_name}")
            print(f"Temperature (Celsius): {temp}")
            print(f"Feels like in (Celsius): {feels_like_temp}")
            print(f"Pressure: {pressure}")
            print(f"Humidity: {humidity}")
            print(f"Wind Speed: {0:.2f} km/hr".format(wind_speed))
            print(f"Sunrise at {sunrise_time} and Sunset at {sunset_time}")
            print(f"Cloud: {cloudy}")
            print(f"Info: {description}")

            speak(f"The Current Temperatue in {city_name}, is {temp} Celsius with Wind speeds of {wind_speed}kilometer per hour")
            speak(f"The Current Pressure is {pressure}, along with a Humidity of {humidity}")

        else:
            print(f"City Name: {city_name} was not found!")

        










