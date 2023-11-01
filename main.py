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

aarVar = BooleanVar()
draVar = BooleanVar()
hidVar = BooleanVar()
modVar = BooleanVar()
hieVar = BooleanVar()
woeVar = BooleanVar()
eleVar = BooleanVar()
dreVar = BooleanVar()


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
	charWin.geometry("500x710")

	aaraCb = Checkbutton(charWin, text="Aarakocra")
	draCb = Checkbutton(charWin, text="Dragonborn")
	hiDCb = Checkbutton(charWin, text="Hill Dwarf")
	moDCb = Checkbutton(charWin, text="Mountain Dwarf")
	hiECb = Checkbutton(charWin, text="High Elf")
	woECb = Checkbutton(charWin, text="Wood Elf")
	elECb = Checkbutton(charWin, text="Eladrin Elf")
	drECb = Checkbutton(charWin, text="Drow Elf")
	aiGCb = Checkbutton(charWin, text="Air Genasi")
	eaGCb = Checkbutton(charWin, text="Earth Genasi")
	fiGCb = Checkbutton(charWin, text="Fire Genasi")
	waGCb = Checkbutton(charWin, text="Water Genasi")
	roGCb = Checkbutton(charWin, text="Rock Gnome")
	deGCb = Checkbutton(charWin, text="Deep Gnome")
	golCb = Checkbutton(charWin, text="Goliath")
	haElCb = Checkbutton(charWin, text="Half-Elf")
	haOrCb = Checkbutton(charWin, text="Half-Orc")
	ligHaCb = Checkbutton(charWin, text="Lightfoot Halfling")
	stHaCb = Checkbutton(charWin, text="Stout Halfling")
	hCb = Checkbutton(charWin, text="Human")
	tCb = Checkbutton(charWin, text="Tiefling")
	aaCb = Checkbutton(charWin, text="Aasimar")
	aeCb = Checkbutton(charWin, text="Astral Elf")
	agCb = Checkbutton(charWin, text="Autognome")
	gifCb = Checkbutton(charWin, text="Giff")
	hadCb = Checkbutton(charWin, text="Hadozee")
	plaCb = Checkbutton(charWin, text="Plasmoid")
	thKCb = Checkbutton(charWin, text="Thri-Kreen")


	artiCb = Checkbutton(charWin, text="Artificer")
	barbCb = Checkbutton(charWin, text="Barbarian")
	bardCb = Checkbutton(charWin, text="Bard")
	clerCb = Checkbutton(charWin, text="Cleric")
	druiCb = Checkbutton(charWin, text="Druid")
	fighCb = Checkbutton(charWin, text="Fighter")
	monkCb = Checkbutton(charWin, text="Monk")
	palaCb = Checkbutton(charWin, text="Paladin")
	rangCb = Checkbutton(charWin, text="Ranger")
	roguCb = Checkbutton(charWin, text="Rogue")
	sorcCb = Checkbutton(charWin, text="Sorcerer")
	warlCb = Checkbutton(charWin, text="Warlock")
	wizaCb = Checkbutton(charWin, text="Wizard")

	


	aaraCb.grid(row=0, column=0)
	draCb.grid(row=1, column=0)
	hiDCb.grid(row=2, column=0)
	moDCb.grid(row=3, column=0)
	hiECb.grid(row=4, column=0)
	woECb.grid(row=5, column=0)
	elECb.grid(row=6, column=0)
	drECb.grid(row=7, column=0)
	aiGCb.grid(row=8, column=0)
	eaGCb.grid(row=9, column=0)
	fiGCb.grid(row=10, column=0)
	waGCb.grid(row=11, column=0)
	roGCb.grid(row=12, column=0)
	deGCb.grid(row=13, column=0)
	golCb.grid(row=14, column=0)
	haElCb.grid(row=15, column=0)
	haOrCb.grid(row=16, column=0)
	ligHaCb.grid(row=17, column=0)
	stHaCb.grid(row=18, column=0)
	hCb.grid(row=19, column=0)
	tCb.grid(row=20, column=0)
	aaCb.grid(row=21, column=0)
	aeCb.grid(row=22, column=0)
	agCb.grid(row=23, column=0)
	gifCb.grid(row=24, column=0)
	hadCb.grid(row=25, column=0)
	plaCb.grid(row=26, column=0)
	thKCb.grid(row=27, column=0)


	artiCb.grid(row=0, column=1)
	barbCb.grid(row=1, column=1)
	bardCb.grid(row=2, column=1)
	clerCb.grid(row=3, column=1)
	druiCb.grid(row=4, column=1)
	fighCb.grid(row=5, column=1)
	monkCb.grid(row=6, column=1)
	palaCb.grid(row=7, column=1)
	rangCb.grid(row=8, column=1)
	roguCb.grid(row=9, column=1)
	sorcCb.grid(row=10, column=1)
	warlCb.grid(row=11, column=1)
	wizaCb.grid(row=12, column=1)


	def randomizeNPC():
		print("RANDOMIZING")


	randomizeButton = Button(charWin, text="Randomize NPC!", font="Times25", command=randomizeNPC)

	randomizeButton.grid(row=0, column=2)


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