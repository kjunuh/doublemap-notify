import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import tzlocal 

fName = 'data/2hr3-30.h5'
saveFile = 'routes/routePaths.h5'
stops = pd.read_hdf(fName, key='stops')
routes = pd.read_hdf(fName, key='routes')

def makePathDF(routesDF):
    for routeName in routesDF['short_name'].unique():
        route = routesDF.loc[routesDF['short_name'] == routeName]
        print(route)
        outDF = pd.DataFrame()
        outDF['lat'] = [coordinate for i, coordinate in enumerate(route['path'].values[0]) if not i%2]
        outDF['lon'] = [coordinate for i, coordinate in enumerate(route['path'].values[0]) if i%2]
        outDF.to_hdf(saveFile, key=routeName)
    # return outDF

with pd.HDFStore('routes/routePaths.h5') as f:
    keys = f.keys()

coords = pd.read_hdf('routes/routePaths.h5', key='F')
plt.plot(coords['lon'], coords['lat'], alpha=.25)
plt.scatter(coords['lon'], coords['lat'], s=3, marker='x')
plt.savefig("F_route.png")

# def distanceTraveled(lat, lon, routePath):




# plot all routes
# for key in keys:
#     coords = pd.read_hdf('routes/routePaths.h5', key=key)
#     plt.plot(coords['lon'], coords['lat'], alpha=.25)
#     plt.scatter(coords['lon'], coords['lat'], s=3, marker='x')

# plt.show()

