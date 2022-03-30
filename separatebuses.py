import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import tzlocal  # $ pip install tzlocal

ts = float("1284101485")
timezone = tzlocal.get_localzone() # get pytz timezone
locTime = datetime.fromtimestamp(ts, timezone)
df = pd.read_hdf('data/d2.h5').drop_duplicates()

df['time'] = [datetime.fromtimestamp(x,timezone).strftime("%I:%M:%S %p") for x in df['lastUpdate']]
df.sort_values(['lastUpdate'], ascending=True, inplace=True)
buses = [df.loc[df['name']==x] for x in df['name'].unique()]
print([x for x in buses])