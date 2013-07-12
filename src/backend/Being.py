
class Being:
	x = 6000
	y = 6000

	z = 10
	dz = 0

	auto = 0

	horizon = 0
	vertical = 0

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def setX(self,nX):
		self.x = nX

	def setY(self,nY):
		self.y = nY

	def getZ(self):
		return self.z

	def dX(self,d):
		self.x+=d

	def dY(self,d):
		self.y+=d

	def dZ(self):
		self.z += self.dz

	def getAuto(self):
		return self.auto

	def offAuto(self):
		self.auto = 0

	def toggleAuto(self):
		self.auto = 1 - self.auto

	def jump(self):
		self.dz = .5
