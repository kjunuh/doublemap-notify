import pandas as pd
from requests import get 
from datetime import datetime

import matplotlib.pyplot as plt
import tzlocal
import time
from tqdm import tqdm
from math import dist
from scipy.spatial.distance import cdist

def closest_node(node, nodes):
    print(cdist([node], nodes).argmin())
    return nodes[cdist([node], nodes).argmin()]

def distFromStart(dfElem, routes):
    point = [dfElem['lat'], dfElem['lon']]
    # print(dfElem['route'])
    path = routes.loc[routes['id'] == dfElem['route']]['path'].values[0]
    # print(path)
    coords = [(path[i], path[i+1]) for i in range(0, len(path), 2)]
    closest = closest_node(point, coords)
    
    # plt.scatter(closest[0], closest[1], marker='*')
    # plt.scatter(point[0], point[1], marker='x')
    # plt.scatter([x[0] for x in coords], [x[1] for x in coords], marker='o', alpha=.5)
    # plt.show()
    
    # print(coords)
    

fName = 'data/2hr3-30.h5'
buses = pd.read_hdf(fName, key='buses').sort_values('lastUpdate')
routes = pd.read_hdf(fName, key='routes')

distFromStart(buses.iloc[20], routes)