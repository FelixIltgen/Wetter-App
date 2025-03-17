from weather_api import *
from style_sheet import *

import sys as syst
import time

from datetime import timezone as tz
from datetime import datetime

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QDesktopWidget, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QGraphicsDropShadowEffect, QDialog, QGroupBox
from PyQt5.QtGui import QIcon, QPixmap, QFont, QFontDatabase
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets

class WeatherApp(QDialog):
    
    user_input = ""
    weather_data = {}
    screen_count = 0
    screen_two = ""
    
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
        widget.setGeometry(0,0,350,230)
        self.center_window()
        widget.setWindowTitle("Wetter App")
        widget.setWindowIcon(QIcon("pictures//app_icon.png"))
        
        #Set font
        font_id = QFontDatabase.addApplicationFont("fonts//DS-DIGIT.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        self.digital_clock_font = QFont(font_family)
        
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
        widget.setGeometry(0,0,480,950)
        self.center_window()
        #Convert user input into string
        self.user_input = self.input_field.text()
        Screen_two.user_input = self.user_input
        
        #start api request with user input
        self.weather_data = Weather_api.convert_name_in_location(self.user_input)
        
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
            
            #Set sunset and sunrise variables for second screen
            Screen_two.sunset = self.weather_data["sunset"]
            Screen_two.sunrise = self.weather_data["sunrise"]
            
            #Set Object names and center content
            self.time_label.setObjectName("time_label")
            self.time_label.setAlignment(Qt.AlignCenter)
            
            #Set the custom font
            self.time_label.setFont(self.digital_clock_font)
            
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
            
            #Connect function to the button
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
        Screen_two.css_id_screen_one = css_ID
            
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
        time_location = f"{time_location}"
        
        return time_location
           
    def center_window(self):
        #Window into the center of the screen
        qtRectangle = widget.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        widget.move(qtRectangle.topLeft())
    
    def switch_screen(self):
        #Check if a second screen already exists
        if (self.screen_count <= 0):
            #Create a new screen object
            self.screen_two = Screen_two()
            #Add the new object to the widget
            widget.addWidget(self.screen_two)
            #Increment the widget index to the new screen object
            widget.setCurrentIndex(widget.currentIndex()+1)
            #Increment screen count
            self.screen_count =+ 1
        else:
            #Remove existing screen object from the widget
            widget.removeWidget(self.screen_two)
            #Create a new screen object
            self.screen_two = Screen_two()
            #Add the new object to the widget
            widget.addWidget(self.screen_two)
            #Increment the widget index
            widget.setCurrentIndex(widget.currentIndex()+1)
              
class Screen_two(QDialog):
    forecast_data = {}
    extracted_data = []
    sunrise = int
    sunset = int
    user_input = ""
    css_id_screen_one = ""
    def __init__(self):
        super().__init__()
        self.forecast_data = Weather_api.request_forecast()
        self.load_UI()
        
    def load_UI(self):
        self.vbox = QVBoxLayout()
        self.test_button = QPushButton("Zurück",self)
        self.test_button.setObjectName("button_back")
        self.setObjectName(self.css_id_screen_one)
        self.extracted_data = self.display_forecast()

        for i in range(5):
            self.creat_layout_components(i,self.extracted_data[i]["id"])
            
            self.vbox.addWidget(self.box)
        else:
            self.vbox.addWidget(self.test_button)
            self.setLayout(self.vbox)
            self.test_button.clicked.connect(self.switch_screen)
            self.setStyleSheet(Style_Sheet.css_content)
        
    def creat_layout_components(self,index,weather_id):
        self.box = QGroupBox()
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()
        
        weather_pic = QLabel()
        Screen_two.select_weather_pic(weather_id,weather_pic,self.box,self)
        
        weather_date = QLabel(f"{self.extracted_data[index]["weekday"]}{self.extracted_data[index]["time_string_date"]} | {self.extracted_data[index]["time_string_time"]} Uhr")
        weather_info = QLabel("Wetter: "+self.extracted_data[index]["description"])
        weather_temp = QLabel(f"Temperatur: {self.extracted_data[index]["temp"]:.1f} C°")
        
        weather_date.setObjectName("weather_date")
        weather_info.setObjectName("weather_info")
        weather_temp.setObjectName("weather_temp")
        
        hbox.addWidget(weather_pic,4)
        content_list = [weather_date,weather_info,weather_temp]
        
        for content in content_list:
            #content.setObjectName("content")
            vbox.addWidget(content)
        else:
            hbox.addLayout(vbox,12)

        self.box.setLayout(hbox)
        
    def select_weather_pic(weather_id,weather_pic,box,self):
            #Selcet correct weather picture based on retrieved weather codes 
            if(200 <= weather_id <= 232):
                Screen_two.change_gui_appearance("pictures//pictures_x128//lightning_bolt_x128.png","weatherApp_DarkCloud_Forecast",weather_pic,box)
                
            elif(300 <= weather_id <= 321 or 520 <= weather_id <= 531):
                Screen_two.change_gui_appearance("pictures//pictures_x128//heavy_rain_x128.png","weatherApp_Rain_Forecast",weather_pic,box)
                
            elif (500 <= weather_id <=504):
                # check if neight mode picture is necessary
                if(Screen_two.is_night(self)):
                    Screen_two.change_gui_appearance("pictures//pictures_x128//rain_night_x128.png","weatherApp_LightCloud_Forecast",weather_pic,box)
                else:
                    Screen_two.change_gui_appearance("pictures//pictures_x128//rain_x128.png","weatherApp_cloud_sun_Forecast",weather_pic,box)
                
            elif(weather_id== 511 or 600<= weather_id<= 622):
                Screen_two.change_gui_appearance("pictures//pictures_x128//snow_x128.png","weatherApp_LightCloud_Forecast",weather_pic,box)
                
            elif(701 <= weather_id <= 781):
                if(Screen_two.is_night(self)):
                    Screen_two.change_gui_appearance("pictures//pictures_x128//haze_night_x128.png","weatherApp_LightCloud_Forecast",weather_pic,box)
                else:
                    Screen_two.change_gui_appearance("pictures//pictures_x128//haze_x128.png","weatherApp_cloud_sun_Forecast",weather_pic,box)
                
            elif(weather_id == 800):
                if(Screen_two.is_night(self)):
                    Screen_two.change_gui_appearance("pictures//pictures_x128//moon_x128.png","weatherApp_LightCloud_Forecast",weather_pic,box)
                    
                else:
                    Screen_two.change_gui_appearance("pictures//pictures_x128//sun_x128.png","weatherApp_Sun_Forecast",weather_pic,box)
                        
            elif(weather_id == 801):
                if(Screen_two.is_night(self)):
                    Screen_two.change_gui_appearance("pictures//pictures_x128//cloudy_night_x128.png","weatherApp_LightCloud_Forecast",weather_pic,box)
                else:
                    Screen_two.change_gui_appearance("pictures//pictures_x128//cloudy_x128.png","weatherApp_cloud_sun_Forecast",weather_pic,box)
                    
            elif(weather_id == 802):
                Screen_two.change_gui_appearance("pictures//pictures_x128//cloud_computing_x128.png","weatherApp_LightCloud_Forecast",weather_pic,box)
                
            elif(803 <= weather_id <= 804):
                Screen_two.change_gui_appearance("pictures//pictures_x128//clouds_x128.png", "weatherApp_DarkCloud_Forecast",weather_pic,box)
                
    def change_gui_appearance(path, css_ID,weather_pic,current_box):
            #Initialize QPixmap and set pixmap to Qlabel
            pixmap = QPixmap(path)
            weather_pic.setPixmap(pixmap)
            #Scale Pixmap to the size of the Qlabel
            weather_pic.setScaledContents(True)
            #Change CSS ID and set the changed stylesheet
            current_box.setObjectName(css_ID)
            
            weather_shadow = QGraphicsDropShadowEffect()
            weather_shadow.setBlurRadius(20)
            weather_pic.setGraphicsEffect(weather_shadow)
                
    def switch_screen(self):
        widget.setCurrentIndex(widget.currentIndex()-1)
    
    def display_forecast(self):
        five_day_list = self.forecast_data["list"]
        five_day_data = []
        data_list = []
        for dic in five_day_list[::8]:
            five_day_data.append(dic)
        
        for dic in five_day_data:
            necessary_data = {}
            converted_dic = {k: v for (k,v) in dic["weather"][0].items()} # type: ignore
            necessary_data.update(converted_dic)
            necessary_data.update(dic["main"])
            necessary_data["time_string_date"] = datetime.fromtimestamp(dic["dt"]).strftime("%d.%m.%Y")
            necessary_data["time_string_time"] = datetime.fromtimestamp(dic["dt"]).strftime("%H:%M")
            necessary_data["weekday"] = datetime.fromtimestamp(dic["dt"]).strftime("%a")
            
            match necessary_data["weekday"]:
                case "Sun":
                    necessary_data["weekday"] = "So."
                case "Mon":
                    necessary_data["weekday"] = "Mo."
                case "Tue":
                    necessary_data["weekday"] = "Di."
                case "Wed":
                    necessary_data["weekday"] = "Mi."
                case "Thu":
                    necessary_data["weekday"] = "Do."
                case "Fri":
                    necessary_data["weekday"] = "Fr."
                case "Sat":
                    necessary_data["weekday"] = "Sa."
            
            data_list.append(necessary_data)
        
        return data_list
    
    def is_night(self) -> bool:
        #Get current time in unix format
        current_time = int(time.time())
        #Check if current time lies between sunrise and sunset of requested location
        if(current_time >= self.sunrise and current_time <= self.sunset):
            return False
        else:
            return True
     
if __name__ == "__main__":
    app = QApplication(syst.argv)
    widget = QtWidgets.QStackedWidget()
    window = WeatherApp()
    widget.addWidget(window)
    widget.show()
    syst.exit(app.exec_())

#Wochentage hinzufügen