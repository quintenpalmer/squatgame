import math
import random

import Model
from view.maps import MainMapDraw

class MainMap:
	width = None
	height = None

	locs = None
	size = 700.0

	def __init__(self):
		self.locs = []
		for i in range(20):
			self.locs.append([])
			for j in range(20):
				c1 = .1+(random.random()-.5)/10
				c2 = .5+(random.random()-.5)/10
				c3 = .1+(random.random()-.5)/10
				d1 = (random.random()-.5)/10
				d2 = (random.random()-.5)/10
				d3 = (random.random()-.5)/10

				self.locs[i].append([i*self.size,j*self.size,self.size/5*math.sin(i*.3 + j*1.1) + self.size/5*math.sin(i*.5 - j*.7), [c1,c2,c3] , [d1,d2,d3] ])

		self.locs[2][2][2] += 20
		self.locs[3][3][2] += 30
		self.locs[3][2][2] += 40
		self.locs[2][3][2] += 30

		self.width = 500
		self.height = 700

	def getWidth(self):
		return self.width

	def getHeight(self):
		return self.height

	def draw(self):
		MainMapDraw.drawMap(self.locs)
