import requests

api_key = '30d4741c779ba94c470ca1f63045390a'

warning1 = 'The application wasnt able to extract the data you requested, try again later, or contact the developer at alexnite728@gmail.com'


try:
    weather_data_bucharest = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=bucharest&units=metric&APPID={api_key}")
    weather_data_suceava = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=suceava&units=metric&APPID={api_key}")
    weather_data_brasov = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=brasov&units=metric&APPID={api_key}")

    weather_json_bucharest = weather_data_bucharest.json()
    weather_json_suceava = weather_data_suceava.json()
    weather_json_brasov = weather_data_brasov.json()

    if weather_json_bucharest['cod'] == '404' or weather_json_suceava['cod'] == '404' or weather_json_brasov['cod'] == '404':
        with open("data.txt", "w") as file:
            file.write(warning1)
    else:
        weather_bucharest = weather_json_bucharest['weather'][0]['main']
        temp_bucharest = round(weather_json_bucharest['main']['temp'])

        weather_suceava = weather_json_suceava['weather'][0]['main']
        temp_suceava = round(weather_json_suceava['main']['temp'])

        weather_brasov = weather_json_brasov['weather'][0]['main']
        temp_brasov = round(weather_json_brasov['main']['temp'])

        with open("data.txt", "w") as file:
            file.write(f"{weather_bucharest} {temp_bucharest}"+ "\n")
            file.write(f"{weather_brasov} {temp_brasov}"+ "\n")
            file.write(f"{weather_suceava} {temp_suceava}")
        print(f"The weather in Bucharest is: {weather_bucharest}")
        print(f"The temperature in Bucharest is: {temp_bucharest}°C")
        print(f"The weather in Suceava is: {weather_suceava}")
        print(f"The temperature in Suceava is: {temp_suceava}°C")
        print(f"The weather in Brasov is: {weather_brasov}")
        print(f"The temperature in Brasov is: {temp_brasov}°C")
except requests.exceptions.RequestException as e:
    print(f"Error occurred during API request: {e}")
except (KeyError, ValueError) as e:
    print("Error parsing API response.")

