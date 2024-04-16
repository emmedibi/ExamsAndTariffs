from tkinter import Tk
from gui.helpers import createForm


## THE MAIN FILE ##

print('The application is started')
print('Compile the window with the data requested')


ws =Tk()
ws.title('TariffFileCreation')
ws.geometry('250x300')
ws.configure(bg='#dddddd')

createForm(ws)
