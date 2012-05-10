from OpenGL.GL import * 
from OpenGL.GLU import * 
from OpenGL.GLUT import * 
import traceback
import Image
import sys

class Geometrics(object):
	_instance = None
	def __new__(cls, *args, **kwargs):
		if not cls._instance:
			cls._instance = super(Geometrics, cls).__new__(cls, *args, **kwargs)
		return cls._instance

	def __init__(self):
		try:
			self.blue_tex = self.load_texture('src/textures/red.bmp')
			self.red_tex = self.load_texture('src/textures/red.bmp')
		except:
			print "Geometrics could not load textures:", traceback.format_exc()
			sys.exit()

	def blue_cube(self):
		glEnable(GL_TEXTURE_2D)
		glBindTexture(GL_TEXTURE_2D, self.blue_tex)
		glBegin(GL_QUADS)
		glTexCoord2f(0.0, 0.0); glVertex3f(0.0, 0.0,  1.0);
		glTexCoord2f(1.0, 0.0); glVertex3f( 1.0, 0.0,  1.0);
		glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0,  1.0);
		glTexCoord2f(0.0, 1.0); glVertex3f(0.0,  1.0,  1.0);

		glTexCoord2f(1.0, 0.0); glVertex3f(0.0, 0.0, 0.0);
		glTexCoord2f(1.0, 1.0); glVertex3f(0.0,  1.0, 0.0);
		glTexCoord2f(0.0, 1.0); glVertex3f( 1.0,  1.0, 0.0);
		glTexCoord2f(0.0, 0.0); glVertex3f( 1.0, 0.0, 0.0);

		glTexCoord2f(0.0, 1.0); glVertex3f(0.0,  1.0, 0.0);
		glTexCoord2f(0.0, 0.0); glVertex3f(0.0,  1.0,  1.0);
		glTexCoord2f(1.0, 0.0); glVertex3f( 1.0,  1.0,  1.0);
		glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0, 0.0);

		glTexCoord2f(1.0, 1.0); glVertex3f(0.0, 0.0, 0.0);
		glTexCoord2f(0.0, 1.0); glVertex3f( 1.0, 0.0, 0.0);
		glTexCoord2f(0.0, 0.0); glVertex3f( 1.0, 0.0,  1.0);
		glTexCoord2f(1.0, 0.0); glVertex3f(0.0, 0.0,  1.0);

		glTexCoord2f(1.0, 0.0); glVertex3f( 1.0, 0.0, 0.0);
		glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0, 0.0);
		glTexCoord2f(0.0, 1.0); glVertex3f( 1.0,  1.0,  1.0);
		glTexCoord2f(0.0, 0.0); glVertex3f( 1.0, 0.0,  1.0);

		glTexCoord2f(0.0, 0.0); glVertex3f(0.0, 0.0, 0.0);
		glTexCoord2f(1.0, 0.0); glVertex3f(0.0, 0.0,  1.0);
		glTexCoord2f(1.0, 1.0); glVertex3f(0.0,  1.0,  1.0);
		glTexCoord2f(0.0, 1.0); glVertex3f(0.0,  1.0, 0.0);
		glEnd()
	def red_cube(self):
		glEnable(GL_TEXTURE_2D)
		glBindTexture(GL_TEXTURE_2D, self.red_tex)
		glutSolidCube(1)
		
	def load_texture(self, path):
		p = Image.open(path)

		w = p.size[0]
		h = p.size[1]
		p = p.tostring("raw", "RGBX", 0, -1) 
		print "Geometrics texture dim:", w, h
		t = glGenTextures(1)
		glBindTexture(GL_TEXTURE_2D, t)
		#glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
		#glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
		glTexImage2D(GL_TEXTURE_2D, 0, 3, w, h, 0, GL_RGBA, GL_UNSIGNED_BYTE, p)
#		gluBuild2DMipmaps( GL_TEXTURE_2D, 3, w, h, GL_RGB, GL_UNSIGNED_BYTE, p )

		return t
