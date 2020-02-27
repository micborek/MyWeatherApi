import urllib.request
import json
from datetime import datetime, date
import custom

api_path = "http://api.openweathermap.org/data/2.5/weather?q="+custom.city+"&units=metric&lang=pl&appid=b03040b45d9db1e91b4952b8870e9986"
with urllib.request.urlopen(api_path) as url:
    data = json.loads(url.read())


def get_location():
    # get location from API
    location = f"{data['name'].title()}, {data['sys']['country']}"
    return location


def get_temp():
    # get temperature from API
    temp = int(round(data['main']['temp']))
    return temp


def get_pressure():
    # get pressure from API
    pressure = int(data['main']['pressure'])
    return pressure


def get_humidity():
    # get humidity from API
    humidity = int(data['main']['humidity'])
    return humidity


def get_weather_id():
    # get weather_id from API
    weather_id = data['weather'][0]['id'] # for icons
    return str(weather_id)


def get_weather_desc():
    # get weather description from API
    weather_desc = data['weather'][0]['description'].title()
    return weather_desc


def get_wind():
    # get wind value in m/s from API
    wind = int(round(data['wind']['speed']))
    return wind


def get_sunrise():
    # get sunrise time and translate from unix
    sunrise_timestamp = data['sys']['sunrise']
    sunrise_time = datetime.fromtimestamp(sunrise_timestamp)
    ret_sunrise_time = str(sunrise_time.time())[0:5]
    return ret_sunrise_time


def get_sunset():
    # get sunset time and translate from unix
    sunset_timestamp = data['sys']['sunset']
    sunset_time = datetime.fromtimestamp(sunset_timestamp)
    ret_sunset_time = str(sunset_time.time())[0:5]
    return ret_sunset_time

def get_icon():
    # get icon for weather_id
    weather_id = get_weather_id()
    if weather_id == '800':
        file_name='01d.png'
    elif weather_id == '801':
        file_name = '02d.png'
    elif weather_id == '802':
        file_name = '03d.png'
    elif str(weather_id) in ('803','804'):
        file_name = '04d.png'
    elif str(weather_id)[:1] == '2':
        file_name='11d.png'
    elif str(weather_id)[:1] == '3':
        file_name='09d.png'
    elif str(weather_id)[:1] == '5':
        file_name='10d.png'
    elif str(weather_id)[:1] == '6':
        file_name='13d.png'
    elif str(weather_id)[:1] == '7':
        file_name='50d.png'
    else:
        file_name = '01d.png'
    return file_name

def get_date():
    # get date for the app display
    return date.today().strftime("%d.%m.%Y")

def get_holiday():
    # get holiday name from the custom.calendar
    today = date.today().strftime("%d%m")
    if today in custom.calendar:
        holiday = custom.calendar.get(today)
    else:
        holiday = ''
    return holiday
