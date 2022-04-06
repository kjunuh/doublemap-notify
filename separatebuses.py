import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import tzlocal  

# ts = float("1284101485")
timezone = tzlocal.get_localzone() # get pytz timezone
# locTime = datetime.fromtimestamp(ts, timezone)
df = pd.read_hdf('data/d2.h5').drop_duplicates()

df['time'] = [datetime.fromtimestamp(x,timezone).strftime("%I:%M:%S %p") for x in df['lastUpdate']]
df.sort_values(['lastUpdate'], ascending=True, inplace=True)
buses = [df.loc[df['name']==x] for x in df['name'].unique()]

def x(fName):
    stops = pd.read_hdf(fName, key='stops')
    routes = pd.read_hdf(fName, key='routes')
    rdf = routes.drop(routes.columns.difference(['id','name']), axis=1)
    rDict = rdf.to_dict()
    buses = pd.read_hdf(fName, key='buses')
    sbus = []
    for busID in buses['id'].unique():
        sbus.append(buses.loc[buses['id']==busID])
    

    