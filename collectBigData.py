import pandas as pd
from requests import get 
from datetime import datetime
import tzlocal
import time
from tqdm import tqdm

system = 'iub'
folder = 'data/'
def getDF():
    global system
    fetch = get(f'http://{system}.doublemap.com/map/v2/buses').json()
    df = pd.DataFrame(fetch)
    df.drop(['fields', 'bus_type', 'capacity', 'load'], axis=1, inplace=True)
    df.sort_values(by=['route'], inplace=True)
    return df

def stopName(id):
    stops = pd.DataFrame(get("http://iub.doublemap.com/map/v2/stops").json())
    try: return(stops.loc[stops['id']==id]['name'].values[0])
    except: 
        print("Stop ID Invalid")
        return 0

def saveData(interval):
    # interval in seconds
    global folder
    bigDF = pd.DataFrame()
    for i in tqdm(range(interval)):
        newDF = getDF()
        bigDF = pd.concat([newDF, bigDF])
        time.sleep(1)
    bigDF.drop_duplicates()

    routes = pd.DataFrame(get("http://iub.doublemap.com/map/v2/routes").json())
    bigDF.to_hdf(folder+'bus.h5', key='df')

saveData(30)