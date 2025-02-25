from weather_api import *
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QDesktopWidget
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wetter App")
        self.setWindowIcon(QIcon("pictures//app_icon.png"))
        self.setGeometry(0,0,600,800)
        self.setStyleSheet("background-color: #62c8f0")

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 40))
        label.setGeometry(0, 0, 600, 100)
        label.setStyleSheet("color: #292929;"
                                           "background-color: #6fdcf7;"
                                           "font-weight: bold;"
                                           "text-decoration: underline;")
        weather_pic = QLabel(self)
        weather_pic.setGeometry(0,0,100,100)
        pixmap = QPixmap("pictures//app_icon.png")
        weather_pic.setPixmap(pixmap)
        weather_pic.setScaledContents(True)
        weather_pic.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        weather_pic.setGeometry((self.width()-weather_pic.width())//2,(self.height()-weather_pic.height()-200)//2,weather_pic.width(),weather_pic.height())
    

        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

    
    def start_gui():
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())