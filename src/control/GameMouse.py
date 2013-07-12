from OpenGL.GLUT import *
from OpenGL.GL import *

from utils import Util
import Model

class GameMouse:
	def handleMouse(self,button,state,x,y):
		x = x*1.0
		y = y*1.0
		if button == GLUT_LEFT_BUTTON and state == state == GLUT_DOWN:
		#	move camera appropriately
			Model.getMouseInfo().setXY("left",x,y,Model.getCamera().vertical,Model.getCamera().horizon)
			pass
		elif button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
		#	move camera and person appropriately
			Model.getMouseInfo().setXY("right",x,y,Model.getCamera().vertical,Model.getCamera().horizon)
		elif button == 3:
			Model.getCamera().distance-=3
		elif button == 4:
			Model.getCamera().distance+=3
