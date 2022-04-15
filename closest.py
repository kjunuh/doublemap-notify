import pandas as pd
from datetime import datetime
import tzlocal
import matplotlib.pyplot as plt
from tqdm import tqdm, trange
from math import dist

ROUTEPATH = 'routes/routePaths.h5'
def closestPoints(busPos, routeName):
    routeCoords = pd.read_hdf(ROUTEPATH, key=routeName).values
    small, second = 100, 100

    for i in routeCoords:
        print(busPos, i)
        a = dist(busPos, i)
        print("dist:",a<small)
        if a < small: 
            small = i
        
        a=0
    return small, second

p = [39.168404, -86.526893]
print(closestPoints(p, 'F'))
