"""
CUSTOM D&D RANDOMIZERS USING PYTHON & TKINTER
DEVELOPED BY fr1tZ
"""

import math
from tkinter import *
from monsters import *
from loot import *
from random import choice, randint

root = Tk(className=' D&D RANDOMIZERS BY fr1tZ ')
root.geometry("500x500")


def character():
	charWin = Tk(className = ' CHARACTERS ')
	charWin.geometry("500x500")



def zeros():
	moutWin = Tk(className = ' S-M ')
	moutWin.geometry("250x250")

	moutLabel = Label(moutWin, font="Times25")
	zeroChoice = choice(zeroList)
	zeroAmount = randint(1, 7)

	outStr = str(zeroChoice + " " + "x" + str(zeroAmount))
	moutLabel.config(text=outStr)

	moutLabel.pack()

def ones():
	moutWin = Tk(className = ' S-M ')
	moutWin.geometry("250x250")

	moutLabel = Label(moutWin, font="Times25")
	oneChoice = choice(oneList)
	oneAmount = randint(1, 8)

	outStr = str(oneChoice + " " + "x" + str(oneAmount))
	moutLabel.config(text=outStr)

	moutLabel.pack()


def monsters():
	monWin = Tk(className=' MONSTERS ')
	monWin.geometry("500x500")

	zeroB = Button(monWin, text="0 & Below", height=5, width=15, font='Times25', command=zeros)
	oneB = Button(monWin, text="One", height=5, width=15, font='Times25', command=ones)

	zeroB.grid(row=0, column=0)
	oneB.grid(row=1, column=0)
	monWin.mainloop()


monstersButton = Button(root, text="MONSTERS", height=5, width=15, font='Times25', command=monsters)
charactersButton = Button(root, text="CHARACTERS", height=5, width=15, font='Times25')
magicButton = Button(root, text="MAGIC", height=5, width=15, font='Times25')
lootButton = Button(root, text="LOOT", height=5, width=15, font='Times25')



monstersButton.grid(row=0, column=0)
charactersButton.grid(row=1, column=0)
magicButton.grid(row=2, column=0)
lootButton.grid(row=3, column=0)



if __name__ == "__main__":
	root.mainloop()