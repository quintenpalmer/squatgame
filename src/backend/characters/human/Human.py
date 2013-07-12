from Physical import Physical
from view.characters import HumanDraw
from ...Being import Being
from animations import Standing
from animations import Running
from utils import Util

class Human(Being):
	physical = None
	keyframes = None 

	run = None
	stand = None

	def __init__(self,nlLeg,nlLegw,nuLeg,nuLegw,    ntorsoHeight,ntorsoWidth,ntorsoDepth,     nlArm,nlArmw,nuArm,nuArmw,   nheadHeight,nheadWidth,nheadDepth):
		self.tab = 0
		self.numOthers = 0 
		self.physical = Physical(nlLeg,nlLegw,nuLeg,nuLegw,    ntorsoHeight,ntorsoWidth,ntorsoDepth,     nlArm,nlArmw,nuArm,nuArmw,   nheadHeight,nheadWidth,nheadDepth)
		self.keyframes = Standing.Standing()
		self.run = Running.Running()
		self.stand = Standing.Standing()

	def getPhysical(self):
		return self.physical

	def draw(self):
		HumanDraw.drawHuman(self.physical)

	def animate(self):
		Util.animate(self.physical,self.keyframes)

	def running(self):
		self.keyframes = self.run

	def standing(self):
		self.keyframes = self.stand
	
	def blink(self):
		Util.move(90,0)
