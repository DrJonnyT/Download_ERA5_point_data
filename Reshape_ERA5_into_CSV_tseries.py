# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 10:25:41 2021

@author: Jonny Taylor (jonathan.taylor@manchester.ac.uk Github:DrJonnyT)
"""
#Loop through lots of ERA5 files, loaded using Download_ERA5.py and load up the met data process into one CSV per variable

import glob
import xarray as xr
import pandas as pd
import pdb

#Load in CSV of sites
# url=r"https://www.dropbox.com/s/f2yvbhlld6hzj8m/Sites_modifed2.csv?dl=1"
# site_data=pd.read_csv(url)
# #site_data=pd.read_csv('Sites_modifed2.csv')

# site_data = site_data.set_index('Site_Number')

site_data=pd.read_csv(r'C:\Users\mbcx5jt5\Dropbox (The University of Manchester)\Air quality data in China\Manchester_AURN_latlon.csv')


###############################################################################
#Loop through the different sites
#Making one met file for each site
for index, row in site_data.iterrows():
    lat = row['Latitude']
    lon = row['Longitude']
    #Make an array with the data in
    print(lat)
    print(lon)
    data_thissite = []
    #Loop through all the met files
    for filepath in glob.iglob(r'C:\Work\Python\Github\Download_ERA5_point_data\met\Manchester\*.nc'):
        try:
            #pdb.set_trace()
            ds = xr.open_dataset(filepath)
            df_thisfile_thissite =  ds.sel(longitude=lon,latitude=lat,method="nearest",tolerance=0.5).to_dataframe().drop(['latitude','longitude'],axis=1)
            data_thissite.append(df_thisfile_thissite)        
 
        ##At the end you want one met file for each site, with all the variables
    
        except:
            print('Failed to load ' + filepath)
        
    #I think you need to have the directory /met_sites/ already created    
    export_filename = "met_sites/Manchester/" + str(index) + ".csv"
    pd.concat(data_thissite,axis=0).to_csv(export_filename)
        


#####FUNCTION NUMBER 2, DON'T NEED TO RUN THIS AT PRESENT
###############################################################################
#Loop through the different variable
#Create one file with all the pressure, one for all the temperature etc etc, with the columns being the different sites

# #First, what are the data variables?
# variable_names = list(xr.open_dataset(r'C:\Work\Python\Github\Download_ERA5_point_data\met\2016-1-China_ERA5_met.nc').keys())
# #data arrays of the latitude and longitude to use for indexing to extract only tyhe right data points
# lats = xr.DataArray(site_data['Latitude']) #'z' is an arbitrary name placeholder
# lons = xr.DataArray(site_data['Longitude'])

# #Now loop through the different variables
# for variable in variable_names:
#     first_iteration = 1    
#     #Loop through all the met files
#     for filepath in glob.iglob(r'C:\Work\Python\Github\Download_ERA5_point_data\met\*.nc'):
#         try:
#             ds = xr.open_dataset(filepath)
#             print('Loaded ' + filepath)
#             if(first_iteration):
#                 data_df = pd.DataFrame(ds[variable].sel(latitude = lats, longitude = lons, method = 'nearest').values,columns=site_data.index).set_index(ds.time.values)
#                 first_iteration=0
#             else:
#                 #Not the most efficient way of doing it, sue me!
#                 #Here there's some bullshit going on, the time is getting appended lots of times
#                 data_df = data_df.append(pd.DataFrame(ds[variable].sel(latitude = lats, longitude = lons, method = 'nearest').values,columns=site_data.index).set_index(ds.time.values))
                
#         except:
#             print('Failed to load ' + filepath)
        
#     #Now you have time and data for one variable
#     #I think you need to have the directory /met_vars/ already created
#     export_filename = ('met_vars/' + variable + '.csv')
#     data_df.index.rename('time',inplace=True)
#     data_df = data_df.sort_values(by='time',ascending=True)
#     data_df.to_csv(export_filename)
        