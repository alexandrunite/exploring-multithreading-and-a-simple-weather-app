import requests

api_key = '30d4741c779ba94c470ca1f63045390a'
cities = ['bucharest', 'suceava', 'brasov']
warning_message = 'The application wasn\'t able to extract the data you requested, try again later, or contact the developer at alexnite728@gmail.com'

def get_weather_data(city):
    try:
        weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key}")
        weather_json = weather_data.json()

        if weather_json['cod'] == '404':
            return None

        weather = weather_json['weather'][0]['main']
        temp = round(weather_json['main']['temp'])
        
        return {'weather': weather, 'temp': temp}
    except requests.exceptions.RequestException as e:
        print(f"Error occurred during API request: {e}")
        return None
    except (KeyError, ValueError) as e:
        print("Error parsing API response.")
        return None

weather_data = {}
for city in cities:
    weather_data[city] = get_weather_data(city)

if None in weather_data.values():
    with open("data.txt", "w") as file:
        file.write(warning_message)
else:
    with open("data.txt", "w") as file:
        for city, data in weather_data.items():
            file.write(f"{data['weather']} {data['temp']}°C\n")
            print(f"The weather in {city.capitalize()} is: {data['weather']}")
            print(f"The temperature in {city.capitalize()} is: {data['temp']}°C")
