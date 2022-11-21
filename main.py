# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

import sys
import os
import platform
from playsound import *
import time

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None
script_dir = os.path.dirname(__file__)

time_to_sleep = 0

class MainWindow(QMainWindow):
    selectedDevice = ""

    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui
        


        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "Silent Speech"
        description = "Inaudible Sound Attacks Against S.A.G.A (Siri, Amazon, Google, Android)"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_widgets.clicked.connect(self.buttonClick)
        widgets.btn_new.clicked.connect(self.buttonClick)
        widgets.weather.clicked.connect(self.buttonClick)
        widgets.time.clicked.connect(self.buttonClick)
        widgets.lights.clicked.connect(self.buttonClick)
        widgets.spotify.clicked.connect(self.buttonClick)
        widgets.timer.clicked.connect(self.buttonClick)
        widgets.emergency.clicked.connect(self.buttonClick)
        widgets.joke.clicked.connect(self.buttonClick)
        widgets.radioButton.clicked.connect(self.buttonClick)
        widgets.radioButton_2.clicked.connect(self.buttonClick)
        widgets.radioButton_3.clicked.connect(self.buttonClick)
        widgets.radioButton_4.clicked.connect(self.buttonClick)
        widgets.record.clicked.connect(self.buttonClick)
        widgets.play_back.clicked.connect(self.buttonClick)
        widgets.stop_record.clicked.connect(self.buttonClick)



        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////

    def playDevice(self):
        print("selected device: ", self.selectedDevice)
        if self.selectedDevice == "":
            pass        
        elif self.selectedDevice == "Siri":
            print("in loop")
            playsound('./sounds/Hey_Siri.wav')
        elif self.selectedDevice == "Google":
            playsound('./sounds/Hey_Google.wav')
        elif self.selectedDevice == "Amazon":
            playsound('./sounds/Hey_Alexa.wav')
        elif self.selectedDevice == "Android":
            playsound('./sounds/Hey_Google.wav')
        else:
            pass


    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW WIDGETS PAGE
        if btnName == "btn_widgets":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_new":
            widgets.stackedWidget.setCurrentWidget(widgets.new_page) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        # Weather 
        if btnName == "weather":
            print("Weather")
            self.playDevice()
            time.sleep(time_to_sleep)
            playsound('./sounds/weather.wav')
        # Time 
        if btnName == "time":
            print("Time")
            self.playDevice()
            time.sleep(time_to_sleep)
            playsound('./sounds/time.wav')
        #Lights
        if btnName == "lights":
            print("Lights")
            self.playDevice()
            time.sleep(time_to_sleep)
            playsound('./sounds/lights.wav')
        #Spotify
        if btnName == "spotify":
            print("Spotify")
            self.playDevice()
            time.sleep(time_to_sleep)
            playsound('./sounds/spotify.wav')
        #Timer
        if btnName == "timer":
            print("Timer")
            self.playDevice()
            time.sleep(time_to_sleep)
            playsound('./sounds/timer.wav')
        #Emergency
        if btnName == "emergency":
            print("Emergency")
            self.playDevice()
            time.sleep(time_to_sleep)
            playsound('./sounds/emergency.wav')
        #Joke
        if btnName == "joke":
            print("Joke")
            self.playDevice()
            time.sleep(time_to_sleep)
            playsound('./sounds/joke.wav')

        #Siri
        if btnName == "radioButton_2":
            print("Siri")
            self.selectedDevice = "Siri"
        #Amazon
        if btnName == "radioButton_4":
            print("Amazon")
            self.selectedDevice = "Amazon"
        #Google
        if btnName == "radioButton_3":
            print("Google")
            self.selectedDevice = "Google"
        #Android
        if btnName == "radioButton":
            print("Android")
            self.selectedDevice = "Android"

        #Record
        if btnName == "record":
            print("Recording")

        #Stop Recording
        if btnName == "stop_record":
            print("Recording Stopped")

        #Play Back
        if btnName == "play_back":
            print("Play Backing")

        

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec_())
