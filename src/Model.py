from model.Camera import Camera
from model.Winfo import Winfo
from model.GlutFuncs import GlutFuncs
from model.GameModel import GameModel
from model.MouseInfo import MouseInfo

game = GameModel()

glutFuncs = GlutFuncs()

camera = Camera()

winfo = Winfo()

camove = []

keybindings = []

mouseInfo = MouseInfo()

def getha():
	return ha

def getGame():
	return game.game

def getKeyHandle():
	return glutFuncs.keyHandle

def getViewer():
	return glutFuncs.viewer

def getMouseHandle():
	return glutFuncs.mouseHandle

def getAmbient():
	return glutFuncs.ambient

def getMotion():
	return glutFuncs.motion

def getCamera():
	return camera

def getWinfo():
	return winfo

def getMouseInfo():
	return mouseInfo

def changeView(name):
	glutFuncs.change(name)
	camera.change(name)
	game.change(name)
