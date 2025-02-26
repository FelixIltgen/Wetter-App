from weather_api import *
from style_sheet import *
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QDesktopWidget, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    user_input = ""
    weather_data = {}
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wetter App")
        self.setWindowIcon(QIcon("pictures//app_icon.png"))
        self.setGeometry(0,0,600,800)
        
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        self.headline = QLabel("Überschrift",self)
        self.input_field = QLineEdit("Herbolzheim",self)
        self.button_search = QPushButton("Send",self)
        self.weather_pic = QLabel(self)
        #self.pixmap = QPixmap("")=> Kann glaube ichauch erst in funktion erstellt werden
        self.output_label = QLabel(self)
        

        self.init_ui()
        

    def init_ui(self):

        self.headline.setFont(QFont("Arial",40))
        self.headline.setGeometry(0, 0, self.width(), 100)
        #self.headline.setAlignment(Qt.AlignHCenter | Qt.AlignVCenters)
        self.headline.setStyleSheet("color: #292929;"
                                           "background-color: #6fdcf7;"
                                           "font-weight: bold;"
                                           "text-decoration: underline;")
        self.weather_pic.setGeometry(0,0,300,300)
        self.weather_pic.setGeometry((self.width()-self.weather_pic.width())//2,(self.height()-self.weather_pic.height())//2-50,self.weather_pic.width(),self.weather_pic.height())
        self.weather_pic.setStyleSheet("background-color: black;")

        self.input_field.setGeometry(150,130,200,50)
        self.button_search.setGeometry(350,130,100,50)
        self.output_label.setGeometry(100,550,400,200)
        self.output_label.setObjectName("output_label")
        
        self.button_search.clicked.connect(self.get_user_input_start_api)
        
        self.setStyleSheet(Style_Sheet.css_content)
        
    def get_user_input_start_api(self):
        self.user_input = self.input_field.text()
        self.weather_data = Weather_api.convert_name_in_location(self.user_input)
        self.extrtact_weather_data(self.weather_data)
        
        string = f"""Aktuelles Wetter für {self.user_input}
        Wetter: {self.weather_data["description"]}
        Aktuelle Temperatur: {self.weather_data["temp"]:.1f} C° | Gefühlt: {self.weather_data["feels_like"]:.1f} C°
        Minimal: {self.weather_data["temp_min"]:.1f} C° und maximal {self.weather_data["temp_max"]:.1f} C°
        Luftfeuchtigkeit: {self.weather_data["humidity"]} %"""
        self.output_label.setText(string)
    
    def extrtact_weather_data(self,data=dict) -> dict:
        data_list = [new_data for new_data in data if new_data == "weather" or new_data =="main"]
        dict_data = {k: v for (k,v) in data[data_list[0]][0].items()}
        dict_data.update(data[data_list[1]])
        self.weather_data = dict_data
      
    def start_gui():
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())