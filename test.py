from requests import get 
import pandas as pd 
import matplotlib.pyplot as plt
from time import sleep
from datetime import datetime
# import tzlocal 


routes = pd.DataFrame(get("http://iub.doublemap.com/map/v2/routes").json())
routes.drop(routes.columns.difference(['id','short_name','active', 'stops', 'color']),axis=1, inplace=True)
routes.set_index('short_name', inplace=True)

def getData(fetch):
    df = pd.DataFrame(fetch)
    df.drop(['fields', 'bus_type', 'capacity', 'load'], axis=1, inplace=True)
    df.sort_values(by=['route'], inplace=True)
    return df

# def transTime(timestamp):
#     timezone = tzlocal.get_localzone() 
#     local_time = datetime.fromtimestamp(timestamp, timezone)
#     return local_time.strftime("%H:%M:%S")

routes.loc[routes['id'] == 787]['color'].item()
df = pd.DataFrame(get('http://iub.doublemap.com/map/v2/buses').json())
df.drop(['fields', 'bus_type', 'capacity', 'load'], axis=1, inplace=True)
df.sort_values(by=['route'], inplace=True)
plt.scatter(df['lon'], df['lat'], c=["#"+routes.loc[routes['id'] == x]['color'].item() for x in df['route']])
plt.show()

# df = getData(get('http://iub.doublemap.com/map/v2/buses').json())
# [print(transTime(x)) for x in list(df["lastUpdate"])]
# while 1:
#     df = getData(get('http://iub.doublemap.com/map/v2/buses').json())
#     print(df)
#     sleep(3)