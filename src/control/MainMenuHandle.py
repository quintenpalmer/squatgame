import Model
import sys

class MainMenuHandle:
	def handleKey(self,key,x,y):
		if key == 'q':
			sys.exit(1)	
		elif key == 'v':
			pass
		elif key == 'c':
			pass
		elif key == 'g':
			Model.changeView("maingame")

	def handleUpKey(self,key,x,y):
		pass
