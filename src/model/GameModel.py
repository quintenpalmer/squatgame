from backend.MainGame import MainGame

class GameModel:
	game = MainGame()

	def change(self,name):
		self.game.init(name)
