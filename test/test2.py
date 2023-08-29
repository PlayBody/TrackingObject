import math
from PyQt6.QtOpenGL import (QOpenGLBuffer, QOpenGLShader, QOpenGLShaderProgram, QOpenGLTexture)
from PyQt6 import QtCore, QtOpenGL, QtWidgets, QtGui, QtOpenGLWidgets
from PyQt6.QtOpenGLWidgets import QOpenGLWidget
from OpenGL import GLU
import OpenGL.GL as gl

class GLSphere(QOpenGLWidget):

  def __init__(self):

    # Inherit from QOpenGLWidget
    super().__init__()  
    
    # Initial sphere position
    self.xPos = 0.0 
    self.yPos = 0.0
    
    # Store texture image
    self.texture = QOpenGLTexture(QOpenGLTexture.Target.Target2D)

  def initializeGL(self):

    # Initialize OpenGL functions
    # self.initializeGL()

    # Setup viewport, projection etc
    self.resizeGL(self.width(), self.height()) 

    # Create shader program
    self.program = QOpenGLShaderProgram()

    # Add and compile shaders 
    self.program.addShaderFromSourceFile(QOpenGLShader.ShaderTypeBit.Vertex, "vertex.glsl")
    self.program.addShaderFromSourceFile(QOpenGLShader.ShaderTypeBit.Fragment, "fragment.glsl")

    # Link program and check for errors
    self.program.link()
    self.program.bind()

    # Load and bind texture
    # self.texture.setData(image_data)
    self.texture.setMinificationFilter(QOpenGLTexture.Filter.LinearMipMapLinear)
    self.texture.setMagnificationFilter(QOpenGLTexture.Filter.Linear) 
    
    # Start redraw timer
    self.timer = QtCore.QTimer(self)
    self.timer.timeout.connect(self.update)
    self.timer.start(20)

  def paintGL(self):

    # Clear buffers and set view 
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

    # Bind texture
    self.texture.bind()  

    # Pass vars to shaders
    uniform = self.program.uniformLocation("translation")
    gl.glUniform3f(uniform, self.xPos, self.yPos, 0.0)

    # Draw sphere using VAO/VBO
    # self.vao.bind()
    # gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 0, sphere_vertices.size())

  # Keypress handler  
  def keyPressEvent(self, event):

    # Update position  
    if event.key() == QtCore.Qt.Key.Key_A:
       self.xPos -= 0.1
    elif event.key() == QtCore.Qt.Key.Key_D:  
       self.xPos += 0.1

  # Timer redraws  
  def timerEvent(self, event):
    self.update()

app = QtWidgets.QApplication([])
widget = GLSphere()  
widget.show()
app.exec()