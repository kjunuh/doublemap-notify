import pandas as pd
from datetime import datetime
import tzlocal
import matplotlib.pyplot as plt

fName = 'data/2hr3-30.h5'
stops = pd.read_hdf(fName, key='stops')
routes = pd.read_hdf(fName, key='routes')
buses = pd.read_hdf(fName, key='buses').sort_values('lastUpdate')
saveFile = 'routes/routePaths.h5'

with pd.HDFStore(saveFile) as f:
    keys = f.keys()
paths = []
for rkey in keys:
    paths.append([rkey,pd.read_hdf('routes/routePaths.h5', key = rkey)])
