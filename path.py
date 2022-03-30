from requests import get
import matplotlib.pyplot as plt
import math

master = []
for x in get("http://iub.doublemap.com/map/v2/routes").json():
    path = x['path']
    lat, lon = [], []
    for i in range(len(path)): 
        if i%2: lon.append(path[i])
        else: lat.append(path[i])
    master.append([x['id'], x['name'], lat, lon])

# print(master)
pairMaster = []
for path in master:
    pairs = []
    # rLat = list(map(lambda x: round(x, 5), path[2])) # rounded lat/lon
    # rLon = list(map(lambda x: round(x, 5), path[3]))
    for i in range(len(path[3])):
        pairs.append([path[2][i], path[3][i]])
    pairMaster.append([path[0], path[1], pairs])
    plt.plot(path[2], path[3], label=path[1], alpha=.25)
    plt.scatter(path[2], path[3], label=path[1], s=.5)
    ax = plt.gca()

ax.set_facecolor('#dddddd')
ax.legend(loc='best')
print(pairMaster)

plt.plot(path[2], path[3], label=path[1], alpha=.25)
plt.show()
# math.dist([], [])