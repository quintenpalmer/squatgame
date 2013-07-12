from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def drawHuman(physical):

	glTranslate(0,physical.height,0)

	# torso
	glPushMatrix()

	glPushMatrix()
	glColor(.64,0,0)
	glScale(physical.torsoDepth,physical.torsoHeight,physical.torsoWidth)
	glutSolidCube(1)
	glPopMatrix()

	# left leg
	glPushMatrix()

	glTranslate(0,-physical.torsoHeight/2,-physical.torsoWidth/4)

	glRotate(physical.getJoint("lvhip"),1,0,0)
	glRotate(physical.getJoint("lhhip"),0,0,1)

	glTranslate(0,-physical.uLeg/2,0)

	glPushMatrix()
	glColor(0,0,.55)
	glScale(physical.uLegw,physical.uLeg,physical.uLegw)
	glutSolidCube(1)
	glPopMatrix()

	glTranslate(0,-physical.uLeg/2,0)

	glRotate(physical.getJoint("lknee"),0,0,1)

	glTranslate(0,-physical.lLeg/2,0)

	glPushMatrix()
	glColor(1,.8,.64)
	glScale(physical.lLegw,physical.lLeg,physical.lLegw)
	glutSolidCube(1)
	glPopMatrix()

	# left leg
	glPopMatrix()

	# right leg
	glPushMatrix()

	glTranslate(0,-physical.torsoHeight/2,physical.torsoWidth/4)

	glRotate(physical.getJoint("rvhip"),1,0,0)
	glRotate(physical.getJoint("rhhip"),0,0,1)

	glTranslate(0,-physical.uLeg/2,0)


	glPushMatrix()
	glColor(0,0,.55)
	glScale(physical.uLegw,physical.uLeg,physical.uLegw)
	glutSolidCube(1)
	glPopMatrix()

	glTranslate(0,-physical.uLeg/2,0)

	glRotate(physical.getJoint("rknee"),0,0,1)

	glTranslate(0,-physical.lLeg/2,0)

	glPushMatrix()
	glColor(1,.8,.64)
	glScale(physical.lLegw,physical.lLeg,physical.lLegw)
	glutSolidCube(1)
	glPopMatrix()

	# right leg
	glPopMatrix()

	# left arm
	glPushMatrix()

	glTranslate(0,physical.torsoHeight/4,physical.torsoWidth/2+1.5)

	glRotate(physical.getJoint("lvshoulder"),1,0,0)
	glRotate(physical.getJoint("lhshoulder"),0,0,1)

	glTranslate(0,-physical.uArm/4,0)

	glPushMatrix()
	glColor(.64,0,0)
	glScale(physical.uArmw,physical.uArm,physical.uArmw)
	glutSolidCube(1)
	glPopMatrix()

	glTranslate(0,-physical.uArm/2,0)

	glRotate(physical.getJoint("lelbow"),0,0,1)

	glTranslate(0,-physical.lArm/2,0)

	glPushMatrix()
	glColor(1,.8,.64)
	glScale(physical.lArmw,physical.lArm,physical.lArmw)
	glutSolidCube(1)
	glPopMatrix()

	# left arm
	glPopMatrix()

	# right arm
	glPushMatrix()

	glTranslate(0,physical.torsoHeight/4,-physical.torsoWidth/2-1.5)

	glRotate(physical.getJoint("rvshoulder"),1,0,0)
	glRotate(physical.getJoint("rhshoulder"),0,0,1)

	glTranslate(0,-physical.uArm/4,0)

	glPushMatrix()
	glColor(.64,0,0)
	glScale(physical.uArmw,physical.uArm,physical.uArmw)
	glutSolidCube(1)
	glPopMatrix()

	glTranslate(0,-physical.uArm/2,0)

	glRotate(physical.getJoint("relbow"),0,0,1)

	glTranslate(0,-physical.lArm/2,0)

	glPushMatrix()
	glColor(1,.8,.64)
	glScale(physical.lArmw,physical.lArm,physical.lArmw)
	glutSolidCube(1)
	glPopMatrix()

	# right arm
	glPopMatrix()


	# physical.head
	glPushMatrix()

	glTranslate(0,physical.torsoHeight/2,0)

	glRotate(physical.getJoint("xhead"),1,0,0)
	glRotate(physical.getJoint("yhead"),0,1,0)
	glRotate(physical.getJoint("zhead"),0,0,1)

	glTranslate(0,physical.headHeight/2,0)

	glPushMatrix()
	glColor(1,.8,.64)
	glScale(physical.headDepth,physical.headHeight,physical.headWidth)
	glutSolidCube(1)
	glPopMatrix()

	glPushMatrix()
	glColor(0.05,0.05,0.05)
	glTranslate(2,0,0)
	glutSolidCube(1)
	glPopMatrix()

	glTranslate(0,physical.headHeight/2,0)

	glPushMatrix()
	glColor(0.4,.26,.13)
	glScale(physical.headDepth*1.1,physical.headHeight*.3,physical.headWidth*1.1)
	glutSolidCube(1)
	glPopMatrix()

	# physical.head
	glPopMatrix()

	# torso
	glPopMatrix()
