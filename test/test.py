from OpenGL import GLU
import OpenGL.GL as gl
from PyQt6 import QtOpenGL, QtWidgets, QtGui, QtOpenGLWidgets
import math

class GLSphere(QtOpenGLWidgets.QOpenGLWidget):

  def __init__(self, parent=None):
    self.parent = parent
    QtOpenGLWidgets.QOpenGLWidget.__init__(self, parent)
  
  def initializeGL(self):
    # self.glClearColor(QtGui.QColor(0, 0, 255))
    # gl.glEnable(gl.GL_DEPTH_TEST)
    gl.glClearColor(1, 1, 1, 1)

    gl.glClearDepth(1.0)              
    gl.glDepthFunc(gl.GL_LESS)
    gl.glEnable(gl.GL_DEPTH_TEST)
    gl.glShadeModel(gl.GL_SMOOTH)
    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()                    
    GLU.gluPerspective(45.0, 1.33, 0.1, 100.0) 
    gl.glMatrixMode(gl.GL_MODELVIEW)

  def resizeGL(self, width, height):
    gl.glViewport(0, 0, width, height)
    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    aspect = width / float(height)

    GLU.gluPerspective(45.0, aspect, 1.0, 100.0)
    gl.glMatrixMode(gl.GL_MODELVIEW)

  def paintGL(self):
    # gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    # gl.glLoadIdentity()
    
    # gl.glTranslatef(0.0, 0.0, -5.0)

    # gl.glBegin(gl.GL_TRIANGLE_STRIP)

    # for i in range(21):
    #   theta = i * 3.1415927 / 10
    #   gl.glVertex3f(0.5*math.cos(theta),      0.5*math.sin(theta), 0.0)
    #   gl.glVertex3f(0.5*math.cos(theta+0.03), 0.5*math.sin(theta+0.03), 0.0)

    # gl.glEnd()

    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    gl.glLoadIdentity()
    gl.glTranslatef(-2.5, 0.5, -6.0)
    gl.glColor3f( 1.0, 1.5, 0.0 )
    gl.glPolygonMode(gl.GL_FRONT, gl.GL_FILL)
    gl.glBegin(gl.GL_TRIANGLES)
    gl.glVertex3f(0, 2, 0.0)
    gl.glVertex3f(0, 0.0, 0.0)
    gl.glVertex3f(0, 1, 1)
    gl.glEnd()
    gl.glFlush()

app = QtWidgets.QApplication([])
widget = GLSphere()  
widget.show()
app.exec()