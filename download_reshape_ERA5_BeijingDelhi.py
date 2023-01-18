#To work you need to install the cds API following the instructions on this page https://cds.climate.copernicus.eu/api-how-to There are separate ones for if you are a windows user
#This file will download a lot of ERA5 data, you will then need to run Reshape_ERA5_into_CSV_tseries.py to pick out your site data
#The bit below 'area' is the lat/lon range you are covering
#The area works as [N,W,S,E]

import cdsapi
import pandas as pd
import xarray as xr

c = cdsapi.Client()

#Set lat/lon range
lon_beijing_max = 117
lon_beijing_min = 115.5
lat_beijing_max = 41
lat_beijing_min = 39

lon_delhi_max = 78
lon_delhi_min = 76
lat_delhi_max = 29.5
lat_delhi_min = 28


#Total accumulated precip during a time period
#The time is the end time, so accumulation over the previous hour

data_path = "C:/Work/Orbitrap/ERA5/"

#Beijing winter
filename = "Beijing_winter_ERA5_met.nc"
c.retrieve("reanalysis-era5-single-levels",
           {
               'variable': ['total_precipitation'],
               "product_type": "reanalysis",
               "year": 2016,
               'month': [11,12],
               'day': list(range(1,32)),
               'time': [
                   '00:00', '01:00', '02:00', '03:00',
                   '04:00', '05:00', '06:00', '07:00',
                   '08:00', '09:00', '10:00', '11:00',
                   '12:00', '13:00', '14:00', '15:00',
                   '16:00', '17:00', '18:00', '19:00',
                   '20:00', '21:00', '22:00', '23:00',
                   ],
               "format": "netcdf",
               'area': [
                   lat_beijing_max,lon_beijing_min,lat_beijing_min,lon_beijing_max]
               }, (data_path+filename))
         
#Beijing summer
filename = "Beijing_summer_ERA5_met.nc"
c.retrieve("reanalysis-era5-single-levels",
           {
               'variable': ['total_precipitation'],
               "product_type": "reanalysis",
               "year": 2017,
               'month': [5,6],
               'day': list(range(1,32)),
               'time': [
                   '00:00', '01:00', '02:00', '03:00',
                   '04:00', '05:00', '06:00', '07:00',
                   '08:00', '09:00', '10:00', '11:00',
                   '12:00', '13:00', '14:00', '15:00',
                   '16:00', '17:00', '18:00', '19:00',
                   '20:00', '21:00', '22:00', '23:00',
                   ],
               "format": "netcdf",
               'area': [
                   lat_beijing_max,lon_beijing_min,lat_beijing_min,lon_beijing_max]
               }, (data_path+filename))

#Delhi summer
filename = "Delhi_summer_ERA5_met.nc"
c.retrieve("reanalysis-era5-single-levels",
           {
               'variable': ['total_precipitation'],
               "product_type": "reanalysis",
               "year": 2018,
               'month': [5,6],
               'day': list(range(1,32)),
               'time': [
                   '00:00', '01:00', '02:00', '03:00',
                   '04:00', '05:00', '06:00', '07:00',
                   '08:00', '09:00', '10:00', '11:00',
                   '12:00', '13:00', '14:00', '15:00',
                   '16:00', '17:00', '18:00', '19:00',
                   '20:00', '21:00', '22:00', '23:00',
                   ],
               "format": "netcdf",
               'area': [
                   lat_delhi_max,lon_delhi_min,lat_delhi_min,lon_delhi_max]
               }, (data_path+filename))
           
#Delhi autumn
filename = "Delhi_autumn_ERA5_met.nc"
c.retrieve("reanalysis-era5-single-levels",
           {
               'variable': ['total_precipitation'],
               "product_type": "reanalysis",
               "year": 2018,
               'month': [10,11],
               'day': list(range(1,32)),
               'time': [
                   '00:00', '01:00', '02:00', '03:00',
                   '04:00', '05:00', '06:00', '07:00',
                   '08:00', '09:00', '10:00', '11:00',
                   '12:00', '13:00', '14:00', '15:00',
                   '16:00', '17:00', '18:00', '19:00',
                   '20:00', '21:00', '22:00', '23:00',
                   ],
               "format": "netcdf",
               'area': [
                   lat_delhi_max,lon_delhi_min,lat_delhi_min,lon_delhi_max]
               }, (data_path+filename))






#Load and proces the netCDF files
lat_beijing = 39.97444
lon_beijing = 116.3711
lat_delhi = 28.664
lon_delhi = 77.232


#Beijing winter
filepath = data_path + "Beijing_winter_ERA5_met.nc"
export_filepath = data_path + "Beijing_winter_ERA5_met.csv"
ds = xr.open_dataset(filepath)
df_site_data =  ds.sel(longitude=lon_beijing,latitude=lat_beijing,method="nearest",tolerance=0.5).to_dataframe().drop(['latitude','longitude'],axis=1)
df_site_data.to_csv(export_filepath)

#Beijing summer
filepath = data_path + "Beijing_summer_ERA5_met.nc"
export_filepath = data_path + "Beijing_summer_ERA5_met.csv"
ds = xr.open_dataset(filepath)
df_site_data =  ds.sel(longitude=lon_beijing,latitude=lat_beijing,method="nearest",tolerance=0.5).to_dataframe().drop(['latitude','longitude'],axis=1)
df_site_data.to_csv(export_filepath)

#Delhi summer
filepath = data_path + "Delhi_summer_ERA5_met.nc"
export_filepath = data_path + "Delhi_summer_ERA5_met.csv"
ds = xr.open_dataset(filepath)
df_site_data =  ds.sel(longitude=lon_delhi,latitude=lat_delhi,method="nearest",tolerance=0.5).to_dataframe().drop(['latitude','longitude'],axis=1)
df_site_data.to_csv(export_filepath)

#Delhi autumn
filepath = data_path + "Delhi_autumn_ERA5_met.nc"
export_filepath = data_path + "Delhi_autumn_ERA5_met.csv"
ds = xr.open_dataset(filepath)
df_site_data =  ds.sel(longitude=lon_delhi,latitude=lat_delhi,method="nearest",tolerance=0.5).to_dataframe().drop(['latitude','longitude'],axis=1)
df_site_data.to_csv(export_filepath)