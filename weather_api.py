import requests
class Weather_api:
    
    api_key = "ba681c6c43210f960984664da2109e44"
    basic_url = "http://api.openweathermap.org"
    
    lat = ""
    lon = ""
    
    def __init__(self):
        pass
    
    def request_current_weather_data(lat=str, lon=str) -> dict:
        #Construct url for request
        url = f"{Weather_api.basic_url}/data/2.5/weather?lat={lat}&lon={lon}&appid={Weather_api.api_key}&units=metric&lang=de"
        #Request data
        response = requests.get(url)
        #Phrase response data into json
        response_data = response.json()
        
        return response_data
    
    def request_forecast() -> dict:
        #Construct url for request
        url = f"{Weather_api.basic_url}/data/2.5/forecast?lat={Weather_api.lat}&lon={Weather_api.lon}&appid={Weather_api.api_key}&units=metric&lang=de"
        #Request data
        response = requests.get(url)
        #Check response code
        if (response.status_code == 200):
            #Phrase response data into json
            response_data = response.json()
            return response_data
        else:
            print(f"Daten konnten nicht gefunden werden! {response.status_code}")
    
    
    def convert_name_in_location(user_input):
        #Construct url for request
        url = f"{Weather_api.basic_url}/geo/1.0/direct?q={user_input}&limit=1&appid={Weather_api.api_key}"
        #Request data
        response = requests.get(url)
        #Check status code of response
        if(response.status_code == 200):
            #Phrase response data into json
            response_data = response.json()
            #Check if resonse Objekt is emty
            if not response_data:
                return False
            else:
                #Access response data
                response_dict = response_data[0]
                #Extract c of given location
                Weather_api.lat = str(response_dict["lat"])
                Weather_api.lon = str(response_dict["lon"])
                #Start function with given coordinates
                return Weather_api.request_current_weather_data(Weather_api.lat,Weather_api.lon)
        else: 
            print(f"Daten konnten nicht gefunden werden! {response.status_code}")