import sys

from utils import Util
import Model

class GameHandle:
	def handleKey(self,key,x,y):
		if key == 'c':
			Model.getGame().getPlayer().toggleAuto()
		if key == 'z':
			Util.resetCamera()
		if key == '\x20':
			Model.getGame().getPlayer().jump()
		if key == '\t':
			Model.getGame().toggleTarget()
		if key == '\x1b':
			Model.getGame().clearTarget()
		if key == 'q':
			sys.exit()
		if key == 'g':
			Model.getGame().getPlayer().blink()
		if key == 't':
			Model.changeView("mainmenu")

		self.handleConstantDown(key)

	def handleUpKey(self,key,x,y):
		if key == 'e' and Model.camove.count("forward") > 0:
			Model.getGame().getPlayer().standing()
			Model.camove.remove("forward")
		elif key == 'd' and Model.camove.count("backward") > 0:
			Model.camove.remove("backward")
		elif key == 'w' and Model.camove.count("sleft") > 0:
			Model.camove.remove("sleft")
		elif key == 'r' and Model.camove.count("sright") > 0:
			Model.camove.remove("sright")
		elif key == 'f' and Model.camove.count("tright") > 0:
			Model.camove.remove("tright")
		elif key == 's' and Model.camove.count("tleft") > 0:
			Model.camove.remove("tleft")
		elif key == '5' and Model.camove.count("cameraright") > 0:
			Model.camove.remove("cameraright")
		elif key == '1' and Model.camove.count("cameraleft") > 0:
			Model.camove.remove("cameraleft")
		elif key == 'x' and Model.camove.count("zoomout") > 0:
			Model.camove.remove("zoomout")
		elif key == 'v' and Model.camove.count("zoomin") > 0:
			Model.camove.remove("zoomin")
		elif key == '4' and Model.camove.count("cameradown") > 0:
			Model.camove.remove("cameradown")
		elif key == '2' and Model.camove.count("cameraup") > 0:
			Model.camove.remove("cameraup")

	def handleConstantDown(self,key):
		if key == 'e' and Model.camove.count("forward") == 0:
			Model.getGame().getPlayer().running()
			Model.camove.append("forward")
		elif key == 'd' and Model.camove.count("backward") == 0:
			Model.camove.append("backward")
		elif key == 'w' and Model.camove.count("sleft") == 0:
			Model.camove.append("sleft")
		elif key == 'r' and Model.camove.count("sright") == 0:
			Model.camove.append("sright")
		elif key == 'f' and Model.camove.count("tright") == 0:
			Model.camove.append("tright")
		elif key == 's' and Model.camove.count("tleft") == 0:
			Model.camove.append("tleft")
		elif key == '5' and Model.camove.count("cameraright") == 0:
			Model.camove.append("cameraright")
		elif key == '1' and Model.camove.count("cameraleft") == 0:
			Model.camove.append("cameraleft")
		elif key == 'x' and Model.camove.count("zoomout") == 0:
			Model.camove.append("zoomout")
		elif key == 'v' and Model.camove.count("zoomin") == 0:
			Model.camove.append("zoomin")
		elif key == '4' and Model.camove.count("cameradown") == 0:
			Model.camove.append("cameradown")
		elif key == '2' and Model.camove.count("cameraup") == 0:
			Model.camove.append("cameraup")
