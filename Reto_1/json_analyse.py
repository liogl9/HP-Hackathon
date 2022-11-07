import geojson
import numpy as np
from tqdm import tqdm
from itertools import product
from math import ceil


def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return ceil(n * multiplier) / multiplier


def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx


N = 10  # Orden de magnitud
WM = [*range(-N, N+1, 1)]
lats = [42.57682,
        42.90510,
        40.51642,
        41.40124,
        37.39523]

json_file = open("Windmills.geojson")

data = geojson.load(json_file)

windmill_dict = {data["features"][i]["properties"]
                 ["name"]: data["features"][i] for i in range(len(data["features"]))}
key_list = list(windmill_dict.keys())
lat_list = [windmill_dict[key]["geometry"]["coordinates"][0][1]
            for key in key_list]

WM_list = [list(wm) for wm in product(WM, repeat=5)]

WM_possible_lats = np.dot(
    np.array(WM_list, dtype=np.float64), np.array(lats, dtype=np.float64))

WM_filter_lats = np.array([bool(wm >= 36.260 and wm <= 43.460)
                          for wm in WM_possible_lats])

WM_lats = np.multiply(WM_possible_lats, WM_filter_lats)

print(len(WM_lats))

WM_lats = np.round(WM_lats[WM_lats != 0], 5)
count = 0
for i in tqdm(WM_lats):
    idx = find_nearest(lat_list, i)
    if abs(lat_list[idx] - i) < 0.0001:
        count += 1
        # print(i, lat_list[idx], key_list[idx])
        if int(windmill_dict[key_list[idx]]["properties"]["windmill.config.blades.speed.limit"][:-4]) < int(windmill_dict[key_list[idx]]["properties"]["windmill.system.sensor.blades.speed"][:-4]):
            print(windmill_dict[key_list[idx]])
print(count)
