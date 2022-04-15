import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

route = pd.read_hdf('routes/routePaths.h5', key = 'B').values
stops = pd.read_hdf('data/2hr3-30.h5', key='stops')

plt.ion()

#plt.plot(route[0], route[1])
#plt.show()
#for i in range(len(route)):
#    plt.scatter([x[1] for x in route[:i]], [x[0] for x in route[:i]], alpha=.25)
#    plt.plot([x[1] for x in route[:i]], [x[0] for x in route[:i]])
#    plt.draw()
#    plt.pause(0.001)
#    if i < len(route)-2:
#        plt.clf()

plt.ioff()    

plt.scatter([x[1] for x in route], [x[0] for x in route], alpha=.25)
plt.plot([x[1] for x in route], [x[0] for x in route])
plt.scatter(stops['lon'].values, stops['lat'].values, marker='x')
plt.show()
