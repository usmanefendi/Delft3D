# Delft3D
Script konversi data NWP ke format .amp (data Mean sea level pressure), .amu (data angin u), .amv (data angin v) untuk input data meteorologi di Delft3D
Script ini dibuat menggunakan bahasa Python, sehingga pastikan untuk sudah menginstall interpreter python serta mengetahui bagaimana cara running program python yang bisa dicari tutorialnya di internet atau Youtube.

Script WRF2Delft3d.py digunakan untuk konversi file output WRF dalam format netCDF sebelum postprocessing menggunakan ARWpost, biasa memilii nama file wrfout.... Khusus untuk script ini masih menggunakan Python 2 sehingga harus diedit lagi jika dijalankan di Python 3.

Script ECMWF2Delft3d.py digunakan untuk konversi file netCDF dari ECMWF Era Interim (https://apps.ecmwf.int/datasets/data/interim-full-daily/levtype=sfc/) ke format Delft3D. Parameter yang didownload terdiri dari 10 metre U wind component, 10 metre V wind component, serta Mean sea level pressure. Untuk menggunakakan script tersebut, sesuaikan path input file dan output file pada bagian berikut.
```
inpf = 'Mei2018_2019.nc'
outf = 'datameteo_1tahun'
```

Script fnl2delft3d.py dan gfs2delft3d.py digunakan untuk konversi data grib FNL dan GFS ke format Delft3D. Karena harus membaca file grib, pastikan sudah menginstall library pygrib, mungkin harus menggunakan python di OS Linux, atau mungkin untuk pengguna windows bisa memakai Anaconda. Cara penggunaan kedua script sama, yakni dengan meletakan file grib FNL atau GFS dan script pada folder yang sama, kemudian jalankan script melalui command prompt atau terminal, maka semua file akan otomatis terkonversi

Script batimetri.py digunakan untuk konversi file netCDF batimetri GEBCO ke dalam format xyz yang biasa digunakan dalam Delft3D. Untuk menggunakan script tersebut sesuaikan path pada input dan output file pada bagian berikut
```
#Tulis nama inputfile dan outputfile
inputfile = 'GEBCO_2019.nc'
outputfile = 'GEBCO_2019_SCS.xyz'
```

Bagi yang menggunakan script ini mohon mensitasi publikasi berikut http://ejournal-balitbang.kkp.go.id/index.php/jkn/article/view/9634.
Jika membutuhkan bantuan bisa hubungi usman.ngc225@gmail.com atau usman.efendi@bmkg.go.id
