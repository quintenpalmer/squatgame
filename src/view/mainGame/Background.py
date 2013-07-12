from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import Model
from utils import Util

def draw():
	Util.setup2D()

	glColor(.1,.1,.5)
	glRectf(0,Model.getWinfo().h/2,Model.getWinfo().w,Model.getWinfo().h)
	glColor(.1,.5,.1)
	glRectf(0,0,Model.getWinfo().w,Model.getWinfo().h/2)

	Util.finish2D()
		
