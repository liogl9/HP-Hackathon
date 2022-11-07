from itertools import product
from time import process_time
import numpy as np

t1_start = process_time() 

N = 10 # Orden de magnitud
WM = [*range(-N, N+1, 1)]
lats = [42.57682, 
        42.90510, 
        40.51642, 
        41.40124, 
        37.39523]

WM_list = [list(wm) for wm in product(WM, repeat=5)]

WM_possible_lats = np.dot(np.array(WM_list), np.array(lats))

WM_filter_lats = np.array([bool(wm >= 36.260 and wm <= 43.460) for wm in WM_possible_lats])

WM_lats = np.multiply(WM_possible_lats, WM_filter_lats)

print(len(WM_lats))

WM_lats = np.round(WM_lats[WM_lats != 0], 5)

print(len(WM_lats))

t1_stop = process_time()

print(len(WM_list))
