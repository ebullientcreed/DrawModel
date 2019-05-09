# Thekkumpat,Navaneeth. 
# nxt6413
# 2019-05-02

#----------------------------------------------------------------------
import numpy
import math

class beizer_C :
	
	def resolveBezierPatch(self,resolution,controlPts):
		pointlist=[]
		control = []
		control.append(controlPts[0:4])
		control.append(controlPts[4:8])
		control.append(controlPts[8:12])
		control.append(controlPts[12:16])
		controlPts = control
		for u in numpy.linspace( 0.0, 1.0 ,resolution):
			for v in numpy.linspace( 0.0, 1.0 ,resolution):
				point=[ 0.0, 0.0, 0.0 ]
				#c1=((((-u+1)**3)*((-v+1)**3)),((3*v*((-u+1)**3))*((-v+1)**2)),((3*(v**2)*((-u+1)**3)*(-v+1))),(((v**3)*((-u+1)**3))))
				#c2=(((3*u*((-u+1)**2))*((-v+1)**3)),((9*u*v*((-u+1)**2))*((-v+1)**2)),((9*u*(v**2)*((-u+1)**2)*(-v+1))),(3*u*(v**3)*((-u+1)**2)))
				#c3=(((3*(u**2)*((-u+1)))*((-v+1)**3)),((9*v*(u**2)*((-u+1)))*((-v+1)**2)),(9*(v**2)*(u**2)*((-u+1))*(-v+1)),((3*(u**2)*(v**3)*((-u+1)))))
				#c4=((((u)**3)*((-v+1)**3)),((3*v*((u)**3))*((-v+1)**2)),(3*(u**3)*(v**2)*(-v+1)),((v**3)*(u**3)))
				#c=(c1,c2,c3,c4)
				for i in range(0,4):
					for j in range(0,4):
						c=(6.0/(math.factorial(i)*math.factorial(3-i)))*((u**i)*(1-u)**(3-i))*(6.0/(math.factorial(j)*math.factorial(3-j)))*((v**j)*(1-v)**(3-j))
						#point[0]=point[0]+(c[i][j]*controlPts[i][j][0])
						#point[1]=point[1]+(c[i][j]*controlPts[i][j][1])
						#point[2]=point[2]+(c[i][j]*controlPts[i][j][2])
						point[0]=point[0]+(c*controlPts[i][j][0])
						point[1]=point[1]+(c*controlPts[i][j][1])
						point[2]=point[2]+(c*controlPts[i][j][2])
				pointlist.append(point)
		return pointlist







