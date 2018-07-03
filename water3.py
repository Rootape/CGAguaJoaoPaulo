#https://threejs.org/examples/#webgl_water
#https://math.stackexchange.com/questions/2097503/what-mathematical-shape-is-the-surface-of-waves-on-water
#https://pdfs.semanticscholar.org/b88a/c2e6b2cd4f72835e89209d8240615791f742.pdf
#https://en.wikipedia.org/wiki/Midpoint_circle_algorithm

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

chg = []
vec = []
#m = 144
m = 72
eq = 0
#crista = 5
crista = 3
test = 0
hitter = 0


for i in range(0, m):
        aux = []
        for j in range(0, m):
                aux.append([j - m/2, eq])
        vec.append(aux)


def midPoint(raio):
        
        ang = math.pi / 180
	circParts = []
		
	for i in range(1, 360):
	    
	    if i != 90 or i != 180 or i != 270:
		vec = []
		
		xi = raio * math.cos(ang * i)
		zi = raio * math.sin(ang * i)
		
		x = int(xi)
		z = int(zi)
		
		if abs(xi - x) > 0.5:    
		    x = x + 1

		if abs(zi - z) > 0.5:
		    z = z + 1
		   
		vec = [x, z]
		
		if vec not in circParts and vec != [0, 0] and vec != [1, 1] and vec != [-1, 1] and vec != [1, -1] and vec != [-1, -1]:
		    circParts.append(vec)

		rem = []
		for i in range(1, len(circParts) - 1):
		    if (circParts[i][0] == circParts[i+1][0] and circParts[i][1] == circParts[i-1][1]) or (circParts[i][0] == circParts[i-1][0] and circParts[i][1] == circParts[i+1][1]):
			rem.append(i)

		for i in rem:
		    del circParts[i]

	return circParts

def handlerX(i, j, r):
	ang = math.pi / 180
	return vec[i][j][0] + r * math.cos( (vec[i][j][1]) * ang)

def handlerY(i, j, r):
	ang = math.pi / 180
	return r * math.sin( (vec[i][j][1]) * ang)

def waterHit():
	center = m/2
	auxAng = 270
	reducer = 270/(crista*3) 
	counter = 0	

	for i in range(0, crista * 3):
		points = midPoint(i)
		for cord in points:
			if cord[0] >= 0 and cord[0] < m and cord[1] >= 0 and cord[1] < m:
				vec[cord[0] + m/2][cord[1] + m/2][1] = auxAng
				auxAng += reducer
				if auxAng >= 360:
					auxAng -= 360
				
def wavHandler():

	vAux = vec[m/2][m/2][1]

	for i in range(1, m/2):
		points = midPoint(i)
		vAux2 = vec[m/2][m/2 + i][1]
		for cord in points:
			vec[cord[0] + m/2][cord[1] + m/2][1] = vAux
		vAux = vAux2	
		
testing = 0
r = 2

def Parab():

	global r
	global crista
	global hitter
	global testing

	if r > 0:
		r -= 0.1

	if hitter == 1:
		wavHandler()

	if hitter == 0:
		waterHit()
		hitter = 1

	glColor3fv((0, 0, 1))

        for i in range(0, m-1):
                for j in range(0, m-1):
                        glBegin(GL_TRIANGLES)
                        glVertex3f(handlerX(i, j, r), handlerY(i, j, r), (i - (m/2.0)))
                        glVertex3f(handlerX(i, j+1, r), handlerY(i, j+1, r), (i - (m/2.0)))
                        glVertex3f(handlerX(i, j, r), handlerY(i, j, r), (i - (m/2.0))+1)
                        glEnd()

			glBegin(GL_TRIANGLES)
			glVertex3f(handlerX(i, j+1, r), handlerY(i, j+1, r), (i - (m/2.0))+1)
			glVertex3f(handlerX(i, j+1, r), handlerY(i, j+1, r), (i - (m/2.0)))
                        glVertex3f(handlerX(i, j, r), handlerY(i, j, r), (i - (m/2.0))+1)
                        glEnd()


#	for i in range(0, m-1):
#                for j in range(0, m-1):
#                        glBegin(GL_QUADS)
#                        glVertex3f(handlerX(i, j, r), handlerY(i, j, r), (i - (m/2.0)))
#                        glVertex3f(handlerX(i, j+1, r), handlerY(i, j+1, r), (i - (m/2.0)))
#                        glVertex3f(handlerX(i, j+1, r), handlerY(i, j+1, r), (i - (m/2.0))+1)
#                        glVertex3f(handlerX(i, j, r), handlerY(i, j, r), (i - (m/2.0))+1)
#                        glEnd()

def abacaxi():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    #glRotatef(2,1,3,0)
    Parab()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(100,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("PARABOLA")
glutDisplayFunc(abacaxi)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(90,800.0/600.0,0.1,50.0)
glTranslatef(0.0,-5.0,-20)
#glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
glutMainLoop()
	

