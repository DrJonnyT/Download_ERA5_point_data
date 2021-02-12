# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 10:25:41 2021

@author: Jonny Taylor (jonathan.taylor@manchester.ac.uk Github:DrJonnyT)
"""
#Loop through lots of ERA5 files, loaded using Download_ERA5.py and load up the met data process into one CSV per variable

import glob
import xarray as xr
import pandas as pd

#Load in CSV of sites
url=r"https://www.dropbox.com/s/f2yvbhlld6hzj8m/Sites_modifed2.csv?dl=1"
site_data=pd.read_csv(url)
#site_data=pd.read_csv('Sites_modifed2.csv')

site_data = site_data.set_index('Site_Number')
site_data.head()



#Loop through the different sites
for index, row in site_data.iterrows():
    lat = row['Latitude']
    lon = row['Longitude']
    #Make an array with the data in

    data_thissite = []
    #Loop through all the met files
    for filepath in glob.iglob(r'C:\Users\mbcx5jt5\Google Drive\China_met\met\*.nc'):
        try:
            ds = xr.open_dataset(filepath)
            df_thisfile_thissite =  ds.sel(longitude=lon,latitude=lat,method="nearest").to_dataframe().drop(['latitude','longitude'],axis=1)
            data_thissite.append(df_thisfile_thissite)        
 
##At the end you want one met file for each site, with all the variables
    
        except:
            print('Failed to load ' + filepath)
        
        
    export_filename = "met_sites/" + index + ".csv"
    pd.concat(data_thissite,axis=0).to_csv(export_filename)
        

type(data_thissite)
               )
tes = [ds.data_vars.keys(]
ds.sel(longitude=lon,latitude=lat,method="nearest").values()


#Nanjing_met_test = ds.to_dataframe()
#Nanjing_met_test.head()
ds.sel(obs=0)
Nanjing_met_site1 = (ds.sel(obs=0)).to_dataframe()
Nanjing_met_site2 = (ds.sel(obs=1)).to_dataframe()

##Need to then make a new dataframe with the met data and time
#First convert the time. The timestamp is in nanoseconds since 1st jan 1979, obviously
datetimes = pd.to_datetime(Nanjing_met_site1.index, unit='ns')

Nanjing_met_site1['utc_time']=pd.to_datetime(Nanjing_met_site1.index, unit='ns')
Nanjing_met_site1 = Nanjing_met_site1.set_index('utc_time')
Nanjing_met_site1 = Nanjing_met_site1.drop('realization', 1)
Nanjing_met_site1
    




ds = xr.open_dataset(filepath)

#ds.get_index('longitude')
#ds.get_index('latitude')



test = ds.t2m.sel(longitude=75.1,latitude=60.1,method="nearest").values
test = ds.sel(longitude=75.1,latitude=60.1,method="nearest").values
test

ds.get_index('time')


#Make new dataframe with the index of the time
df_t2m_thisfile = pd.DataFrame(ds.get_index('time'))

#Make an array with the data in
time_thisfile = ds.get_index('time')
data_thissite = []



