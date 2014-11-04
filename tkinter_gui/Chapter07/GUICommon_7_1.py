# 
#  GUI Common Class definitions
#

from Common_9_1 import *

class GUICommon:
    def turnon(self):
        self.status = STATUS_ON
        if not self.blink: self.update()

    def turnoff(self):
        self.status = STATUS_OFF
        if not self.blink: self.update()

    def alarm(self):
        self.status = STATUS_ALARM
        if not self.blink: self.update()

    def warn(self):
        self.status = STATUS_WARN
        if not self.blink: self.update()

    def set(self, color):
        self.status       = STATUS_SET
        self.specialColor = color
        self.update()

    def blinkon(self):
        if not self.blink:
            self.blink   = 1
            self.onState = self.status
            self.update()

    def blinkoff(self):
        if self.blink:
            self.blink   = 0
            self.status  = self.onState
            self.onState = None
            self.on=0
            self.update()

    def blinkstate(self, blinkstate):
        if blinkstate:
            self.blinkon()
        else:
            self.blinkoff()

# The following define drawing vertices for various 
# graphical elements

ARROW_HEAD_VERTICES = [
     ['x-d', 'y-d', 'x',   'y+d', 'x+d', 'y-d', 'x-d', 'y-d'],
     ['x',   'y-d', 'x-d', 'y+d', 'x+d', 'y+d', 'x',   'y-d'],
     ['x-d', 'y-d', 'x+d', 'y',   'x-d', 'y+d', 'x-d', 'y-d'],
     ['x-d', 'y',   'x+d', 'y+d', 'x+d', 'y-d', 'x-d', 'y'  ]]

