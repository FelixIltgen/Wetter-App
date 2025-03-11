from weather_api import *
from style_sheet import *

import sys as syst
import time
import json

from datetime import timezone as tz
from datetime import datetime

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QDesktopWidget, QLineEdit, QPushButton, QVBoxLayout, QGraphicsDropShadowEffect
from PyQt5.QtGui import QIcon, QPixmap 
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    user_input = ""
    weather_data = {}
    forecast_data = {}
    
    def __init__(self):
        super().__init__()
        #Initialise GUI components
        self.input_field = QLineEdit("Herbolzheim",self)
        self.button_search = QPushButton("Wetter suchen 🔎",self)
        self.weather_pic = QLabel(self)
        self.pixmap = QPixmap("")
        self.time_label = QLabel(self)
        self.output_label = QLabel(self)
        
        self.vbox = QVBoxLayout()
        
        self.init_ui()
        
    def init_ui(self):
        
        #Adjust name and icon of the window
        self.setWindowTitle("Wetter App")
        self.setWindowIcon(QIcon("pictures//app_icon.png"))
        self.setGeometry(0,0,350,200)
        self.center_window()
        
        #Add Widgets to vertical vox layout
        self.vbox.addWidget(self.input_field)
        self.vbox.addWidget(self.button_search)
        
        #Set vertical box layout
        self.setLayout(self.vbox)
        
        #Set window name (CSS ID)
        self.setObjectName("weatherApp")
        
        #Set widgets name (CSS ID)
        self.input_field.setObjectName("input_field")
        self.button_search.setObjectName("button_search")
        
        #Connect event to the button
        self.button_search.clicked.connect(self.get_user_input_start_api)
        
        #Apply shadow to specific widgets
        for child in self.findChildren(QWidget):
            if (child.objectName() == "input_field" or child.objectName() == "button_search"):
                shadow = QGraphicsDropShadowEffect()
                shadow.setBlurRadius(50)
                child.setGraphicsEffect(shadow)
        
        #Set the sytlesheet for all components
        self.setStyleSheet(Style_Sheet.css_content)
        
    def get_user_input_start_api(self):
        #Set inital window size and center window
        self.setGeometry(0,0,550,900)
        self.center_window()
        
        #Convert user input into string
        self.user_input = self.input_field.text()
        #start api request with user input
        self.weather_data = Weather_api.convert_name_in_location(self.user_input)
        self.forecast_data = Weather_api.request_forecast()
        #print(self.forecast_data)
        #print(json.dumps(self.forecast_data,indent=4))
        self.display_forecast()
        
        
        #check if response is empty
        if(not self.weather_data):
            
            #set diffrent css style
            self.input_field.setObjectName("input_field_wrong")
            self.setStyleSheet(Style_Sheet.css_content)
        else:
            #Allways set object name and stylesheet
            self.input_field.setObjectName("input_field")
            self.setStyleSheet(Style_Sheet.css_content)
            
            #Extract necessary data from response object
            self.extrtact_weather_data(self.weather_data)
            
            #Set Object names and center content
            self.time_label.setObjectName("time_label")
            self.time_label.setAlignment(Qt.AlignCenter)
            
            self.output_label.setObjectName("output_label")
            self.output_label.setAlignment(Qt.AlignCenter)
            
            #Apply shadow to the output label
            shadow = QGraphicsDropShadowEffect()
            shadow.setBlurRadius(30)
            self.output_label.setGraphicsEffect(shadow)
            
            #Add remaining widgets to the vertical box layout
            self.vbox.addWidget(self.weather_pic)
            self.vbox.addWidget(self.time_label)
            self.vbox.addWidget(self.output_label)
            
            #Set vertical box layout
            self.setLayout(self.vbox)
            
            #Construct the output string
            string = f"""Aktuelles Wetter für {self.user_input}\nWetter: {self.weather_data["description"]}\nTemperatur: {self.weather_data["temp"]:.1f} C° | Gefühlt: {self.weather_data["feels_like"]:.1f} C°\nMinimal: {self.weather_data["temp_min"]:.1f} C° und maximal {self.weather_data["temp_max"]:.1f} C°\nLuftfeuchtigkeit: {self.weather_data["humidity"]} %"""
            
            #Set string into output text
            self.output_label.setText(string)
            
            #Set calculated time
            self.time_label.setText(self.get_local_time())
            self.select_weather_pic()
            
    def extrtact_weather_data(self,data=dict) -> dict:
        #Extract system data from response data
        dict_data = data["sys"] # type: ignore
        
        #convert response list [{}] into dictonary
        converted_dic = {k: v for (k,v) in data["weather"][0].items()} # type: ignore
    
        #Update extracted data 
        dict_data.update(converted_dic)
        dict_data.update(data["main"]) # type: ignore
        dict_data["timezone"] = data["timezone"] # type: ignore
        
        #Initialize extracted data
        self.weather_data = dict_data
        
    def select_weather_pic(self):
        #Selcet correct weather picture based on retrieved weather codes 
        if(200 <= self.weather_data["id"] <= 232):
            self.change_gui_appearance("pictures//lightning_bolt.png","weatherApp_DarkCloud")
              
        elif(300 <= self.weather_data["id"] <= 321 or 520 <= self.weather_data["id"] <= 531):
            self.change_gui_appearance("pictures//heavy_rain.png","weatherApp_Rain")
            
        elif (500 <= self.weather_data["id"] <=504):
            # check if neight mode picture is necessary
            if(self.is_night()):
                self.change_gui_appearance("pictures//rain_night.png","weatherApp_LightCloud")
            else:
                self.change_gui_appearance("pictures//rain.png","weatherApp_cloud_sun")
             
        elif(self.weather_data["id"]== 511 or 600<= self.weather_data["id"]<= 622):
            self.change_gui_appearance("pictures//snow.png","weatherApp_LightCloud")
            
        elif(701 <= self.weather_data["id"] <= 781):
            if(self.is_night()):
                self.change_gui_appearance("pictures//haze_night.png","weatherApp_LightCloud")
            else:
                self.change_gui_appearance("pictures//haze.png","weatherApp_cloud_sun")
              
        elif(self.weather_data["id"] == 800):
            if(self.is_night()):
                self.change_gui_appearance("pictures//moon.png","weatherApp_LightCloud")
            else:
                self.change_gui_appearance("pictures//sun.png","weatherApp_Sun")
                    
        elif(self.weather_data["id"] == 801):
            if(self.is_night()):
                self.change_gui_appearance("pictures//cloudy_night.png","weatherApp_LightCloud")
            else:
                self.change_gui_appearance("pictures//cloudy.png","weatherApp_cloud_sun")
                
        elif(self.weather_data["id"] == 802):
            self.change_gui_appearance("pictures//cloud_computing.png","weatherApp_LightCloud")
            
        elif(803 <= self.weather_data["id"] <= 804):
            self.change_gui_appearance("pictures//clouds.png", "weatherApp_DarkCloud")
            
        #Apply shadow to all weather pictures
        weather_shadow = QGraphicsDropShadowEffect()
        weather_shadow.setBlurRadius(20)
        self.weather_pic.setGraphicsEffect(weather_shadow)
    
    def change_gui_appearance(self, path=str, css_ID=str):
            
        #Initialize QPixmap and set pixmap to Qlabel
        pixmap = QPixmap(path)
        self.weather_pic.setPixmap(pixmap)
        #Scale Pixmap to the size of the Qlabel
        self.weather_pic.setScaledContents(True)
            
        #Change CSS ID and set the changed stylesheet
        self.setObjectName(css_ID)
        self.setStyleSheet(Style_Sheet.css_content)
    
    def is_night(self) -> bool:
        #Get current time in unix format
        current_time = int(time.time())
        #Check if current time lies between sunrise and sunset of requested location
        if(current_time >= self.weather_data["sunrise"] and current_time <= self.weather_data["sunset"]): # type: ignore
            return False
        else:
            return True
    
    def get_local_time(self) -> str:
        #Get current utc time
        utc_time = datetime.now(tz.utc)
        #Convert utc time into unix timestamp
        utc_unix_timestamp = utc_time.timestamp()
        #Subtract time difference between local time and utc time
        utc_unix_timestamp = utc_unix_timestamp - 3600#!Only CET-Times
        #Calculate time of searched location
        unix_time_of_location = int(utc_unix_timestamp + self.weather_data["timezone"]) # type: ignore
        #Convert calculated unix timestamp into normal time 
        time_location = datetime.fromtimestamp(unix_time_of_location).strftime("%H:%M")
        time_location = f"{time_location} Uhr"
        
        return time_location
    
    def display_forecast(self):
        five_day_list = self.forecast_data["list"]
        five_day_data = []
        for dic in five_day_list[::8]:
            five_day_data.append(dic)
        
        for dic in five_day_data:
            nessesary_data = {}
            converted_dic = {k: v for (k,v) in dic["weather"][0].items()} # type: ignore
            nessesary_data.update(converted_dic)
            nessesary_data.update(dic["main"])
            nessesary_data["dt"] = dic["dt"]
            
            time_string_date = datetime.fromtimestamp(nessesary_data["dt"]).strftime("%d.%m.%Y")
            time_string_time = datetime.fromtimestamp(nessesary_data["dt"]).strftime("%H:%M")
            
        
        
        
        
        
            
            
        

    def center_window(self):
        #Window into the center of the screen
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
      
    def start_gui():
        app = QApplication(syst.argv)
        window = WeatherApp()
        window.show()
        syst.exit(app.exec_())