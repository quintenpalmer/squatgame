import math

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from utils import Util
import Model
from . import GameInterface
from . import Background

class GameView:
	def view(self):
		Util.setup3d()
		Util.updateCamera()

		self.drawBackground()
		self.drawMap()
		self.drawModel(Model.getGame().getPlayer())
		self.drawOthers()
		self.drawTarget()
		self.drawInterface()

		glFlush()
		glutSwapBuffers()

	def drawModel(self,player):
		glPushMatrix()
		angle = 180/math.pi*player.horizon

		glTranslate(player.getX(),player.getZ(),player.getY())
		glRotate(angle,0,1,0)

		player.draw()
		glPopMatrix()

	def drawOthers(self):
		for player in Model.getGame().getOthers():
			self.drawModel(player)

	def drawMap(self):
		Model.getGame().getMap().draw()

	def drawInterface(self):
		GameInterface.draw()

	def drawTarget(self):
		target = Model.getGame().getTarget()
		if target != None:
			glPushMatrix()
			glColor(.9,.5,.1)
			glTranslate(target.getX(),target.z+target.physical.height+15,target.getY())
			glScale(4,4,4)
			glutSolidCube(1)
			glPopMatrix()

	def drawBackground(self):
		Background.draw()
