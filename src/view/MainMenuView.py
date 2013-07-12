import Model
import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from utils import Util

class MainMenuView:
	spin = 0

	def view(self):
		Util.setup3d()

		self.drawMap()
		self.drawModel()
		
		glFlush()
		glutSwapBuffers()

	def drawModel(self):
		self.spin += 1
		glRotate(self.spin,0,1,0)

		glPushMatrix()
		glColor3f(1.0,0.35,0.0)

		glScale(16,16,16)
		glutSolidCube(1)
		glPopMatrix()

		glTranslate(0,8,0)
		Model.getGame().getPlayer().draw()

	def drawMap(self):
		glPushMatrix()
		glScale(66,1,66)
		glutSolidCube(1)
		glPopMatrix()


