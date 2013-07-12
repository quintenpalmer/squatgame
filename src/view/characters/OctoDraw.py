from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class OctoDraw:

	def draw(self):
		self.drawOcto()

	def drawOcto(self):
		glTranslated(0,10,0)

		glColor3f(0.0,.0,0.0)

		glPushMatrix()
		glTranslated(5,3,1)
		glScaled(.5,1,.5)
		glutSolidSphere(1,8,8)
		glPopMatrix()

		glPushMatrix()
		glTranslated(5,3,-1)
		glScaled(.5,1,.5)
		glutSolidSphere(1,8,8)
		glPopMatrix()

		glColor3f(1.0,.35,0.0)

		glPushMatrix()
		glScaled(6,6,6)
		glutSolidSphere(1,2*8,2*8)
		glPopMatrix()

		for i in range(0,8):
			self.drawTentacle(i)
			
	def drawTentacle(self,offset):
		glRotated((360/8)*(offset),0,1,0)
		legswing = 50

		glPushMatrix()
		qobj = gluNewQuadric()
		gluQuadricDrawStyle(qobj,GLU_FILL)
		glTranslated(0,-2,-2)
		glRotated(170,1,0,0)

		glRotated(10,0,1,0)

		glPushMatrix()
		glScaled(1.5,1.5,5)
		gluCylinder(qobj,1,1,1,8,8)
		glPopMatrix()

		glTranslated(0,0,5)

		glPushMatrix()
		glScaled(1.5,1.5,1.5)
		glutSolidSphere(1,8,8)
		glPopMatrix()

		glRotated(-30,1,0,0)

		glPushMatrix()
		glScaled(1.5,1.5,5)
		gluCylinder(qobj,1,1,1,8,8)
		glPopMatrix()
		
		glTranslated(0,0,5)

		glPushMatrix()
		glScaled(1.5,1.5,1.5)
		glutSolidSphere(1,8,8)
		glPopMatrix()

		glRotated(30,1,0,0)

		glPushMatrix()
		glScaled(1.5,1.5,10)
		gluCylinder(qobj,1,1,1,8,8)
		glPopMatrix()
		
		glPopMatrix()
		

