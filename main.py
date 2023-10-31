"""
CUSTOM D&D RANDOMIZERS USING PYTHON & TKINTER
DEVELOPED BY fr1tZ
"""

import math
from tkinter import *
from monsters import *
from magic import *
from random import choice, randint

root = Tk(className=' D&D RANDOMIZERS BY fr1tZ ')
root.geometry("500x500")

levelVar = 1





def randomizeLoot():
	# CURRENCY TYPES = CP, SP, EP, GP, PP

	global levelVar


	def getLeveledLoot():
		level = levelVar
		currencyRange = randint(1, 100)

		if 1 <= level <= 5:
			cp = randint(1, 250)
			sp = randint(1, 150)
			ep = randint(1, 75)
			gp = randint(1, 50)
			pp = randint(1, 8)

			copperOut = (str(cp) + " " + "CP")
			silverOut = (str(sp) + " " + "SP")
			electrumOut = (str(ep) + " " + "EP")
			goldOut = (str(gp) + " " + "GP")
			platinumOut = (str(pp) + " " + "PP")

			if currencyRange <= 20:
				lootLabel.config(text=copperOut)

			elif currencyRange <= 40:
				lootLabel.config(text=silverOut)

			elif currencyRange <= 60:
				lootLabel.config(text=electrumOut)

			elif currencyRange <= 80:
				lootLabel.config(text=goldOut)

			elif currencyRange <= 100:
				lootLabel.config(text=platinumOut)

		elif 5 < level <= 10:
			cp = randint(75, 500)
			sp = randint(75, 250)
			ep = randint(15, 92)
			gp = randint(1, 75)
			pp = randint(1, 14)

			copperOut = (str(cp) + " " + "CP")
			silverOut = (str(sp) + " " + "SP")
			electrumOut = (str(ep) + " " + "EP")
			goldOut = (str(gp) + " " + "GP")
			platinumOut = (str(pp) + " " + "PP")

			if currencyRange <= 20:
				lootLabel.config(text=copperOut)

			elif currencyRange <= 40:
				lootLabel.config(text=silverOut)

			elif currencyRange <= 60:
				lootLabel.config(text=electrumOut)

			elif currencyRange <= 80:
				lootLabel.config(text=goldOut)

			elif currencyRange <= 100:
				lootLabel.config(text=platinumOut)

		elif 10 < level <= 15:
			cp = randint(250, 1200)
			sp = randint(150, 600)
			ep = randint(150, 600)
			gp = randint(100, 175)
			pp = randint(10, 100)

			copperOut = (str(cp) + " " + "CP")
			silverOut = (str(sp) + " " + "SP")
			electrumOut = (str(ep) + " " + "EP")
			goldOut = (str(gp) + " " + "GP")
			platinumOut = (str(pp) + " " + "PP")

			if currencyRange <= 20:
				lootLabel.config(text=copperOut)

			elif currencyRange <= 40:
				lootLabel.config(text=silverOut)

			elif currencyRange <= 60:
				lootLabel.config(text=electrumOut)

			elif currencyRange <= 80:
				lootLabel.config(text=goldOut)

			elif currencyRange <= 100:
				lootLabel.config(text=platinumOut)

		elif 15 < level <= 20:
			cp = randint(500, 4500)
			sp = randint(500, 1000)
			ep = randint(500, 1000)
			gp = randint(375, 682)
			pp = randint(100, 500)

			copperOut = (str(cp) + " " + "CP")
			silverOut = (str(sp) + " " + "SP")
			electrumOut = (str(ep) + " " + "EP")
			goldOut = (str(gp) + " " + "GP")
			platinumOut = (str(pp) + " " + "PP")

			if currencyRange <= 20:
				lootLabel.config(text=copperOut)

			elif currencyRange <= 40:
				lootLabel.config(text=silverOut)

			elif currencyRange <= 60:
				lootLabel.config(text=electrumOut)

			elif currencyRange <= 80:
				lootLabel.config(text=goldOut)

			elif currencyRange <= 100:
				lootLabel.config(text=platinumOut)

		else:
			print("BROKEN SOMEHOW!?!??!?!?!")
			lootLabel.config(text="YOU BROKE ME SOMEHOW!")

	def addLevel():
		global levelVar
		levelVar = levelVar + 1
		if levelVar > 20:
			levelVar = 20

		levelLabel.config(text=levelVar)

	def subLevel():
		global levelVar
		levelVar = levelVar - 1

		if levelVar <= 0:
			levelVar = 1

		levelLabel.config(text=levelVar)

	currWin = Tk(className=' LOOT ')
	currWin.geometry("250x250")

	addLevelButton = Button(currWin, text="+ LEVEL", command=addLevel)
	subLevelButton = Button(currWin, text="- LEVEL", command=subLevel)

	levelLabel = Label(currWin, text="1", font="Times25")
	lootLabel = Label(currWin, text="LOOT", font="Times25")

	getLootButton = Button(currWin, text="GEN LOOT", font="Times25", command=getLeveledLoot)

	addLevelButton.pack(anchor=CENTER)
	subLevelButton.pack(anchor=CENTER)
	levelLabel.pack(anchor=CENTER)
	getLootButton.pack(anchor=CENTER)
	lootLabel.pack(anchor=CENTER)

	currWin.mainloop()

def character():
	charWin = Tk(className = ' NPCS ')
	charWin.geometry("500x500")




	charWin.mainloop()

def zeros():
	moutWin = Tk(className = ' S-M ')
	moutWin.geometry("250x150")

	moutLabel = Label(moutWin, font="Times25")
	zeroChoice = choice(zeroList)
	zeroAmount = randint(1, 7)

	outStr = str(zeroChoice + " " + "x" + str(zeroAmount))
	moutLabel.config(text=outStr)

	moutLabel.pack(anchor=CENTER)

def ones():
	moutWin = Tk(className = ' S-M ')
	moutWin.geometry("250x150")

	moutLabel = Label(moutWin, font="Times25")
	oneChoice = choice(oneList)
	oneAmount = randint(1, 8)

	outStr = str(oneChoice + " " + "x" + str(oneAmount))
	moutLabel.config(text=outStr)

	moutLabel.pack(anchor=CENTER)

def twos():
	moutWin = Tk(className = ' S-M ')
	moutWin.geometry("250x150")

	moutLabel = Label(moutWin, font="Times25")
	oneChoice = choice(twoList)
	oneAmount = randint(1, 8)

	outStr = str(oneChoice + " " + "x" + str(oneAmount))
	moutLabel.config(text=outStr)

	moutLabel.pack(anchor=CENTER)

def monsters():
	monWin = Tk(className=' MONSTERS ')
	monWin.geometry("500x500")

	zeroB = Button(monWin, text="0 & Below", height=5, width=15, font='Times25', command=zeros)
	oneB = Button(monWin, text="One", height=5, width=15, font='Times25', command=ones)
	twoB = Button(monWin, text="Two", height=5, width=15, font='Times25', command=twos)

	zeroB.grid(row=0, column=0)
	oneB.grid(row=1, column=0)
	twoB.grid(row=2, column=0)
	monWin.mainloop()

def magic():
	def randCommon():
		commons = choice(common)
		outLab.config(text=commons)

	def randUncommon():
		uncommons = choice(uncommon)
		outLab.config(text=uncommons)

	def randRare():
		rares = choice(rare)
		outLab.config(text=rares)

	def randVRare():
		veryRares = choice(veryRare)
		outLab.config(text=veryRares)

	def randLegendary():
		legendaries = choice(legendary)
		outLab.config(text=legendaries)

	def randArtifact():
		artifacts = choice(artifact)
		outLab.config(text=artifacts)


	magicWin = Tk(className=' MAGIC ITEMS ')
	magicWin.geometry("500x750")

	cButton = Button(magicWin, text="COMMON", height=5, width=15, font="Times25", command=randCommon)
	ucButton = Button(magicWin, text="UNCOMMON", height=5, width=15, font="Times25", command=randUncommon)
	rButton = Button(magicWin, text="RARE", height=5, width=15, font="Times25", command=randRare)
	vrButton = Button(magicWin, text="VERY RARE", height=5, width=15, font="Times25", command=randVRare)
	lButton = Button(magicWin, text="LEGENDARY", height=5, width=15, font="Times25", command=randLegendary)
	aButton = Button(magicWin, text="ARTIFACT", height=5, width=15, font="Times25", command=randArtifact)

	outLab = Label(magicWin, text="MAGIC ITEM", font="Times25")

	cButton.grid(row=0, column=0)
	ucButton.grid(row=1, column=0)
	rButton.grid(row=2, column=0)
	vrButton.grid(row=3, column=0)
	lButton.grid(row=4, column=0)
	aButton.grid(row=5, column=0)
	outLab.grid(row=1, column=1)






monstersButton = Button(root, text="MONSTERS", height=5, width=15, font='Times25', command=monsters)
charactersButton = Button(root, text="NPCS", height=5, width=15, font='Times25',command=character)
magicButton = Button(root, text="MAGIC", height=5, width=15, font='Times25', command=magic)
lootButton = Button(root, text="LOOT", height=5, width=15, font='Times25', command=randomizeLoot)



monstersButton.grid(row=0, column=0)
charactersButton.grid(row=1, column=0)
magicButton.grid(row=2, column=0)
lootButton.grid(row=3, column=0)



if __name__ == "__main__":
	root.mainloop()