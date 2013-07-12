import Model
from utils import Util

class GameMotion:
	def motion(self,x,y):
		turnh = -(x-Model.getMouseInfo().clickedx)/(Model.getWinfo().w*.31)
		turnv = (y-Model.getMouseInfo().clickedy)/(Model.getWinfo().w*.31)
		if Model.getMouseInfo().side == "left":
			Util.restoreCamera()
			Util.turnCamera(turnh,turnv)
		elif Model.getMouseInfo().side == "right":
			Util.restoreCamera()
			Util.turnCamera(turnh,turnv)
			Util.resetPlayer()
