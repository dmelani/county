from OpenGL.GL import * 
from OpenGL.GLU import * 
from OpenGL.GLUT import * 
import pygame

class Firmament(object):
	width = 800
	height = 600
	def __init__(self):
		print 'Firmament solidified...'
		pygame.init()
		pygame.display.set_mode((self.width,self.height), pygame.OPENGL|pygame.DOUBLEBUF)
		glViewport(0, 0, self.width, self.height)
		#pygame.mouse.set_visible(False)

	def run(self):
		pass
