from utils import Util

class Running:
	tic = 0.0
	maxtime = 100.0

	frames = []

	lknees = []
	rknees = []
	lhhips = []
	rhhips = []

	def __init__(self):

		self.lknees.append(["lknee",0,0]) 
		self.lknees.append(["lknee",-100,50])
		self.lknees.append(["lknee",0,self.maxtime])

		self.frames.append(self.lknees)

		self.lhhips.append(["lhhip",0,0])
		self.lhhips.append(["lhhip",50,50])
		self.lhhips.append(["lhhip",0,self.maxtime])

		self.frames.append(self.lhhips)

		self.rknees.append(["rknee",-100,0])
		self.rknees.append(["rknee",0,50])
		self.rknees.append(["rknee",-100,self.maxtime])

		self.frames.append(self.rknees)

		self.rhhips.append(["rhhip",50,0])
		self.rhhips.append(["rhhip",0,50])
		self.rhhips.append(["rhhip",50,self.maxtime])

		self.frames.append(self.rhhips)
