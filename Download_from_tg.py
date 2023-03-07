from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
import sys
import configparser
from dw_func import download_image_from_file
    

# Подкласс QMainWindow для настройки главного окна приложения
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image downloader")
        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.start_download)
        
        layout = QVBoxLayout()
        layout.addWidget(button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def start_download(self):
        settings = configparser.ConfigParser()
        settings.read('settings.ini')
        filename = settings['DEFAULT']['filename']        
        download_image_from_file(filename) 

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()