import math

class Physical:
#	length/width on bones
	lLeg = 0
	lLegw = 0
	uLeg = 0
	uLegw = 0
	torsoHeight = 0
	torsoWidth= 0
	lArm = 0
	lArmw = 0
	uArm = 0
	uArmw = 0
	headHeidght = 0
	headWidth = 0
	headDepth = 0

	height = None
	staticHeight = None

#	angles on joints
	angles = None

	def __init__(self,nlLeg,nlLegw,nuLeg,nuLegw,    ntorsoHeight,ntorsoWidth,ntorsoDepth,     nlArm,nlArmw,nuArm,nuArmw,   nheadHeight,nheadWidth,nheadDepth):
		self.lLeg = nlLeg
		self.lLegw = nlLegw
		self.uLeg = nuLeg
		self.uLegw = nuLegw

		self.torsoHeight = ntorsoHeight
		self.torsoWidth = ntorsoWidth
		self.torsoDepth = ntorsoDepth

		self.lArm = nlArm
		self.lArmw = nlArmw
		self.uArm = nuArm
		self.uArmw = nuArmw

		self.headHeight = nheadHeight
		self.headWidth = nheadWidth
		self.headDepth = nheadDepth

		self.angles = []
		self.angles.append(["lknee",0.0])
		self.angles.append(["lvhip",0.0])
		self.angles.append(["lhhip",0.0])
		self.angles.append(["lvshoulder",0.0])
		self.angles.append(["lhshoulder",0.0])
		self.angles.append(["lelbow",0.0])

		self.angles.append(["rknee",0.0])
		self.angles.append(["rvhip",0.0])
		self.angles.append(["rhhip",0.0])
		self.angles.append(["rvshoulder",0.0])
		self.angles.append(["rhshoulder",0.0])
		self.angles.append(["relbow",0.0])

		self.angles.append(["xhead",0.0])
		self.angles.append(["yhead",0.0])
		self.angles.append(["zhead",0.0])

		self.staticHeight = self.uLeg + self.lLeg + self.torsoHeight + self.headHeight

		self.ground()


	def ground(self):
		right = math.cos(math.pi*self.getJoint("rhhip")/180.0)*self.uLeg + math.cos(math.pi*self.getJoint("rknee")/180.0+math.pi*self.getJoint("rhhip")/180.0)*self.lLeg + self.torsoHeight/2
		left = math.cos(math.pi*self.getJoint("lhhip")/180.0)*self.uLeg + math.cos(math.pi*self.getJoint("lknee")/180.0+math.pi*self.getJoint("lhhip")/180.0)*self.lLeg + self.torsoHeight/2
		self.height = max(left,right)

	def setJoint(self,name,angle):
		for a in self.angles:
			if a[0] == name:
				a[1] = angle

	def getJoint(self,name):
		for a in self.angles:
			if a[0] == name:
				return a[1]
		return 9000
