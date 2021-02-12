# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 10:34:42 2021

@author: Jonny Taylor (jonathan.taylor@manchester.ac.uk Github:DrJonnyT)
"""
#To work you need to install the cds API following the instructions on this page https://cds.climate.copernicus.eu/api-how-to There are separate ones for if you are a windows user
#This file will download a lot of ERA5 data, you will end up with 1 file per month containing the various data parameters listed in 'variable' below
#The bit below 'area' is the lat/lon range you are covering

import cdsapi

import pandas as pd

c = cdsapi.Client()

#Load in the CSV with the lat/lon co-ordinates
#This has 3 columns of Site_Number, Longitude, Latitude
#Although in mine site number is actually a string

url=r"https://www.dropbox.com/s/f2yvbhlld6hzj8m/Sites_modifed2.csv?dl=1"
site_data=pd.read_csv(url)
#site_data=pd.read_csv('Sites_modifed2.csv')

site_data = site_data.set_index('Site_Number')
site_data.head()

#What is the max/min lat/lon range you need data for?
#You could use these or just set a range
lon_max = site_data['Longitude'].max()
lon_max = site_data['Longitude'].min()
lat_max = site_data['Latitude'].max()
lat_max = site_data['Latitude'].min()


#Load a grid of the selected area, with one file per month
for year in range(2016,2021):
    for month in range(1,13):

        filename = "met/" + str(year) + "-" + str(month) +"-" + "China_ERA5_met.nc"
        c.retrieve("reanalysis-era5-single-levels",
                   {
                       'variable': ['2m_temperature','mean_sea_level_pressure',
                          '10m_u_component_of_wind','10m_v_component_of_wind',
                          'boundary_layer_height','2m_dewpoint_temperature'],
                       "product_type": "reanalysis",
                       #"year": list(range(2016,2021)),
                       #'month': list(range(1,13),
                       'month': month,
                       'year': year,
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
                           15.,75.,60.,135.]   #Lat1 Lon1 Lat2 Lon2, a tiny area
                       }, filename)










# =============================================================================
# #THIS ONE DOESNT WORK BECAUSE BOOHOO IT WOULD HAVE TO LOAD TOO MANY DATA POINTS WAAAAA
# #But if you just want a short period then it could work
# #Load in the csv.
# #Loop through the CSV, setting a lat/lon range each time that is tiny and just located just around the
# #lat/lon of that point
# #It will DL one file per station, so name it by the station name
# 
# for index, row in site_data.iterrows():
#     lat = row['Latitude']
#     lon = row['Longitude']
#     filename = "ERA5_met_" + index + ".nc"
#     c.retrieve("reanalysis-era5-single-levels",
#         {
#         'variable': ['2m_temperature','mean_sea_level_pressure',
#                           '10m_u_component_of_wind','10m_v_component_of_wind',
#                           'boundary_layer_height','2m_dewpoint_temperature'],
#         "product_type": "reanalysis",
#         #"year": list(range(2016,2020)),
#         #'month': list(range(1,12)),
#         'month': 1,
#         'year': 2016,
#         'day': list(range(1,31)),
#                 'time': [
#                         '00:00', '01:00', '02:00', '03:00',
#                         '04:00', '05:00', '06:00', '07:00',
#                         '08:00', '09:00', '10:00', '11:00',
#                         '12:00', '13:00', '14:00', '15:00',
#                         '16:00', '17:00', '18:00', '19:00',
#                         '20:00', '21:00', '22:00', '23:00',
#                     ],
#         "format": "nc",
#         'area': [
#             lat+0.001,lon+0.001,lat,lon]   #Lat1 Lon1 Lat2 Lon2, a tiny area
#         }, filename)
# =============================================================================
