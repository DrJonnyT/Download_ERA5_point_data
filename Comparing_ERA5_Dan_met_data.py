# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 11:18:11 2021

@author: mbcx5jt5

Comparing the ERA5 met data to some ground data Dantong sent me
"""

import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
import metpy.calc as mpcalc

##Import Dan met data
#2017 met data for lat 118.909, lon 31.332.
df_Dan = pd.read_csv(r'C:\Users\mbcx5jt5\Google Drive\China_met\From_Dan\Danmet_1-3.csv')

df_Dan = df_Dan.append(pd.read_csv(r'C:\Users\mbcx5jt5\Google Drive\China_met\From_Dan\Danmet_4-6.csv'))

df_Dan = df_Dan.append(pd.read_csv(r'C:\Users\mbcx5jt5\Google Drive\China_met\From_Dan\Danmet_7-9.csv'))
df_Dan = df_Dan.append(pd.read_csv(r'C:\Users\mbcx5jt5\Google Drive\China_met\From_Dan\Danmet_10-12.csv'))

df_Dan.replace(999999.0,np.nan,inplace=True)
df_Dan.replace(999998.0,np.nan,inplace=True)
df_Dan.plot.line(y='Temp_C',x='Time')

df_Dan['datetime'] = pd.to_datetime(df_Dan['Time'],format="%d/%m/%Y %H:%M")
df_Dan.plot.line(y='Temp_C',x='datetime')

#df_Dan = df_Dan.sort_values(by='datetime',ascending=True)
df_Dan=df_Dan.set_index('datetime')
df_Dan = df_Dan.drop('Time',axis=1)

df_Dan['Temp_C'].plot.line()

#Get rid of bad values


##Import ERA5
df_ERA5 = pd.read_csv(r'C:\Users\mbcx5jt5\Google Drive\China_met\met_sites\1151A.csv')
df_ERA5['datetime'] = pd.to_datetime(df_ERA5['time'])
df_ERA5 = df_ERA5.set_index('datetime')
df_ERA5['msl'] = df_ERA5['msl'] / 100
df_ERA5['t2m'] = df_ERA5['t2m'] - 273.15
df_ERA5['d2m'] = df_ERA5['d2m'] - 273.15


#Combine the dataframes
combined_df=pd.merge(df_Dan,df_ERA5, left_index=True, right_index=True)

#Pressure
combined_df.plot.scatter('SLPress','msl')
plt.xlabel('Dantong data')
plt.ylabel('ERA5')
plt.title('Sea level pressure(mbar)')
#plt.show()
plt.savefig("figs/Pressure_scatter.png")

#Temperature
combined_df.plot.scatter('Temp_C','t2m')
plt.xlabel('Dantong data')
plt.ylabel('ERA5')
plt.title('Temperature (C)')
#plt.show()
plt.savefig("figs/Temp_scatter.png")

#Wind
from metpy.units import units
Danwspeed = combined_df['wind_speed_10min'].values * units('m/s')
Danwdir = combined_df['wind_dir_10min'].values * units.degrees

combined_df['wind_u_10min'] = mpcalc.wind_components(Danwspeed , Danwdir)[0]
combined_df['wind_v_10min'] = mpcalc.wind_components(Danwspeed , Danwdir)[1]

combined_df.plot.scatter('wind_u_10min','u10')
plt.xlabel('Dantong data')
plt.ylabel('ERA5')
plt.title('Wind u (m/s)')
#plt.show()
plt.savefig("figs/wind_u_scatter.png")

combined_df.plot.scatter('wind_v_10min','v10')
plt.xlabel('Dantong data')
plt.ylabel('ERA5')
plt.title('Wind v (m/s)')
#plt.show()
plt.savefig("figs/wind_v_scatter.png")


#RH

ERA5_T = combined_df['t2m'].values * units.degC
ERA5_Td = (combined_df['d2m'].values) * units.degC
Dan_T = combined_df['Temp_C'].values * units.degC
Dan_RH = combined_df['RH'].values/100 * units('')
Dan_Td = mpcalc.thermo.dewpoint_from_relative_humidity(Dan_T , Dan_RH)
combined_df['Dan_Td'] = Dan_Td

combined_df['RH_ERA5'] = mpcalc.relative_humidity_from_dewpoint(ERA5_T, ERA5_Td)*100

combined_df.plot.scatter('RH','RH_ERA5')
plt.xlabel('Dantong data')
plt.ylabel('ERA5')
plt.title('RH (%)')
#plt.show()
plt.savefig("figs/RH_scatter.png")


#Tdew
combined_df.plot.scatter('Dan_Td','d2m')
plt.xlabel('Dantong data')
plt.ylabel('ERA5')
plt.title('Dew point (C)')
#plt.show()
plt.savefig("figs/Dew_point_scatter.png")






#Calculating RH myself
from math import exp
import numpy as np
combined_df['RH_ERA5'] = 100*(np.exp((17.625*combined_df['d2m'].values)/(243.04+combined_df['d2m'].values))/np.exp((17.625*combined_df['t2m'].values)/(243.04+combined_df['t2m'].values)))






combined_df[['SLPress','msl']].plot.line()
combined_df[['Temp_C','t2m']].plot.line()

combined_df[['Dan_Td','d2m']].plot.line()
combined_df[['RH','RH_ERA5']].plot.line()


#What is the distance between Dan's site and 1151A?
import geopy.distance
coords_Dan = (31.332,118.909)
coords_1151A = (32.1083,118.803)
print(geopy.distance.distance(coords_Dan, coords_1151A).km)
#87km away

