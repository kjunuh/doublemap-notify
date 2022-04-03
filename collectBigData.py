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
    start = time.strftime("%I:%M:%S%p", time.localtime())
    stops = pd.DataFrame(get("http://iub.doublemap.com/map/v2/stops").json())
    stops.drop(['code', 'ivr_code', 'description'], axis=1, inplace=True)

    routes = pd.DataFrame(get("http://iub.doublemap.com/map/v2/routes").json())
    routes.drop(['description'], axis=1, inplace=True)


    bigDF = pd.DataFrame()
    for i in tqdm(range(interval)):
        newDF = getDF()
        bigDF = pd.concat([newDF, bigDF]).drop_duplicates()
        time.sleep(1)
    end = time.strftime("%I:%M:%S%p", time.localtime())
    # fName = start+'_to_'+end+"_on_"+time.strftime("", time.localtime())
    fName = "testHDF1"
    stops.to_hdf(folder+fName+'.h5', key='stops')
    routes.to_hdf(folder+fName+'.h5', key='routes')
    bigDF.to_hdf(folder+fName+'.h5', key='buses')

saveData(2*60*60)