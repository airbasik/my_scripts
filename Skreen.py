# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 09:48:16 2020

@author: Us
"""

from tkinter import *
from PIL import ImageGrab
import time

root=Tk()
root.geometry('270x160')
root.title('PyScreen')


def screen():
    NumberShots = int(e1.get()) #число снимков

    TimeDelay = float(e2.get()) #задержка между снимками

    i = 0

    WayFile = str(e3.get()) + '\\' + str(e4.get()) + '{}.png' #путь сохранения файла
    
    while i < NumberShots:

        snapshot = ImageGrab.grab() #скриншот
        save_path = WayFile.format(i) #путь сохранения файла
        snapshot.save(save_path) #сохранение файла
        time.sleep(TimeDelay) #задержка времени
        i = i + 1
        
#print(i)    

    
e1=Entry(width=20, justify='center')
e1.grid(row=0, column=0, padx=5, pady=5)

e2=Entry(width=20, justify='center')
e2.grid(row=1, column=0, padx=5, pady=5)

e3=Entry(width=20, justify='center')
e3.grid(row=2, column=0, padx=5, pady=5)

e4=Entry(width=20, justify='center')
e4.grid(row=3, column=0, padx=5, pady=5)

b=Button(text='Запустить', command=screen, cursor='pirate')
b.grid(row=4, column=1, padx=5, pady=5)

l1 = Label(text='Количество снимков')
l1.grid(row=0, column=1, padx=5, pady=5)

l2 = Label(text='Интервал снимков')
l2.grid(row=1, column=1, padx=5, pady=5)

l3 = Label(text='Путь сохранения')
l3.grid(row=2, column=1, padx=5, pady=5)

l4 = Label(text='Имя величины')
l4.grid(row=3, column=1, padx=5, pady=5)

lb = Label(text='>>>')
lb.grid(row=4, column=0, padx=5, pady=5)

root.mainloop()




