

#Datos Entrada
Lw = 100
Latitud = -33.3911
Longitud = -70.7972
Altura = 200
Lw = 120
Hmap =2
import geojsoncontour
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import utm 

Eas, Nor, Zone, Num = utm.from_latlon(Latitud, Longitud)

def f(E, N, H, x, y, z, Lw):
    dist= np.sqrt((E-x)**2 + (N-y)**2 + (H-z)**2)
    Lp = Lw - 20*np.log10(dist)-8
    return Lp

x = np.linspace(Eas-1000, Eas+1000, 10)
y = np.linspace(Nor-1000, Nor+1000, 10)

X, Y = np.meshgrid(x, y)
Z = f(Eas, Nor, Altura, X, Y, Hmap, Lw)
Lat, Lon  = utm.to_latlon(x, y, Zone, Num)
fig, ax = plt.subplots()
cs = ax.contourf(Lon, Lat, Z)


cbar = fig.colorbar(cs)

plt.show()

geojson = geojsoncontour.contourf_to_geojson(
    contourf=cs,
    ndigits=3,
    unit='m'
)
#print (geojson)

with open('myfile1.geojson', 'w') as f:
   f.write(geojson)
f.close()


