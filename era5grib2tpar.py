'''
Program konversi data grib ERA5 menjadi input data wave boundary condition Delft3D
created by Usman Efendi
usman.efendi@bmkg.go.id
'''

import pygrib 
import numpy as np
from datetime import datetime
import os

file_path = "D:/Model/Delft3D/rembang/era5.grib"
file=pygrib.open(file_path)
lintang = -6.449037
bujur = 111.489

file.seek(0)
# for i in file:
#     print(i)
# print(file)

# fungsi mengambil indeks data sesuai koordinat
def find_nearest(array, value):
	array = np.asarray(array)
	idx = (np.abs(array - value)).argmin()
	assert isinstance(idx, object)
	return int(idx)

# fungsi ekstrak data titik
def point_data(nama,lintang,bujur):
	case=[]
	data = file.select(name=nama)
	lat,lon = data[0].latlons()
	lat_list = lat[:,0]
	lon_list = lon[0,:]
	lat_idx = find_nearest(lat_list,lintang)
	lon_idx = find_nearest(lon_list,bujur)
	for i in range(len(data)):
		value = data[i].values
		val_point = value[lat_idx,lon_idx]
		# print(val_point)
		case.append(val_point)
	return case
def datetime_spr(nama):
	case_t = []
	data = file.select(name=nama)
	spr = [30] * len(data)
	for j in range(len(data)):
		time = data[j].validDate
		case_t.append(time.strftime("%Y%m%d.%H%M%S"))
	return case_t, spr


hs = np.round(point_data(nama='Significant height of combined wind waves and swell',
				lintang=lintang,bujur=bujur),3)
period = np.round(point_data(nama='Mean wave period',
				lintang=lintang,bujur=bujur),3)
dir_hs = np.round(point_data(nama='Mean wave direction',
				lintang=lintang,bujur=bujur)).astype(int)
time,spread = datetime_spr(nama='Significant height of combined wind waves and swell')

# tulis kedalam file TPAR
tpar = open("{0}/TPAR_{1}_{2}.bnd".format(os.path.dirname(file_path),lintang,bujur), "w")
tpar.write('TPAR\n')
for k in range(len(hs)):
	tpar.write('{0} {1} {2} {3} {4}\n'.format(time[k],hs[k],period[k],dir_hs[k],spread[k]))
tpar.close() 
file.close()

