from tkinter import *
from tkinter.ttk import *
import configparser
from helpers import *

# Temp for Button
from tkinter import messagebox

window = Tk()
notebook = Notebook(window, width=800, height=480, padding=0)

# canvas = Canvas(window, width=800, height=480, bg="White")
# canvas.pack()

def newVessel():
    msg = messagebox.showinfo( "Hello Python", "Hello World")

def drawVessels(vessels):
    for vessel in vessels:
        notebook.add(Frame(notebook), text = vessel, padding=10)
    notebook.pack(expand=True, fill='both')

def initVessels():
    ''' Read the configuration file at settings.ini. Display new vessel interface if there's no vessels,
    or iterate over the vessels and draw their respective interfaces.
    '''
    settings = configparser.ConfigParser()
    settings._interpolation = configparser.ExtendedInterpolation()
    settings.read('settings.ini')

    if len(settings.sections()) > 0:
        attributes = ['gpio', 'cycle', 'pkf', 'pti', 'ptd']
        vessels = {}
        for vessel in settings.sections():
            vessels[vessel] = {}
            for attribute in attributes:
                vessels[vessel][attribute] = settings.get(vessel, attribute)
        print(vessels)
        drawVessels(vessels)

    else:
        print("NO WESSELS")


# btnNewVessel = Button( window, text = "New Vessel", command = newVessel )
# btnNewVessel.place(x=50,y=50)

# notebook.place(x=0,y=0)

# window.attributes("-fullscreen",True)

initVessels()

window.mainloop()
