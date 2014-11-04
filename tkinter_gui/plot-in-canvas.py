#!/usr/bin/python
# plot of log line
from Tkinter import *
import math
def particleCount(decay, p0, time):
    p = (p0*math.e)**(-(decay*time))
    return (p)

# define root window
root = Tk()
root.title("Radioactive Decay Graph")

# create frame to put control buttons onto
frame = Frame(root, bg='grey', width=400, height=40)
frame.pack(fill='x')
button1 = Button(frame, text='Button1')
button1.pack(side='left', padx=10)
button2 = Button(frame, text='Button2')
button2.pack(side='left')

# set canvas properties
width = 400
height = 400
center = height*(5/6)
x_increment = 1

# invoke canvas
c = Canvas(root, width=width, height=height, bg='black')
c.pack()

# add string
str1 = "Logarithmic decay graph"
c.create_text(10, 20, anchor=SW, text=str1)

# line width stretch
x_factor = 1

# line height stretch
y_amplitude = -300
center_line = c.create_line(0, center +1, width, center+1, fill='green')
coordinates = []
coord = []

for x in range(0, 600):
    # x coordinates
    coord.append((x * x_increment) * x_factor)
    # y coordinates
    y = particleCount((1.16*(10**-3)), (5*(10**6)), x)
    coord.append((y * y_amplitude) + center)
    coordinates.append(coord)
    coord = []

log_line = c.create_line(coordinates, fill='red')
root.mainloop()
