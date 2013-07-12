from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import Model

def setup3d():
	camera = Model.getCamera()
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

	glColor3f(0.0,0.0,0.0)
#	gluPerspective(90,1,1,9000)
	width = float(Model.getWinfo().w)/float(Model.getWinfo().h)
	glFrustum(-width,width,-1,1,1,9000)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	gluLookAt(camera.location[0],camera.location[1],camera.location[2],camera.lookAt[0],camera.lookAt[1],camera.lookAt[2],camera.up[0],camera.up[1],camera.up[2])
	
	light = [0.2,0.2,0.2,1.0]
	glLightfv(GL_LIGHT0,GL_AMBIENT,light)
	light0 = [0.5,0.5,0.5,1.0]
	glLightfv(GL_LIGHT0,GL_DIFFUSE,light0)
	light1 = [2.0,20.0,2.0,1.0]
	glLightfv(GL_LIGHT0,GL_POSITION,light1)

def setup2D():
	glMatrixMode(GL_PROJECTION)
	glPushMatrix()
	glLoadIdentity()

	gluOrtho2D(0,Model.getWinfo().w,0,Model.getWinfo().h)
	glMatrixMode(GL_MODELVIEW)
	glPushMatrix()
	glLoadIdentity()

	glDisable(GL_DEPTH_TEST)
	glDisable(GL_LIGHTING)


def finish2D():
	glEnable(GL_DEPTH_TEST)
	glEnable(GL_LIGHTING)

	glMatrixMode(GL_MODELVIEW)
	glPopMatrix()

	glMatrixMode(GL_PROJECTION)
	glPopMatrix()
	glMatrixMode(GL_MODELVIEW)



def circle(horizontal,vertical,distance,x,y):
	r = 100
	height = Model.getGame().getPlayer().z + Model.getGame().getPlayer().physical.staticHeight
	lx = -math.cos(horizontal)*distance+x
	ly = math.sin(horizontal)*distance+y
	lz = math.sin(vertical)*distance*2+height
	cx = math.cos(horizontal)*r+x
	cy = -math.sin(horizontal)*r+y
	cz = -math.sin(vertical)*r*2+height
	return [lx,lz,ly,cx,cz,cy]

#def updateCamera(camera, player):
def updateCamera():
	camera = Model.getCamera()
	player = Model.getGame().getPlayer()

	locs = circle(camera.horizon,camera.vertical,camera.distance,player.getX(),player.getY())
	camera.location[0] = locs[0]
	camera.location[1] = locs[1]
	camera.location[2] = locs[2]
	camera.lookAt[0]=locs[3]
	camera.lookAt[1] = locs[4]
	camera.lookAt[2]=locs[5]

#def resetCamera(camera,player):
def resetCamera():
	Model.getCamera().horizon = Model.getGame().getPlayer().horizon
	updateCamera()

def resetPlayer():
	Model.getGame().getPlayer().horizon = Model.getCamera().horizon

def restoreCamera():
	Model.getCamera().horizon = Model.getMouseInfo().horizontal
	Model.getCamera().vertical = Model.getMouseInfo().vertical
	updateCamera()

def move(forward,left):
	if forward != 0 and left != 0:
		forward = forward/math.sqrt(2)
		left = left/math.sqrt(2)

	player = Model.getGame().getPlayer()
	camera = Model.getCamera()

	fx = -math.cos(player.horizon)
	fy = math.sin(player.horizon)
	lx = math.cos(player.horizon+(math.pi/2))
	ly = -math.sin(player.horizon+(math.pi/2))

	player.dX(-forward*fx)
	camera.location[0]-=forward*fx
	camera.lookAt[0]-=forward*fx
	player.dY(-forward*fy)
	camera.location[2]-=forward*fy
	camera.lookAt[2]-=forward*fy

	player.dX(left*lx)
	camera.location[0]+=left*lx
	camera.lookAt[0]+=left*lx
	player.dY(left*ly)
	camera.location[2]+=left*ly
	camera.lookAt[2]+=left*ly

def turnCamera(left,up):
	Model.getCamera().horizon+=left
	Model.getCamera().vertical+=up
	updateCamera()

def interpolate(rot,arot,start,time,atime):
	arot = rot*(math.sin((atime/time)*math.pi-math.pi/2.0)+1.0)/2.0 + start*(1.0-(math.sin((atime/time)*math.pi-math.pi/2.0)+1.0)/2.0)
	return arot

def animate(physical,keyframes):
	for b in keyframes.frames:
		for f in range(0,len(b)-1):
			if keyframes.tic < b[f+1][2] and keyframes.tic > b[f][2]:
				angle = interpolate(b[f+1][1],physical.getJoint(b[f][0]),b[f][1],b[f+1][2]-b[f][2],keyframes.tic-b[f][2])
				physical.setJoint(b[f][0], angle)

	if keyframes.tic < keyframes.maxtime:
		keyframes.tic+=1.0
	else:
		keyframes.tic = 0

	physical.ground()

def gravity(player,board):
	size = board.size
	xindex = int(player.x/size)
	yindex = int(player.y/size)
	xamount = player.x/size
	yamount = player.y/size

	tdz = board.locs[xindex+1][yindex][2]
	bdz = board.locs[xindex][yindex+1][2]
	tda = (yindex+1)-(yamount)
	bda = (yamount-yindex)

	d = tdz*tda + bdz*bda
	dheight = 1 - (yamount - yindex)
	
	if (yamount-yindex) + (xamount-xindex) > 1:
		myz = board.locs[xindex+1][yindex][2]
		lz = board.locs[xindex+1][yindex+1][2]
		mya = (yindex+1)-(yamount)
		la = (yamount-yindex)
 		edge = myz*mya + lz*la

		amountd = (1 - (xamount-xindex))/(1-dheight)
		amountedge = ((xamount-xindex)- dheight)/(1-dheight)
		total = edge * amountedge + d * amountd

	else:
		myz = board.locs[xindex][yindex][2]
		lz = board.locs[xindex][yindex+1][2]
		mya = (yindex+1)-(yamount)
		la = (yamount-yindex)
 		edge = myz*mya + lz*la

		amountedge = (dheight-(xamount-xindex))/dheight
		amountd = (xamount-xindex)/dheight
		total = edge * amountedge + d * amountd
	
	player.z = total
