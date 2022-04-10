import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import tzlocal  

# ts = float("1284101485")
# locTime = datetime.fromtimestamp(ts, timezone)
df = pd.read_hdf('data/2hr3-30.h5', key='buses')
df.sort_values(['lastUpdate'], ascending=True, inplace=True)

df['time'] = [datetime.fromtimestamp(x,tzlocal.get_localzone()).strftime("%I:%M:%S %p") for x in df['lastUpdate']]

buses = [df.loc[df['name']==x] for x in df['name'].unique()]
print(buses)

def x(fName):
    stops = pd.read_hdf(fName, key='stops')
    routes = pd.read_hdf(fName, key='routes')
    rdf = routes.drop(routes.columns.difference(['id','name']), axis=1)
    rDict = rdf.to_dict()
    buses = pd.read_hdf(fName, key='buses')
    sbus = []
    for busID in buses['id'].unique():
        sbus.append(buses.loc[buses['id']==busID])
    print(sbus)


    