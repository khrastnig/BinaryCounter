#!/usr/bin/env python3
# 2021 nr@bulme.at
#Karoline Hrastnig
#12.10.2022
#Binary Counter

from gpiozero import Button, LED, LEDBoard
from PyQt5.QtCore import Qt, QObject, pyqtSignal
from PyQt5.QtWidgets import (QWidget, QLCDNumber,
    QVBoxLayout, QApplication)

DOWN_PIN = 22
RESET_PIN = 27
UP_PIN = 17
leds=[LED(25),LED(24),LED(23),LED(18)]

class QtButton(QObject):
    changed = pyqtSignal()                              # funktion signal -> emit()

    def __init__(self, pin):
        super().__init__()
        self.button = Button(pin) 
        self.button.when_pressed = self.gpioChange      #rufe gpioChange auf wenn der Button gedrückt wird       

    def gpioChange(self):
        self.changed.emit()                             #Änderung wenn Signal 

class Counter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()
        self.count = 0

    def initUi(self):
        self.lcd = QLCDNumber()
        self.lcd.display(0)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lcd)                       #Anzeige

        self.setLayout(vbox)                           #Anzeigefeld
        self.setMinimumSize(400, 200)
        self.setWindowTitle('Counter')                 #Beschriftung Anzeigefeld
        self.show()
        
    def setLed (self, count):                          #Funktion um die Leds anzusteuern
        for i, led in enumerate(leds):
            if (count & 1<<i):                
                led.on()
            else:                
                led.off()          
    
    def countUp(self):
        if self.count == 15:
             self.count = -1   
        self.count += 1
        self.lcd.display(self.count)                    #Gibt den Wert in self.lcd.display aus also in der Anzeige
        self.setLed(self.count)                         #Gibt den Wert in am Ledboard aus
                
    def countDown(self):
        if self.count == 0:
             self.count = 16
        self.count -= 1
        self.lcd.display(self.count)
        self.setLed(self.count)
                
    def countReset(self):
        self.count = 0
        self.lcd.display(self.count)
        self.setLed(self.count)
        
if __name__ ==  '__main__':
    app = QApplication([])
    gui = Counter()                                     #greift auf die Klasse Counter zu  
    buttonUp = QtButton(UP_PIN)                         #bindet den Button UP_PIN aus der QtButtonklasse an buttonUp
    buttonUp.changed.connect(gui.countUp)                #bindet buttonUp , bei Veränderung (Funktion changed) an die Funktion countUp aus der Counterklasse 
    buttonDown = QtButton(DOWN_PIN)
    buttonDown.changed.connect(gui.countDown)
    buttonReset = QtButton(RESET_PIN)
    buttonReset.changed.connect(gui.countReset)
    app.exec_()
    