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
		glEnable(GL_DEPTH_TEST)
		glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
		glDepthMask(GL_TRUE)
		glEnable(GL_BLEND)
		glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
		glClearColor(0.0, 0.0, 0.0, 1.0)

	def clear(self):
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		

