from weather_api import *

class Main:
    weather_data = {}
    user_input = ""
    def __init__(self):
        pass
    
    def main() -> None:
        Main.start_weather_app()
        Main.extrtact_weather_data(Main.weather_data)
        Main.build_gui(Main.weather_data)
    
    def start_weather_app() -> None:
        print("Wilkommen bei der Wetter-App")
        print("****************************")
        Main.ask_for_user_input()
    
    def extrtact_weather_data(data=dict) -> dict:
        data_list = [new_data for new_data in data if new_data == "weather" or new_data =="main"]
        dict_data = {k: v for (k,v) in data[data_list[0]][0].items()}
        dict_data.update(data[data_list[1]])
        Main.weather_data = dict_data
        print(Main.weather_data)
    
    def build_gui(weather) -> None:
        print(f"Aktuelles Wetter für {Main.user_input}".center(48))
        print(f"************************************************")
        print(f"Wetter: {weather["description"]}")
        print(f"Aktuelle Temperatur: {weather["temp"]:.1f} C° | Gefühlt: {weather["feels_like"]:.1f} C°")
        print(f"Minimal: {weather["temp_min"]:.1f} C° und maximal {weather["temp_max"]:.1f} C°")
        print(f"Luftfeuchtigkeit: {weather["humidity"]} %")
        print(f"************************************************")
        
          
    def ask_for_user_input():
        Main.user_input = input("Gebe ein Standort an: ")
        Main.weather_data = Weather_api.convert_name_in_location(Main.user_input)

if __name__ == "__main__":
    Main.main()