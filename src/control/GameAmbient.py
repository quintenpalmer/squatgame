from utils import Util
import Model

class GameAmbient:
	def calc(self):
		Model.getGame().animate()
		Model.getGame().gravity()
		self.move()

	def move(self):
		forward = 0
		left = 0
		for key in Model.camove:
			if key == "forward":
				Model.getGame().getPlayer().offAuto()
				forward += 1
			elif key == "backward":
				Model.getGame().getPlayer().offAuto()
				forward += -1
			elif key == "sleft":
				left += 1
			elif key == "sright":
				left += -1
			elif key == "tright":
				Util.turnCamera(-.02,0)
				Model.getGame().getPlayer().horizon-=.02
			elif key == "tleft":
				Util.turnCamera(.02,0)
				Model.getGame().getPlayer().horizon+=.02
			elif key == "cameraright":
				Util.turnCamera(.02,0)
			elif key == "cameraleft":
				Util.turnCamera(-.02,0)
			elif key == "zoomout":
				Model.getCamera().distance+=1
			elif key == "zoomin":
				Model.getCamera().distance-=1
			elif key == "cameradown":
				Util.turnCamera(0,.01)
			elif key == "cameraup":
				Util.turnCamera(0,-.01)
		Util.move(forward,left)

		Util.move(Model.getGame().getPlayer().getAuto(),0)
