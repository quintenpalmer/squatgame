from utils import Util

class Camera:
	location = [30,30,0]
	lookAt = [-70,10,0]
	up = [0,1,0]
	horizon = 0
	vertical = -10
	distance = 50

	def change(self,name):
		if name == "maingame":
			self.horizontal = 0
			self.vertical = .25
			Util.resetCamera()
		elif name == "mainmenu":
			self.location = [30,30,0]
			self.lookAt = [-70,10,0]
			self.up = [0,1,0]
			self.horizon = 0
			self.vertical = -1.0
			self.distance = 50
