from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def drawMap(locs):

	for i in range(len(locs)-1):
		for j in range(len(locs[i])-1):

			glColor(locs[i][j][3][0],locs[i][j][3][1],locs[i][j][3][2])
			glBegin(GL_TRIANGLES)
			glVertex(locs[i][j+1][0],locs[i][j+1][2],locs[i][j+1][1])
			glVertex(locs[i][j][0],locs[i][j][2],locs[i][j][1])
			glVertex(locs[i+1][j][0],locs[i+1][j][2],locs[i+1][j][1])
			glEnd()

			glColor(locs[i][j][3][0]+locs[i][j][4][0],locs[i][j][3][1]+locs[i][j][4][1],locs[i][j][3][2]+locs[i][j][4][2])
			glBegin(GL_TRIANGLES)
			glVertex(locs[i+1][j+1][0],locs[i+1][j+1][2],locs[i+1][j+1][1])
			glVertex(locs[i][j+1][0],locs[i][j+1][2],locs[i][j+1][1])
			glVertex(locs[i+1][j][0],locs[i+1][j][2],locs[i+1][j][1])
			glEnd()
