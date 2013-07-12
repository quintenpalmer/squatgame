from utils import Util

class Standing:
	tic = 0.0
	maxtime = 100.0

	frames = []

	lknees = []
	rknees = []
	lhhips = []
	rhhips = []

	lknees.append(["lknee",0,0])
	lknees.append(["lknee",-100,20])
	lknees.append(["lknee",-100,40])
	lknees.append(["lknee",0,60])
	lknees.append(["lknee",0,maxtime])

	frames.append(lknees)

	lhhips.append(["lhhip",0,0])
	lhhips.append(["lhhip",50,20])
	lhhips.append(["lhhip",100,60])
	lhhips.append(["lhhip",0,maxtime])

	frames.append(lhhips)

	rknees.append(["rknee",0,0])
	rknees.append(["rknee",-100,40])
	rknees.append(["rknee",0,maxtime])
	frames.append(rknees)

	rhhips.append(["rhhip",0,0])
	rhhips.append(["rhhip",50,40])
	rhhips.append(["rhhip",0,maxtime])

	frames.append(rhhips)
