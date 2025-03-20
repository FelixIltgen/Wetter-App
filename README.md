# Wetter-App ☀️🌦️
### Ein kompaktes Wetter Programm für das aktuelle Wetter. 

Hierbei handelt es sich um eine kompakte Wetter-App, welche das aktuelle Wetter und eine fünftägige Wettervorhersage für einen beliebigen Standort ermittelt. Die dafür benötigten Daten erhält das Programm über einen API Request. Dazu wurde die kostenlose Version der API von [OpenWeather](https://openweathermap.org/) genutzt. Die durch den Request erhaltenen Daten werden durch das Programm bereinigt und für den in diesem Projekt benötigten Umfang reduziert. Anschließend werden die Daten dem Nutzer visuell aufbereitet präsentiert. 

![Image](https://github.com/user-attachments/assets/9a7ee1b4-bc07-4b37-ba70-c6accab4e781)
![Image](https://github.com/user-attachments/assets/7b4c32b2-0fe0-420f-8dc2-3481027cdb1f)

Geschrieben wurde das Projekt mit:
```
Python 3.13.0
```
### Hinweis!
Um alle Funktionen des Programms fehlerfrei nutzen zu können, ist es zwingend notwenig, dass sich das Endgerät in der [CET](https://www.timeanddate.com/time/zones/cet) Zeitzone befindet. Falls dies dennoch der Fall sein sollte, kann es bei der Nutzung zu Fehlern bei den Zeitangaben kommen.
## Nutzung & Instalation
### Benötigte Ressourcen
Folgende Python Module werden für die Nutzung benötigt.
* PyQt5

Falls nicht installiert:
* Requests
### Instalation
Clone dieses Repository an einen belibiebigen Ort deines Computers. Führe anschließend in einer Python fähigen IDM die gui.py Datei aus.
 
=> Eine executable ist in Arbeit.

## API
### Doku der API
* [Current weather data](https://openweathermap.org/current)
* [5 day weather forecast](https://openweathermap.org/forecast5)
* [Geocoding API](https://openweathermap.org/api/geocoding-api)
### KEY & URL
```
api_key = "ba681c6c4328654sdf6664da2109e44" #Dummy-Key
basic_url = "http://api.openweathermap.org
```
### Grundlegende Funktion der API
Um einen Standort mit der [Current weather data API](https://openweathermap.org/current) abzufragen, müssen zunächst mit der [Geocoding API](https://openweathermap.org/api/geocoding-api) die Koordinaten des gewünschten Standorts ermittelt werden. Die Koordinaten werden für den Request bei der [Current weather data API](https://openweathermap.org/current) und [5 day weather forecast API](https://openweathermap.org/forecast5) benötigt. Diese liefern als Response eine JSON-Datei mit allen benötigten Daten.
### API Requests
Für den Request bei der API werden zunächst immer folgende Parameter benötigt. Einen gültigen API-Key kann durch die Anmeldung bei OpenWeather erhalten werden. 
## KEY & Basic URL
```
api_key = "ba681c6c4328654sdf6664da2109e44" #Dummy-Key
basic_url = "http://api.openweathermap.org
```
## Geo Coding
Für die Berechnung der Koordinaten werden zusätzlich der Name des gewünschten Standorts benötigt. Das Limit ist optional und bezieht sich auf die Anzahl an Standorten, welche in der Response enhalten sind.
### Beispiel
```
http://api.openweathermap.org/geo/1.0/direct?q={city name}
&limit={limit}&appid={API key}

http://api.openweathermap.org/geo/1.0/direct?q=London
&limit=5&appid={API key}
```
## Current weather data API
Mit den Koordinaten ist es nun möglich, das Wetter für den jeweiligen Standort abzufragen. Dazu muss die Request URL leicht verändert werden.
```
https://api.openweathermap.org/data/2.5/weather?
lat={lat}&lon={lon}&appid={API key}

https://api.openweathermap.org/data/2.5/weather?
lat=44.34&lon=10.99&appid={API key}
``` 
Zusätzlich können weitere Parameter dem Request mitgegeben werden, um die Daten zu spezifizieren. 
Nutze für eine detailliertere Dokumentation der API und ihrer Funktionen die Doku von [OpenWeather](https://openweathermap.org/).
