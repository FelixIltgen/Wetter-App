from weather_api import *
from gui import *
class Main:
    
    def __init__(self):
        pass
    
    weather_data = {}
    user_input = ""
    
    def main() -> None:
        WeatherApp.start_gui()
        print("Wilkommen bei der Wetter-App")
        print("****************************")
        Main.ask_for_user_input()
        Main.extrtact_weather_data(Main.weather_data)
        Main.build_gui(Main.weather_data)
       
    def extrtact_weather_data(data=dict) -> dict:
        data_list = [new_data for new_data in data if new_data == "weather" or new_data =="main" ]
        dict_data = {k: v for (k,v) in data[data_list[0]][0].items()}
        dict_data.update(data[data_list[1]])
        Main.weather_data = dict_data
    
    def build_gui(weather,self) -> None:
        print(f"Aktuelles Wetter für {Main.user_input}".center(48))
        print(f"************************************************")
        print(f"Wetter: {weather["description"]}" )
        print(f"Aktuelle Temperatur: {weather["temp"]:.1f} C° | Gefühlt: {weather["feels_like"]:.1f} C°")
        print(f"Minimal: {weather["temp_min"]:.1f} C° und maximal {weather["temp_max"]:.1f} C°")
        print(f"Luftfeuchtigkeit: {weather["humidity"]} %")
        print(f"************************************************")
        Main.ask_again()
        
    def ask_again():
        user_input = input("Möchtest du erneut Wetterdaten abfargen? Y/N: ").upper()
        if(user_input == "Y"):
            Main.main()
        elif(user_input =="N"):
            print("Tschüss")
        else:
            print("Eingabe ist Falsch!")
            Main.ask_again()
    
    def ask_for_user_input():
        Main.user_input = input("Gebe ein Standort an: ")
        Main.weather_data = Weather_api.convert_name_in_location(Main.user_input)

if __name__ == "__main__":
    Main.main()

#To do's
#Richtige Gui
#Forecast 
#Wetterkarte anzeigens => wenn möglich