from weather_api import *

class Main:
    
    user_input = ""
    def __init__(self):
        pass
    
    def main() -> None:
        Main.start_weather_app()
    
    def start_weather_app() -> None:
        print("Wilkommen bei der Wetter-App")
        print("****************************")
        Main.ask_for_user_input()
    
    def build_gui() -> None:
        pass
    
    def get_weather_icon() -> None:
        pass
    
    def ask_for_user_input():
        Main.user_input = input("Gebe ein Standort an: ")
        print(Weather_api.convert_name_in_location(Main.user_input))

if __name__ == "__main__":
    Main.main()