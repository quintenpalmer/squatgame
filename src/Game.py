import sys

from OpenGL.GL import *
from OpenGL.GLUT import *

import Model

class Main:
	def __init__(self):
		Model.getWinfo().setXY(800,800)

	def init(self):
		glClearColor(1.0, 1.0, 1.0, 0.0)
		glColor3f(0.0,0.0,0.0)
		glPointSize(1.0)
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		glOrtho(0.0, 640.0, 0.0, 480.0, -1.0, 1.0)
		glClear(GL_COLOR_BUFFER_BIT);

	def display(self,*args):
		Model.getViewer().view()

	def ambient(self):
		Model.getAmbient().calc()
		self.display()

	def keyboard(self,key,x,y):
		Model.getKeyHandle().handleKey(key,x,y)

	def keyboardUp(self,key,x,y):
		Model.getKeyHandle().handleUpKey(key,x,y)

	def mouse(self,button, state, x, y):
		Model.getMouseHandle().handleMouse(button,state,x,y)

	def motion(self,x,y):
		Model.getMotion().motion(x,y)

	def reshape(self,w, h):
		glViewport(0, 0, w, h)
		Model.getWinfo().setXY(w,h)
		self.init()

	def main(self):
		glutInit()
		glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
		glutInitWindowSize(800, 800)
		glutInitWindowPosition(400,0)
		glutCreateWindow('OpenGL')
		self.init()
		glutReshapeFunc(self.reshape)
		glutDisplayFunc(self.display)
		glutIdleFunc(self.ambient)
		glutMouseFunc(self.mouse)
		glutKeyboardFunc(self.keyboard)
		glutKeyboardUpFunc(self.keyboardUp)
		glutMotionFunc(self.motion)

		glEnable(GL_LIGHTING)
		glEnable(GL_LIGHT0)
		glShadeModel(GL_SMOOTH)
		glEnable(GL_DEPTH_TEST)
		glEnable(GL_NORMALIZE)

		glEnable(GL_COLOR_MATERIAL);
		glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE);

		glutMainLoop()

main = Main()
main.main()
