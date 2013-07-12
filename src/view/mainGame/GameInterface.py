from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from utils import Util
import Model

def draw():
	Util.setup2D()

	glColor(.15,.21,.41)
	barwidth = 400
	x1 = (Model.getWinfo().w/2)-(barwidth/2)
	x2 = (Model.getWinfo().w/2)+(barwidth/2)
	y1 = 20
	y2 = 50
	glRectf(x1,y1,x2,y2)

	Util.finish2D()
