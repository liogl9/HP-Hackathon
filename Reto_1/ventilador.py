
cpd_loc = {"Leon": (42.57682, -5.59698), "Santiago": (42.90510, -8.50701), "Madrid": (
    40.51642, -3.89502), "BCN": (41.40124, 2.19122), "Sevilla": (37.39523, -6.01029)}

pista_lat = 3*cpd_loc["Leon"][0]-4*cpd_loc["Madrid"][0]+2*cpd_loc["Sevilla"][0]
pista_lon = 3*cpd_loc["Leon"][1]-4*cpd_loc["Madrid"][1]+2*cpd_loc["Sevilla"][1]
print(pista_lat, pista_lon)
