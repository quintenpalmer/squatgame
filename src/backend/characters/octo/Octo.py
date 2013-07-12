from view.characters.OctoDraw import OctoDraw
from ...Being import Being

class Octo(Being):
	drawer = OctoDraw()

	def draw(self):
		self.drawer.draw()

	def animate(self):
		pass
