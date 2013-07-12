from model import Camera

class MouseInfo:
	clickedx = 0
	clickedy = 0
	vertical = 0
	horizontal = 0

	side = None

	def setXY(self,side,x,y,vertical,horizontal):
		self.side = side
		self.vertical = vertical
		self.horizontal = horizontal

		self.clickedx = x
		self.clickedy = y
