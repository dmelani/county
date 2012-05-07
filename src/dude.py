from OpenGL.GL import * 
from OpenGL.GLU import * 
from OpenGL.GLUT import * 
from tools import Increment

class Dude(object):
	def __init__(self):

		self.pos_x = 0.0
		self.pos_y = 0.0
		self.pos_z = 0.0
		self.l_x = 0.0
		self.l_y = 0.0
		self.l_z = 0.0
		
		self.flux = []

	def move_to(self, x, y, z):
		self.pos_x = x
		self.pos_y = y
		self.pos_z = z

	def look_at(self, x, y, z):
		self.l_x = x
		self.l_y = y
		self.l_z = z

	def perceive(self):
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		gluPerspective(90,800.0/600.0,1.0,2000.0)
		gluLookAt(self.pos_x, self.pos_y, self.pos_z, self.l_x, self.l_y, self.l_z, 0.0, 1.0, 0.0)			

