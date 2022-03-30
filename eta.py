from requests import get 
import pandas as pd 
import matplotlib.pyplot as plt
from datetime import datetime
import tzlocal

routes = pd.DataFrame(get("http://iub.doublemap.com/map/v2/routes").json())
stops = pd.DataFrame(get("http://iub.doublemap.com/map/v2/stops").json())
stops.drop(stops.columns.difference(['id','name', 'lat', 'lon']),axis=1, inplace=True)

print(stops)

routes.drop(routes.columns.difference(['id','short_name','active', 'stops', 'color']), axis=1, inplace=True)

# print(get("http://iub.doublemap.com/map/v2/eta", params={'stop':99,'route':787}).json()['etas'])
print((get("http://iub.doublemap.com/map/v2/eta", params={'stop':87,'route':817}).json()))