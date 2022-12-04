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
from pydub import AudioSegment

import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import os.path
from scipy.io import wavfile
import pandas as pd

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
        #Create Wave File
        if(self.selectedDevice == "Siri"):
            return AudioSegment.from_wav('./sounds/Hey_Siri.wav')
        elif(self.selectedDevice == "Google"):
            return AudioSegment.from_wav('./sounds/Hey_Google.wav')
        elif(self.selectedDevice == "Amazon"):
            return AudioSegment.from_wav('./sounds/Hey_Alexa.wav')
        elif(self.selectedDevice == "Android"):
            return AudioSegment.from_wav('./sounds/Hey_Google.wav')
        else:   
            return AudioSegment.from_wav('./sounds/Hey_Siri.wav')

    def createCSV(self, input):
        samrate, data = wavfile.read('./sounds/result.wav')
        wavData = pd.DataFrame(data)
        wavData.to_csv(input, mode='w')


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
            #Create Wave File
            sound1 = self.playDevice()
            sound2 = AudioSegment.from_wav("./sounds/weather.wav")
            combined_sounds = sound1 + sound2
            combined_sounds.export("./sounds/result.wav", format="wav")

            #Create CSV file
            self.createCSV("weather.csv")
        # Time 
        if btnName == "time":
            #Create Wave File
            sound1 = self.playDevice()
            sound2 = AudioSegment.from_wav("./sounds/time.wav")
            combined_sounds = sound1 + sound2
            combined_sounds.export("./sounds/result.wav", format="wav")

            #Create CSV file
            self.createCSV("time.csv")
        #Lights
        if btnName == "lights":
            #Create Wave File
            sound1 = self.playDevice()
            sound2 = AudioSegment.from_wav("./sounds/lights.wav")
            combined_sounds = sound1 + sound2
            combined_sounds.export("./sounds/result.wav", format="wav")

            #Create CSV file
            self.createCSV("lights.csv")
        #Spotify
        if btnName == "spotify":
            #Create Wave File
            sound1 = self.playDevice()
            sound2 = AudioSegment.from_wav("./sounds/spotify.wav")
            combined_sounds = sound1 + sound2
            combined_sounds.export("./sounds/result.wav", format="wav")

            #Create CSV file
            self.createCSV("spotify.csv")
        #Timer
        if btnName == "timer":
            #Create Wave File
            sound1 = self.playDevice()
            sound2 = AudioSegment.from_wav("./sounds/timer.wav")
            combined_sounds = sound1 + sound2
            combined_sounds.export("./sounds/result.wav", format="wav")

            #Create CSV file
            self.createCSV("timer.csv")
        #Emergency
        if btnName == "emergency":
            #Create Wave File
            sound1 = self.playDevice()
            sound2 = AudioSegment.from_wav("./sounds/emergency.wav")
            combined_sounds = sound1 + sound2
            combined_sounds.export("./sounds/result.wav", format="wav")

            #Create CSV file
            self.createCSV("emergency.csv")
        #Joke
        if btnName == "joke":
            #Create Wave File
            sound1 = self.playDevice()
            sound2 = AudioSegment.from_wav("./sounds/joke.wav")
            combined_sounds = sound1 + sound2
            combined_sounds.export("./sounds/result.wav", format="wav")

            #Create CSV file
            self.createCSV("joke.csv")

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

            # Sampling frequency
            freq = 44100
            
            # Recording duration
            duration = 5

            # Start recorder with the given values 
            # of duration and sample frequency
            recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
            
            # Record audio for the given number of seconds
            sd.wait()
            
            # Convert the NumPy array to audio file
            wv.write("./sounds/result.wav", recording, freq, sampwidth=2)

        #Play Back
        if btnName == "play_back":
            self.createCSV("playback.csv")

        

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
