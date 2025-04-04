# Wetter-App ☀️🌦️
### A compact weather program to determine the current weather for any location.

This is a compact weather app that determines the current weather and a five-day weather forecast for any location. The program receives the required data via an API request. The free version of the [OpenWeather](https://openweathermap.org/) API was used for this purpose. The data received via the request is adjusted by the program and reduced to the scope required for this project. The data is then presented to the user in a visual format.

![Image](https://github.com/user-attachments/assets/9a7ee1b4-bc07-4b37-ba70-c6accab4e781)
![Image](https://github.com/user-attachments/assets/7b4c32b2-0fe0-420f-8dc2-3481027cdb1f)

The project was written in:
```
Python 3.13.0
```
### Note!
In order to be able to use all functions of the program without errors, it is essential that the end device is in the CET time zone. If this is nevertheless the case, errors may occur in the time information when using the program.
## Use & installation
### Required resources
The following Python modules are required for use:
* PyQt5

If not installed:
* Requests
### Instalation
Clone this repository to any location on your computer. Then execute the gui.py file in a Python-capable IDM.
 
=> An executable is in progress.

## API
### Documentation of the API
* [Current weather data](https://openweathermap.org/current)
* [5 day weather forecast](https://openweathermap.org/forecast5)
* [Geocoding API](https://openweathermap.org/api/geocoding-api)
### KEY & URL
```
api_key = "ba681c6c4328654sdf6664da2109e44" #Dummy-Key
basic_url = "http://api.openweathermap.org
```
### Grundlegende Funktion der API
To query a location using the [Current weather data API](https://openweathermap.org/current), the coordinates of the desired location must first be determined using the [Geocoding API](https://openweathermap.org/api/geocoding-api). The coordinates are required for the request with the Current weather data API and [5 day weather forecast API](https://openweathermap.org/forecast5). These provide a JSON file with all the required data as a response.
### API Requests
The following parameters are always required for the API request. A valid API key can be obtained by registering with OpenWeather.
## KEY & Basic URL
```
api_key = "ba681c6c4328654sdf6664da2109e44" #Dummy-Key
basic_url = "http://api.openweathermap.org
```
## Geo Coding
The name of the desired location is also required to calculate the coordinates. The limit is optional and refers to the number of locations contained in the response.
### Beispiel
```
http://api.openweathermap.org/geo/1.0/direct?q={city name}
&limit={limit}&appid={API key}

http://api.openweathermap.org/geo/1.0/direct?q=London
&limit=5&appid={API key}
```
## Current weather data API
With the coordinates, it is now possible to query the weather for the respective location. To do this, the request URL must be changed slightly.
```
https://api.openweathermap.org/data/2.5/weather?
lat={lat}&lon={lon}&appid={API key}

https://api.openweathermap.org/data/2.5/weather?
lat=44.34&lon=10.99&appid={API key}
``` 
Zusätzlich können weitere Parameter dem Request mitgegeben werden, um die Daten zu spezifizieren. 
Nutze für eine detailliertere Dokumentation der API und ihrer Funktionen die Doku von [OpenWeather](https://openweathermap.org/).
