import requests
class Weather_api:
    
    api_key = "ba681c6c43210f960984664da2109e44"
    basic_url = "http://api.openweathermap.org"
    lat = ""
    lon = ""
    def __init__(self):
        pass
    
    def request_current_weather_data() -> dict:
        url = f"{Weather_api.basic_url}/data/2.5/weather?lat={Weather_api.lat}&lon={Weather_api.lon}&appid={Weather_api.api_key}&units=metric&lang=de"
        response = requests.get(url)
        response_data = response.json()
        print(response_data)
        return response_data
    
    def request_forecast() -> dict:
        pass
     
    def convert_name_in_location(user_input):
        url = f"{Weather_api.basic_url}/geo/1.0/direct?q={user_input}&limit=1&appid={Weather_api.api_key}"
        response = requests.get(url)
        if(response.status_code == 200):
            response_data = response.json()
            response_dict = response_data[0] #==> Wirft error wenn Stanndort nicht exsisitiert
            Weather_api.lat = str(response_dict["lat"])
            Weather_api.lon = str(response_dict["lon"])
            return Weather_api.request_current_weather_data()
        else: 
            print(f"Daten konnten nicht gefunden werden! {response.status_code}")