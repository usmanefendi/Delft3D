# -*- coding: utf-8 -*-
'''
Created on Fri Aug 23 10:52:47 2019

Script untuk mengkonversi data batimetri format netCDF ke format xyz
@author: Usman Efendi
usman.efendi@bmkg.go.id
Meteorologi STMKG
'''

from netCDF4 import Dataset
import numpy as np

#Tulis nama inputfile dan outputfile
inputfile = 'GEBCO_2019.nc'
outputfile = 'GEBCO_2019_SCS.xyz'

#Buka file nc
dset = Dataset(inputfile, 'r')
#sesuaikan nama variabel data pada lat, lon dan depth
lat = dset.variables['lat']
lon = dset.variables['lon']
depth = dset.variables['elevation']

batimetri = open(outputfile,'w')
for i in np.arange(65760,73681,1):
    print 'Memproses data ke ', i
    for j in np.arange(19200,26881,1):
        batimetri.write('{:.4f} {:.4f} {:.2f}\n'.format(lon[i],lat[j],depth[j,i]))
batimetri.close()        
print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
print '! PROCESSING BATHYMETRI DATA SUCCEED !'
print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'


