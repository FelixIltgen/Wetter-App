from weather_api import *
from style_sheet import *
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QDesktopWidget, QLineEdit, QPushButton, QVBoxLayout, QGraphicsDropShadowEffect
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    user_input = ""
    weather_data = {}
    
    def __init__(self):
        super().__init__()
        
        #Initialise GUI components
        self.input_field = QLineEdit("Herbolzheim",self)
        self.button_search = QPushButton("Wetter suchen 🔎",self)
        self.weather_pic = QLabel(self)
        self.pixmap = QPixmap("")
        self.output_label = QLabel(self)
        
        self.vbox = QVBoxLayout()
        
        self.init_ui()
        
    def init_ui(self):
        
        #Adjust name and icon of the Window
        self.setWindowTitle("Wetter App")
        self.setWindowIcon(QIcon("pictures//app_icon.png"))
        
        #Window into the center of the screen
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        
        #
        self.vbox.addWidget(self.input_field)
        self.vbox.addWidget(self.button_search)
        #vbox.addWidget(self.weather_pic)
        #vbox.addWidget(self.output_label)
        
        self.setLayout(self.vbox)
        
        #Set Window name (CSS ID)
        self.setObjectName("weatherApp")
        
        #Set Widgets name (CSS ID)
        self.input_field.setObjectName("input_field")
        self.button_search.setObjectName("button_search")
        
        
        #Connect event to the Button
        self.button_search.clicked.connect(self.get_user_input_start_api)
        
        #Apply shadow to specific widgets
        for child in self.findChildren(QWidget):
            if (child.objectName() == "input_field" or child.objectName() == "button_search"):
                shadow = QGraphicsDropShadowEffect()
                shadow.setBlurRadius(50)
                child.setGraphicsEffect(shadow)
        
        self.setStyleSheet(Style_Sheet.css_content)
        
    def get_user_input_start_api(self):
        self.user_input = self.input_field.text()
        self.weather_data = Weather_api.convert_name_in_location(self.user_input)
        self.extrtact_weather_data(self.weather_data)
        
        self.output_label.setObjectName("output_label")
        self.output_label.setAlignment(Qt.AlignCenter)
        
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(30)
        self.output_label.setGraphicsEffect(shadow)
        
        self.vbox.addWidget(self.weather_pic)
        self.vbox.addWidget(self.output_label)
        
        self.setLayout(self.vbox)
        
        string = f"""Aktuelles Wetter für {self.user_input}\nWetter: {self.weather_data["description"]}\nTemperatur: {self.weather_data["temp"]:.1f} C° | Gefühlt: {self.weather_data["feels_like"]:.1f} C°\nMinimal: {self.weather_data["temp_min"]:.1f} C° und maximal {self.weather_data["temp_max"]:.1f} C°\nLuftfeuchtigkeit: {self.weather_data["humidity"]} %"""
        
        self.output_label.setText(string)
        self.select_weather_pic()
    
    def extrtact_weather_data(self,data=dict) -> dict:
        data_list = [new_data for new_data in data if new_data == "weather" or new_data =="main" or new_data == "id"]
        dict_data = {k: v for (k,v) in data[data_list[0]][0].items()}
        dict_data.update(data[data_list[1]])
        self.weather_data = dict_data
    
    def select_weather_pic(self):
        if(200 <= self.weather_data["id"] <= 232):
            pixmap = QPixmap("pictures//lightning-bolt-.png")
            self.weather_pic.setPixmap(pixmap)
            self.weather_pic.setScaledContents(True)
            
        elif(300 <= self.weather_data["id"] <= 321 or 520 <= self.weather_data["id"] <= 531):
            pixmap = QPixmap("pictures//heavy-rain.png")
            self.weather_pic.setPixmap(pixmap)
            self.weather_pic.setScaledContents(True)
            
        elif (500 <= self.weather_data["id"] <=504):
            pixmap = QPixmap("pictures//rain.png")
            self.weather_pic.setPixmap(pixmap)
            self.weather_pic.setScaledContents(True)
            
        elif(self.weather_data["id"]== 511 or 600<= self.weather_data["id"]<= 622):
            pixmap = QPixmap("pictures//snow.png")
            self.weather_pic.setPixmap(pixmap)
            self.weather_pic.setScaledContents(True)
            
        elif(701 <= self.weather_data["id"] <= 781):
            pixmap = QPixmap("pictures//haze.png")
            self.weather_pic.setPixmap(pixmap)
            self.weather_pic.setScaledContents(True)
            
        elif(self.weather_data["id"] == 800):
            pixmap = QPixmap("pictures//sun.png")
            self.setObjectName("weatherApp2")
            self.weather_pic.setPixmap(pixmap)
            self.weather_pic.setScaledContents(True)
            self.setStyleSheet(Style_Sheet.css_content)
            
        elif(self.weather_data["id"] == 801):
            pixmap = QPixmap("pictures//cloudy.png")
            self.weather_pic.setPixmap(pixmap)
            self.weather_pic.setScaledContents(True)
            
        elif(self.weather_data["id"] == 802):
            pixmap = QPixmap("pictures//cloud-computing.png")
            self.weather_pic.setPixmap(pixmap)
            self.weather_pic.setScaledContents(True)
            
        elif(803 <= self.weather_data["id"] <= 804):
            pixmap = QPixmap("pictures//clouds.png")
            self.weather_pic.setPixmap(pixmap)
            self.weather_pic.setScaledContents(True)
        
        #Apply shadow to all weather pictures
        weather_shadow = QGraphicsDropShadowEffect()
        weather_shadow.setBlurRadius(20)
        self.weather_pic.setGraphicsEffect(weather_shadow)
        
    
      
    def start_gui():
        app = QApplication(sys.argv)
        window = WeatherApp()
        window.show()
        sys.exit(app.exec_())