import requests
class Weather_api:
    
    api_key = "ba681c6c43210f960984664da2109e44"
    basic_url = "http://api.openweathermap.org"
    lat = ""
    lon = ""
    def __init__(self):
        pass
    
    def request_current_weather_data():
        url = f"{Weather_api.basic_url}/data/2.5/weather?lat={Weather_api.lat}&lon={Weather_api.lon}&appid={Weather_api.api_key}&units=metric&lang=de"
        response = requests.get(url)
        response_data = response.json()
        Weather_api.extract_weather_data(response_data)
    
    def request_forecast() -> dict:
        pass
    
    def extract_weather_data(data) -> dict:
        pass
    
    def convert_name_in_location(user_input) -> None:
        url = f"{Weather_api.basic_url}/geo/1.0/direct?q={user_input}&limit=1&appid={Weather_api.api_key}"
        response = requests.get(url)
        if(response.status_code == 200):
            response_data = response.json()
            response_dict = response_data[0]
            Weather_api.lat = str(response_dict["lat"])
            Weather_api.lon = str(response_dict["lon"])
            Weather_api.request_current_weather_data()
        else: 
            print(f"Daten konnten nicht gefunden werden! {response.status_code}")