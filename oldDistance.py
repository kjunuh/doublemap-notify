import pandas as pd
from requests import get 
from datetime import datetime

import tzlocal
import time
from tqdm import tqdm
from math import dist
from scipy.spatial.distance import cdist

def closest_node(node, nodes):
    return nodes[cdist([node], nodes).argmin()]

#def distfromstart(buspos,routename):
#    # busPos = [lat, lon], routeName = 'F' or '/F'
#    route = pd.read_hdf('routes/routePaths.h5', key = routeName).values
#    totalDist = 0
#    for i in range(len(route)-1):
#        if (dist(route[i], busPos) + dist(route[i], busPos)) < ((dist(route[i+1], busPos) + dist(route[i+2], busPos))): 
#            # and heading towards route[i+1]:
#            totalDist += dist(route[i], busPos)
#            return totalDist, i
#        else:
#            totalDist += (dist(route[i],route[i]))

point = [ 39.17965, -86.52678]
print(distFromStart(point,'F'))
