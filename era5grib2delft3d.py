'''
Program konversi data grib ERA5 menjadi input data meteorologi Delft3D
created by Usman Efendi
usman.efendi@bmkg.go.id
'''

import pygrib 
import numpy as np
from datetime import datetime
import os

file_path = "D:/Model/Delft3D/rembang/era5.grib"
file=pygrib.open(file_path)

file.seek(0)
# for i in file:
#     print(i)


#menulis data ERA5 ke format meteofile Delft3d
def meteo_file(parameter):
    dict = { 'mslp': {'nama':'Mean sea level pressure','satuan': 'Pa', 'quantity': 'air_pressure','ekstensi':'.amp'},
        'angin_u': {'nama':'10 metre U wind component','satuan': 'm s-1', 'quantity': 'x_wind','ekstensi':'.amu'},
        'angin_v': {'nama':'10 metre V wind component','satuan': 'm s-1', 'quantity': 'y_wind','ekstensi':'.amv'}}
    
    # buka file grib
    data = file.select(name=dict[parameter]['nama'])
    ref_time = data[0].validDate
    lat,lon = data[0].latlons()
    lat1 = np.squeeze(lat[:,0])
    lon1 = np.squeeze(lon[0,:])
    nlon = len(lon1)
    nlat  = len(lat1)
    lon_kiri = np.min(lon1)
    lat_bawah = np.min(lat1)
    dx = lon1[1]-lon1[0]
    dy = lat1[0]-lat1[1]

    
    fidp = open("{0}/Delft3D_{1}{2}".format(os.path.dirname(file_path),parameter,dict[parameter]['ekstensi']), "w") 
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
    fidp.write('quantity1        =    {0}\n'.format(dict[parameter]['quantity']))
    fidp.write('unit1            =    {0}\n'.format(dict[parameter]['satuan']))

    for i in range(len(data)):
        time = data[i].validDate
        delta_t = (time - ref_time)
        minutes = delta_t.total_seconds() / 60
        fidp.write('TIME             =   {0}  minutes since {1} +00:00\n'.format(minutes,ref_time))
        value = data[i].values
        for j in reversed(range(nlat)):
            get_val_row = value[j,:]
            for item in get_val_row:
                fidp.write(' '+'%.2f' %item)
            fidp.write('\n')  
    print('konversi data {0} selesai'.format(parameter))
    fidp.close()



meteo_file('mslp')      # opsi: 'mslp', 'angin_u', 'angin_v'
meteo_file('angin_u')
meteo_file('angin_v')

file.close()
