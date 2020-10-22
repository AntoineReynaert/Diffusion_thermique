import numpy as np
import matplotlib.pyplot as plt

# materiau             diffusivité thermique(m**2*s**-1)
#aluminium  98.8*10**-6
#fer        22.8*10**-6
#or         127.2*10**-6
#cuivre     117*10**-6
#argent     173*10**-6


nx=50
ny=50
lx=1
ly=1
dx=lx/(nx-1)
dy=ly/(ny-1)
dt=1

T_0=293.
T_thermostat=373.
k=98.8*10**-6
s=0

grille_t0=np.array([[T_0 for i in range(ny)]for i in range(nx)] )
for i in range(nx):
    grille_t0[i][0]=T_thermostat
    grille_t0[i][ny-1]=T_thermostat
for i in range(ny):
    grille_t0[0][i]=T_thermostat
    grille_t0[nx-1][i]=T_thermostat
    
np.array(grille_t0)    

def plaque_recursif(t):
    #est limité a 900 appels 
    t=int(t/dt)*dt
    if t==dt:
        T=grille_t0   
    else:
        T=plaque(t-dt)
    T2=grille_t0
    for i in range(1,nx-1):
        for j in range(1,ny-1):
                T2[i,j]=T[i,j]+k*dt/dx*(T[i+1,j]-2*T[i,j]+T[i-1,j])+k*dt/dy*(T[i,j+1]-2*T[i,j]+T[i,j-1])+s*dt
    return T2

def plaque_iteratif(t):
    T=grille_t0
    T2=grille_t0
    for h in range(int(t/dt)):
        for i in range(1,nx-1):
            for j in range(1,ny-1):
                T2[i,j]=T[i,j]+k*dt/dx**2*(T[i+1,j]-2*T[i,j]+T[i-1,j])+k*dt/dy**2*(T[i,j+1]-2*T[i,j]+T[i,j-1])+s*dt
        T=T2
    return T2

##plt.pcolormesh(plaque_iteratif(3600),vmin=293,vmax=373)
##plt.colorbar()
##plt.title("plaque d'aluminium 1mx1m")
##plt.show()


#animation

##T=grille_t0
##T2=grille_t0
##for h in range(4*360):
##    for i in range(1,nx-1):
##            for j in range(1,ny-1):
##                T2[i,j]=T[i,j]+k*dt/dx*(T[i+1,j]-2*T[i,j]+T[i-1,j])+k*dt/dy*(T[i,j+1]-2*T[i,j]+T[i,j-1])+s*dt
##    T=T2
##    plt.pcolormesh(T2,vmin=293,vmax=373)
##    plt.pause(0.01)
##
##plt.colorbar()
##plt.title("plaque d'aluminium 1mx1m, vitesse x1000")
##plt.show()


#ajout d'un thermostat au centre:

#thermostat de 4cmx4cm

grille_t0=np.array([[T_0 for i in range(ny)]for i in range(nx)] )
for i in range(nx):
    grille_t0[i][0]=T_thermostat
    grille_t0[i][ny-1]=T_thermostat
for i in range(ny):
    grille_t0[0][i]=T_thermostat
    grille_t0[nx-1][i]=T_thermostat

grille_t0[24,24],grille_t0[24,25],grille_t0[25,24],grille_t0[25,25]=T_thermostat,T_thermostat,T_thermostat,T_thermostat

T=grille_t0
T2=grille_t0
for h in range(4*360):
    for i in range(1,nx-1):
            for j in range(1,ny-1):
                if (i,j)!=(24,24) and (i,j)!=(24,25) and (i,j)!=(25,24) and (i,j)!=(25,25):
                    T2[i,j]=T[i,j]+k*dt/dx**2*(T[i+1,j]-2*T[i,j]+T[i-1,j])+k*dt/dy**2*(T[i,j+1]-2*T[i,j]+T[i,j-1])+s*dt
    T=T2
    plt.pcolormesh(T2,vmin=293,vmax=373)
    plt.axis('equal')
    plt.pause(0.01)

plt.colorbar()
plt.title("plaque d'aluminium 1mx1m, vitesse x1000")
plt.show()












