from control.MainMenuHandle import MainMenuHandle
from view.MainMenuView import MainMenuView
from control.MainMenuAmbient import MainMenuAmbient
from control.MainMenuMouse import MainMenuMouse
from control.MainMenuMotion import MainMenuMotion
from control.GameHandle import GameHandle
from control.GameMotion import GameMotion
from view.mainGame.GameView import GameView
from control.GameAmbient import GameAmbient
from control.GameMouse import GameMouse

class GlutFuncs:
	keyHandle = MainMenuHandle()
	viewer = MainMenuView()
	ambient = MainMenuAmbient()
	mouseHandle = MainMenuMouse()
	motion = MainMenuMotion()

	mainMenuHandle = MainMenuHandle()
	mainMenuView = MainMenuView()
	mainMenuAmbient = MainMenuAmbient()
	mainMenuMouse = MainMenuMouse()
	motion = GameMotion()

	gameHandle = GameHandle()
	gameView = GameView()
	gameAmbient = GameAmbient()
	gameMouse = GameMouse()

	def change(self,name):
		if name == "mainmenu":
			self.keyHandle = self.mainMenuHandle
			self.viewer = self.mainMenuView
			self.ambient = self.mainMenuAmbient
			self.mouseHandle = self.mainMenuMouse
		elif name == "maingame":
			self.keyHandle = self.gameHandle
			self.viewer = self.gameView
			self.ambient = self.gameAmbient
			self.mouseHandle = self.gameMouse

