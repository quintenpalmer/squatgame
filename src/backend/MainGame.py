from maps.MainMap import MainMap
from characters.human.Human import Human
from utils import Util

class MainGame:
	board = None
	player = None
	others = None

	playerToGo = None

	tab = None
	target = None

	def __init__(self):
		self.player = Human(4.0,3.0,5.0,2.9,     10.0,7.0,4.0,    4.0,2.9,5.0,3,   4.0,4.0,4.0)
		self.playerToGo = self.player
		self.others = []
		self.others.append(Human(7.0,4.4,7.0,4.5,   15.0,11.0,7.0,  4.0,4.9,5.0,5,  4.0,4.0,4.0))
		self.player.numOthers += 1
		self.board = MainMap()

	def init(self,name):
		if name == "maingame":
			self.player = self.playerToGo
		elif name == "mainmenu":
			self.playerToGo = self.player

	def getPlayer(self):
		return self.player

	def getMap(self):
		return self.board

	def getOthers(self):
		return self.others

	def addOther(self,person):
		others.append(person)

	def removeOther(self,person):
		others.remove(person)

	def animate(self):
		Util.animate(self.player.physical,self.player.keyframes)
		for player in self.others:
			Util.animate(player.physical,player.keyframes)

	def gravity(self):
		Util.gravity(self.player,self.board)
		for player in self.others:
			Util.gravity(player,self.board)

	def getTarget(self):
		return self.target

	def toggleTarget(self):
		if self.tab != None:
			self.tab+=1%len(self.others)
		else:
			self.tab = 0
		self.target = self.others[self.tab]

	def clearTarget(self):
		self.tab = None
		self.target = None
