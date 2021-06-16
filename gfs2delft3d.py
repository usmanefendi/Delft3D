#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on Wed Oct 20 17:01:23 2020

@author: Usman
usman.efendi@bmkg.go.id

'''
import pygrib 
import numpy as np
import os

listfile = []
filename = os.listdir()
for file in filename:
    if file.endswith(".grib2"):
        listfile.append(file)
listfile.sort()

inputfile = listfile[0]
outputfile = inputfile[0:18]
file=pygrib.open(inputfile)
file.seek(0)
# for list in file:
	# print list




##memproses data MSLP
amp = file.select(name='Pressure reduced to MSL')[0] #ekstrak variabel mslp
get_amp = amp.values
lats,lons = amp.latlons() #ekstrak koordinat lat lon
lat1 = np.squeeze(lats[:,0])
lon1 = np.squeeze(lons[0,:])
nlon = len(lon1)
nlat  = len(lat1)
lon_kiri = np.min(lon1)
lat_bawah = np.min(lat1)
dx = lon1[1]-lon1[0]
dy = lat1[0]-lat1[1]

#menulis data MSLP ke file .amp
fidp = open("Delft3D_"+outputfile+".amp", "w") 
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

for nama in listfile:
    readdata_amp = pygrib.open(nama)
    time = readdata_amp[1]
    ref_time = time.analDate #waktu referensi
    cur_time = time.validDate #waktu forecast saat ini
    time_step = time.forecastTime
    time_step *= 60 #forecast time sekian menit dari waktu data analisis
    print("memproses data MSLP forecast tanggal ",cur_time,"...")
    fidp.write('TIME             =   {0}  minutes since {1} +00:00\n'.format(time_step,ref_time))
    data = readdata_amp.select(name='Pressure reduced to MSL')[0]
    amp = data.values
    tekanan = np.round(amp[:,:])
    for j in reversed(range(nlat)):
        get_amp_row = tekanan[j,:]
        for item in get_amp_row:
            fidp.write(' '+'%6i' %item)
        fidp.write('\n')            
fidp.close()

#Memproses data .amu
fidu = open("Delft3D_"+outputfile+".amu", "w") 
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

for nama in listfile:
    readdata_amu = pygrib.open(nama)
    time = readdata_amu[1]
    ref_time = time.analDate #waktu referensi
    cur_time = time.validDate #waktu forecast saat ini
    time_step = time.forecastTime
    time_step *= 60 #forecast time sekian menit dari waktu data analisis
    print("memproses data angin U forecast tanggal ",cur_time,"...")
    fidu.write('TIME             =   {0}  minutes since {1} +00:00\n'.format(time_step,ref_time))
    data = readdata_amu.select(name='10 metre U wind component')[0]
    angin_u = data.values
    uwnd = angin_u[:,:]
    for k in reversed(range(nlat)):
        get_amu_row = uwnd[k,:]
        for item in get_amu_row:
            fidu.write(' '+'%6.1f' %item)
        fidu.write('\n')            
fidu.close()

#Memproses data .amv
fidv = open("Delft3D_"+outputfile+".amv", "w") 
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

for nama in listfile:
    readdata_amv = pygrib.open(nama)
    time = readdata_amv[1]
    ref_time = time.analDate #waktu referensi
    cur_time = time.validDate #waktu forecast saat ini
    time_step = time.forecastTime
    time_step *= 60 #forecast time sekian menit dari waktu data analisis
    print("memproses data angin V forecast tanggal ",cur_time,"...")
    fidv.write('TIME             =   {0}  minutes since {1} +00:00\n'.format(time_step,ref_time))
    data = readdata_amv.select(name='10 metre V wind component')[0]
    angin_v = data.values
    vwnd = angin_v[:,:]
    for k in reversed(range(nlat)):
        get_amv_row = vwnd[k,:]
        for item in get_amv_row:
            fidv.write(' '+'%6.1f' %item)
        fidv.write('\n')            
fidv.close()

# u = file.select(name='10 metre U wind component')[0]
# amu = u.values
# v = file.select(name='10 metre V wind component')[0]
# amv = v.values