import pandas as pd
from datetime import datetime
import tzlocal
import matplotlib.pyplot as plt

fName = 'data/2hr3-30.h5'
stops = pd.read_hdf(fName, key='stops')
routes = pd.read_hdf(fName, key='routes')
buses = pd.read_hdf(fName, key='buses').sort_values('lastUpdate')
rDict = {}
for i in range(len(routes['id'])):        
    rDict[routes['id'].values[i]] = routes['name'].values[i]
buses['routeName'] = [rDict[x] for x in buses['route']]
buses['time'] = [datetime.fromtimestamp(x, tzlocal.get_localzone()).strftime("%I:%M:%S %p") for x in buses['lastUpdate']]
sbus = []
for busID in buses['id'].unique():
    sbus.append(buses.loc[buses['id']==busID])

def findCloseTo(df, lat, lon):
    df.loc[df['lat']-lat<=.0001 & df['lat']-lon<=.0001]
# sbus[0].loc[(abs(sbus[0]['lat']-lat)<=.000001) & (abs(sbus[0]['lon']-lon)<=.000001)] 