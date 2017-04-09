from bs4 import BeautifulSoup
import pandas as pd
import re

for i in range(1, 48):
    if i < 10:
        soup = BeautifulSoup(open("data/AL142016_00" + str(i) + 'adv_TRACK.kml'), "html.parser")
    else:
        soup = BeautifulSoup(open("data/AL142016_0" + str(i) + 'adv_TRACK.kml'), "html.parser")

    item = soup.find_all('placemark')[1]
    print(item)

