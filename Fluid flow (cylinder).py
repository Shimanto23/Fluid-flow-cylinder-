import numpy as np
import matplotlib.pyplot as plt
from numpy import cos,sin

x = np.linspace(-5,5,500)
y = np.linspace(-5,5,500)
X,Y = np.meshgrid(x,y)

U = 2 
R = 2 

r = np.sqrt(X**2+Y**2)  
theta = np.arctan(Y/X)  

Vr = U*(1-(R**2/r**2))*cos(theta) 
Vt = -U*(1+(R**2/r**2))*sin(theta) 

Vx = Vr*cos(theta) - Vt*sin(theta) 
Vy = Vr*sin(theta) + Vt*cos(theta) 

Vx[r<R] = np.nan 
Vy[r<R] = np.nan

plt.figure(figsize=(10,10),dpi=200)
circle1 = plt.Circle((0,0),R,color='white')
plt.gca().add_patch(circle1)

strplot = plt.streamplot(X,Y,Vx,Vy,color = np.sqrt(Vx**2+Vy**2),density=[2,2],cmap='jet')
plt.colorbar()
plt.show()