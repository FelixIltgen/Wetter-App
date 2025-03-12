from weather_api import *
from style_sheet import *

import sys as syst
import time

from datetime import timezone as tz
from datetime import datetime

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QDesktopWidget, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QGraphicsDropShadowEffect, QDialog, QGroupBox
from PyQt5.QtGui import QIcon, QPixmap 
from PyQt5.QtCore import Qt, QRect
from PyQt5 import QtWidgets

class WeatherApp(QDialog):
    
    user_input = ""
    weather_data = {}
    forecast_data = {}
    
    def __init__(self):
        super(WeatherApp,self).__init__()
        #Initialise GUI components
        self.input_field = QLineEdit("Herbolzheim",self)
        self.button_search = QPushButton("Wetter suchen 🔎",self)
        self.weather_pic = QLabel(self)
        
        self.pixmap = QPixmap("")
        self.time_label = QLabel(self)
        self.output_label = QLabel(self)
        self.button_forecast = QPushButton()
        
        self.vbox = QVBoxLayout()
        
        self.init_ui()
        
    def init_ui(self):
    
        #Adjust name and icon of the window
        widget.setGeometry(0,0,350,0)
        self.center_window()
        widget.setWindowTitle("Wetter App")
        widget.setWindowIcon(QIcon("pictures//app_icon.png"))
        
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
        widget.setGeometry(0,0,300,850)
        self.center_window()
        #Convert user input into string
        self.user_input = self.input_field.text()
        
        #start api request with user input
        self.weather_data = Weather_api.convert_name_in_location(self.user_input)
        self.forecast_data = Weather_api.request_forecast()
    
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
            
            #Apply Text content & CSS ID to the forecast button
            self.button_forecast.setText("Wetterbericht")
            self.button_forecast.setObjectName("button_forecast")
            
            
            
            #Add remaining widgets to the vertical box layout
            self.vbox.addWidget(self.weather_pic)
            self.vbox.addWidget(self.time_label)
            self.vbox.addWidget(self.output_label)
            self.vbox.addWidget(self.button_forecast)
            
            #Set vertical box layout
            self.setLayout(self.vbox)
            #Construct the output string
            self.weather_pic.setObjectName("wetterbild")
            
            string = f"""Aktuelles Wetter für {self.user_input}\nWetter: {self.weather_data["description"]}\nTemperatur: {self.weather_data["temp"]:.1f} C° | Gefühlt: {self.weather_data["feels_like"]:.1f} C°\nMinimal: {self.weather_data["temp_min"]:.1f} C° und maximal {self.weather_data["temp_max"]:.1f} C°\nLuftfeuchtigkeit: {self.weather_data["humidity"]} %"""
            
            #Set string into output text
            self.output_label.setText(string)
            
            #Set calculated time
            self.time_label.setText(self.get_local_time())
            self.select_weather_pic()
            
            self.button_forecast.clicked.connect(self.switch_screen)
                  
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
            necessary_data = {}
            converted_dic = {k: v for (k,v) in dic["weather"][0].items()} # type: ignore
            necessary_data.update(converted_dic)
            necessary_data.update(dic["main"])
            necessary_data["dt"] = dic["dt"]
            
            time_string_date = datetime.fromtimestamp(necessary_data["dt"]).strftime("%d.%m.%Y")
            time_string_time = datetime.fromtimestamp(necessary_data["dt"]).strftime("%H:%M")
            
            print(f"Wetter am {time_string_date} um {time_string_time}")
            print("")
            print(f"Temperatur: {necessary_data["temp"]:.1f} C°")
            print(f"{necessary_data["description"]} Icon: {necessary_data["id"]}")
            print("****************************************")
            
    def center_window(self):
        #Window into the center of the screen
        qtRectangle = widget.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        widget.move(qtRectangle.topLeft())
    
    def switch_screen(self):
        print("Screen Zwei")
        screen_two = Screen_two()
        widget.addWidget(screen_two)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Screen_two(QDialog):
    
    def __init__(self):
        super().__init__()
        self.load_UI()
        
    def load_UI(self):
        self.vbox = QVBoxLayout()
        self.test_button = QPushButton("Zurück",self)
        self.test_button.setObjectName("button_back")
        self.setObjectName("weatherApp")

        for i in range(5):
            self.creat_layout_components()
            self.box.setObjectName("test_label")
            self.vbox.addWidget(self.box)
        else:
            self.vbox.addWidget(self.test_button)
            self.setLayout(self.vbox)
            self.test_button.clicked.connect(self.switch_screen)
            self.setStyleSheet(Style_Sheet.css_content)
        
    def creat_layout_components(self):
        self.box = QGroupBox()
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()
        weather_pic = QLabel("Wetterbild")
        weather_date = QLabel("Datum")
        weather_info = QLabel("Wetterinformation")
        weather_temp = QLabel("Wettertemperatur")
        content_list = [weather_date,weather_info,weather_temp]
        hbox.addWidget(weather_pic,4)
        weather_pic.setObjectName("content")
        
        for content in content_list:
            content.setObjectName("content")
            vbox.addWidget(content)
        else:
            hbox.addLayout(vbox,12)
            
        self.box.setLayout(hbox)
        
            
    def switch_screen(self):
        widget.setCurrentIndex(widget.currentIndex()-1)
        
 
if __name__ == "__main__":
    app = QApplication(syst.argv)
    widget = QtWidgets.QStackedWidget()
    window = WeatherApp()
    widget.addWidget(window)
    widget.show()
    syst.exit(app.exec_())      
    
        
        

