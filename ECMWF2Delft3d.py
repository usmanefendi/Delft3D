# -*- coding: utf-8 -*-
'''
Created on Fri May  3 11:03:02 2019

@author: Usman Efendi
usman.efendi@bmkg.go.id
Meteorologi STMKG
'''

from netCDF4 import Dataset
import numpy as np
#from wrf import getvar
from datetime import datetime,timedelta


inpf = 'Mei2018_2019.nc'
outf = 'datameteo_1tahun'
dset = Dataset(inpf)
ref_time = datetime(2007,01,01,00,00,00)
start_run = datetime(2018,05,01,00,00,00)

lon = dset.variables['longitude'][:]
lat = dset.variables['latitude'][:]
time = dset.variables['time'][:]
print len(time)
print np.shape(lat)
#Domain
nlat = len(lat)
nlon = len(lon)
lon_kiri = np.min(lon)
lon_kanan = np.max(lon)
lat_bawah = np.min(lat)
lat_atas = np.max(lat)
dx = lon[1]-lon[0]
dy = lat[0]-lat[1]

#fungsi datenum
def datetime2matlabdn(dt):
    ord = dt.toordinal()
    mdn = dt + timedelta(days = 366)
    frac = (dt-datetime(dt.year,dt.month,dt.day,0,0,0)).seconds / (24.0 * 60.0 * 60.0)
    return mdn.toordinal() + frac
print ' Processing Delft3D Meteo File from WRF Output File'
# #Pressure
fidp = open(outf+".amp", "w") 
fidp.write('FileVersion      =    1.03\n')
fidp.write('filetype         =    meteo_on_equidistant_grid\n')
fidp.write('NODATA_value     =    -999\n')
fidp.write('n_cols           =    %5i\n' %nlon)
fidp.write('n_rows           =    %5i\n'%nlat)
fidp.write('grid_unit        =    degree\n')
fidp.write('x_llcorner       =    %5.3f\n'%lon_kiri)
fidp.write('y_llcorner       =    %5.3f\n'%lat_bawah)
fidp.write('dx               =    %5.3f\n'%dx)
fidp.write('dy               =    %5.3f\n'%dy)
fidp.write('n_quantity       =    1\n')
fidp.write('quantity1        =    air_pressure\n')
fidp.write('unit1            =    Pa\n')

for i in xrange(len(time)):
    msl = dset.variables['msl'][i,:,:]
    t_difmsl = time[i]*60
     #t_difmsl = (datetime2matlabdn(start_run)-datetime2matlabdn(ref_time))*1440+time[i]
	 #print ' extracting msl data for ',time[i],' minutes from ',start_run
    fidp.write('TIME             =   %.2f   minutes since 1900-01-01 00:00:00 +00:00\n'%t_difmsl)
    for j in reversed(xrange(nlat)):
        msl_row = msl[j,:]
        for item in msl_row:
            fidp.write(' '+'%6i' %item)
        fidp.write('\n')            
fidp.close()

 #U wind
fidu = open(outf+".amu", "w")
fidu.write('FileVersion      =    1.03\n')
fidu.write('filetype         =    meteo_on_equidistant_grid\n')
fidu.write('NODATA_value     =    -999\n')
fidu.write('n_cols           =    %5i\n' %nlon)
fidu.write('n_rows           =    %5i\n'%nlat)
fidu.write('grid_unit        =    degree\n')
fidu.write('x_llcorner       =    %5.3f\n'%lon_kiri)
fidu.write('y_llcorner       =    %5.3f\n'%lat_bawah)
fidu.write('dx               =    %5.3f\n'%dx)
fidu.write('dy               =    %5.3f\n'%dy)
fidu.write('n_quantity       =    1\n')
fidu.write('quantity1        =    x_wind\n')
fidu.write('unit1            =    m s-1\n')
for i in xrange(len(time)):
    u = dset.variables['u10'][i,:,:]
    t_difu = time[i]*60
	#t_difu = (datetime2matlabdn(start_run)-datetime2matlabdn(ref_time))*1440+time[i]
    print ' extracting u wind data for ',time[i],' minutes from ',start_run
    fidu.write('TIME             =   %.2f   minutes since 1900-01-01 00:00:00 +00:00\n'%t_difu)
    for j in reversed(xrange(nlat)):
        u_row = u[j,:]
        for item in u_row:
            fidu.write(' '+'%6.1f' %item)
        fidu.write('\n')            
fidu.close()


# #V wind
fidv = open(outf+".amv", "w")
fidv.write('FileVersion      =    1.03\n')
fidv.write('filetype         =    meteo_on_equidistant_grid\n')
fidv.write('NODATA_value     =    -999\n')
fidv.write('n_cols           =    %5i\n' %nlon)
fidv.write('n_rows           =    %5i\n'%nlat)
fidv.write('grid_unit        =    degree\n')
fidv.write('x_llcorner       =    %5.3f\n'%lon_kiri)
fidv.write('y_llcorner       =    %5.3f\n'%lat_bawah)
fidv.write('dx               =    %5.3f\n'%dx)
fidv.write('dy               =    %5.3f\n'%dy)
fidv.write('n_quantity       =    1\n')
fidv.write('quantity1        =    y_wind\n')
fidv.write('unit1            =    m s-1\n')
for i in xrange(len(time)):
    v = dset.variables['v10'][i,:,:]
    t_difv = time[i]*60
    #t_difv = (datetime2matlabdn(start_run)-datetime2matlabdn(ref_time))*1440+time[i]
    print ' extracting v wind data for ',time[i],' minutes from ',start_run
    fidv.write('TIME             =   %.2f   minutes since 1900-01-01 00:00:00 +00:00\n'%t_difv)
    for j in reversed(xrange(nlat)):
        v_row = v[j,:]
        for item in v_row:
            fidv.write(' '+'%6.1f' %item)
        fidv.write('\n')            
fidv.close()
print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
print '! PROCESSING DELFT3D METEO FILE SUCCEED !'
print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'